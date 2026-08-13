#!/usr/bin/env bash
#
# Publie la configuration Apache du site — les DEUX vhosts, pas seulement celui
# du depot.
#
#     sudo ./deploy-vhost.sh [domaine]
#
# Pourquoi ce script existe : certbot cree le vhost HTTPS en copiant le vhost
# HTTP, puis les deux divergent. Or c'est le vhost HTTPS qui sert la totalite du
# trafic. Modifier deploy/<domaine>.conf et le reinstaller ne changeait donc
# strictement rien pour les visiteurs -- une correction de cache est restee
# invisible comme ca.
#
# Fait, dans l'ordre et en s'arretant a la premiere erreur :
#   1. installe les reglages communs dans conf-available (sans les activer
#      globalement : ~18 autres vhosts tournent sur ce serveur)
#   2. installe le vhost HTTP
#   3. fait inclure les reglages communs par le vhost HTTPS de certbot, en
#      retirant les blocs qu'il en dupliquait
#   4. configtest puis reload -- jamais de restart
#   5. VERIFIE les en-tetes reellement servis en HTTPS
#
# L'etape 5 est la raison d'etre du script : c'est elle qui aurait signale que
# la configuration corrigee n'etait pas celle qui repondait.
#
# Le script est idempotent : le relancer ne casse rien.
set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"
DOMAIN="${1:-rubiks.coality.net}"
AVAIL=/etc/apache2/sites-available
CONF=/etc/apache2/conf-available/rubiks-common.conf
SSL="$AVAIL/$DOMAIN-le-ssl.conf"

die() { echo "ARRET : $*" >&2; exit 1; }
step() { echo; echo "== $* =="; }
horodatage() { date +%Y%m%d-%H%M%S; }

[ "$(id -u)" = 0 ] || die "a lancer en root : sudo $0 $DOMAIN"
[ -f "deploy/rubiks-common.conf" ] || die "deploy/rubiks-common.conf introuvable"
[ -f "deploy/$DOMAIN.conf" ] || die "deploy/$DOMAIN.conf introuvable"

# ------------------------------------------------------ 1. reglages communs
step "1/5  reglages communs"
install -m 644 deploy/rubiks-common.conf "$CONF"
echo "  $CONF"
echo "  (volontairement pas active par a2enconf : chaque vhost l'inclut)"

# ----------------------------------------------------------- 2. vhost HTTP
step "2/5  vhost HTTP"
install -m 644 "deploy/$DOMAIN.conf" "$AVAIL/$DOMAIN.conf"
a2ensite "$DOMAIN.conf" >/dev/null
echo "  $AVAIL/$DOMAIN.conf"

# ---------------------------------------------------------- 3. vhost HTTPS
step "3/5  vhost HTTPS (celui qui sert le trafic)"
if [ ! -f "$SSL" ]; then
    echo "  $SSL absent : pas de HTTPS a configurer"
elif grep -q 'rubiks-common.conf' "$SSL"; then
    echo "  inclut deja les reglages communs"
else
    cp -a "$SSL" "$SSL.bak.$(horodatage)"
    echo "  sauvegarde : $SSL.bak.*"
    python3 - "$SSL" <<'PYEOF'
import re, sys

p = sys.argv[1]
s = open(p, encoding='utf-8').read()

# Blocs que certbot a copies du vhost HTTP et que le fichier commun reprend.
# Les laisser en place ferait coexister deux fois les memes directives dans le
# meme vhost, avec des valeurs differentes.
for motif in (r'[ \t]*<Directory [^>]*>.*?</Directory>\n',
              r'[ \t]*<IfModule mod_deflate\.c>.*?</IfModule>\n',
              r'[ \t]*<IfModule mod_expires\.c>.*?</IfModule>\n',
              r'[ \t]*<IfModule mod_headers\.c>.*?</IfModule>\n'):
    s = re.sub(motif, '', s, flags=re.S)

INCLUDE = '    Include conf-available/rubiks-common.conf\n'
if INCLUDE not in s:
    m = re.search(r'^[ \t]*DocumentRoot[^\n]*\n', s, re.M)
    if m:
        s = s[:m.end()] + '\n' + INCLUDE + s[m.end():]
    else:
        s = s.replace('</VirtualHost>', INCLUDE + '</VirtualHost>', 1)
    assert INCLUDE in s, "l'Include n'a pas pu etre insere"

s = re.sub(r'\n{3,}', '\n\n', s)
open(p, 'w', encoding='utf-8').write(s)
print('  blocs dupliques retires, Include ajoute')
PYEOF
fi

# ------------------------------------------------- 4. controle et rechargement
step "4/5  configtest puis reload"
apache2ctl configtest
systemctl reload apache2
echo "  Apache recharge (aucun restart)"

# ------------------------------------------- 5. ce qui est REELLEMENT servi
step "5/5  en-tetes reellement servis en HTTPS"
fail=0
verifie() {                                    # url, motif attendu, libelle
    en_tetes="$(curl -sI --max-time 15 "https://$DOMAIN$1" || true)"
    if echo "$en_tetes" | grep -qi "$2"; then
        printf '  %-34s OK\n' "$3"
    else
        printf '  %-34s ATTENDU « %s »\n' "$3" "$2"
        echo "$en_tetes" | grep -i 'cache-control' | sed 's/^/      recu : /'
        fail=1
    fi
}
verifie /                       'cache-control:.*\(no-cache\|max-age=0\)' 'HTML revalide a chaque visite'
verifie /assets/extra.css       'cache-control:.*max-age=3600' 'CSS cache 1 heure'
verifie /                       'x-content-type-options'      'en-tete de securite present'

echo
[ "$fail" = 0 ] && echo "OK — la configuration servie est bien celle du depot." \
                || die "les en-tetes servis ne correspondent pas : voir ci-dessus."
