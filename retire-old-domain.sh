#!/usr/bin/env bash
#
# Retire proprement un ancien domaine dont l'enregistrement DNS a ete supprime.
#
#     sudo ./retire-old-domain.sh rubik.coality.net
#
# A lancer quand le domaine n'existe plus chez le registrar et qu'on ne compte
# pas le recreer. Tant qu'il reste declare ici, certbot tentera de renouveler
# son certificat a l'approche de l'expiration, echouera a chaque passage du
# timer (la validation HTTP suppose que le domaine resolve) et fera sortir
# `certbot renew` en erreur — ce qui masque les vrais problemes.
#
# Fait, dans l'ordre et en s'arretant a la premiere erreur :
#   1. refuse d'agir si le domaine resout encore, ou s'il est encore servi
#   2. desactive ses vhosts, teste la configuration, recharge Apache
#   3. supprime son certificat (certbot delete)
#
# ORDRE IMPORTANT : les vhosts d'abord. Supprimer le certificat en premier
# laisserait Apache pointer vers des fichiers absents — `configtest` echouerait
# et le prochain reload, meme sans rapport, serait bloque.
#
# Prudence : jamais de restart (une vingtaine d'autres vhosts tournent sur ce
# serveur), toujours configtest puis reload.
#
# Le script est idempotent : le relancer ne casse rien.
set -euo pipefail

OLD="${1:-}"
cd "$(dirname "$(readlink -f "$0")")"

die() { echo "ARRET : $*" >&2; exit 1; }
step() { echo; echo "== $* =="; }

[ -n "$OLD" ] || die "usage : sudo $0 <ancien-domaine>"
[ "$(id -u)" = 0 ] || die "a lancer en root : sudo $0 $OLD"

# --------------------------------------------------- 1. le domaine est-il mort
step "1/3  controles"
if getent hosts "$OLD" >/dev/null 2>&1; then
    die "$OLD resout encore. Retirer d'abord l'enregistrement DNS, ou verifier
       que c'est bien ce domaine-la qu'on veut abandonner."
fi
echo "  $OLD ne resout plus"

code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 "http://$OLD/" || echo 000)"
[ "$code" = 000 ] || die "http://$OLD/ repond encore ($code) : ne pas retirer."
echo "  plus rien ne repond sur $OLD"

# ------------------------------------------------------------- 2. les vhosts
step "2/3  vhosts Apache"
found=0
for conf in "$OLD.conf" "$OLD-le-ssl.conf"; do
    if [ -L "/etc/apache2/sites-enabled/$conf" ]; then
        a2dissite "$conf" >/dev/null
        echo "  desactive : $conf"
        found=1
    else
        echo "  deja inactif : $conf"
    fi
done
if [ "$found" = 1 ]; then
    apache2ctl configtest
    systemctl reload apache2
    echo "  Apache recharge"
fi

# --------------------------------------------------------- 3. le certificat
step "3/3  certificat"
if certbot certificates 2>/dev/null | grep -qE "Certificate Name: +$OLD\$"; then
    certbot delete --cert-name "$OLD" --non-interactive
    echo "  lignee $OLD supprimee"
else
    echo "  aucun certificat au nom de $OLD"
fi
apache2ctl configtest

echo
echo "OK — $OLD est retire. Les vhosts desactives restent dans"
echo "     /etc/apache2/sites-available/ si tu veux les relire."
