#!/usr/bin/env bash
#
# Bascule complete du site vers un nouveau domaine, en une commande.
#
#     sudo ./deploy-domain.sh rubiks.coality.net
#
# Fait, dans l'ordre et en s'arretant a la premiere erreur :
#   1. verifie que le DNS du nouveau domaine pointe bien sur cette machine
#   2. installe et active le vhost, teste la conf, recharge Apache
#   3. obtient le certificat (certbot)
#   4. remplace l'ancien vhost par une redirection 301 (le referencement suit)
#   5. reecrit le domaine dans les sources et reconstruit les trois sites
#   6. verifie le resultat en HTTPS
#
# Prudence : on ne fait JAMAIS "systemctl restart apache2" — une vingtaine
# d'autres vhosts tournent sur ce serveur. Toujours configtest puis reload.
#
# Le script est idempotent : le relancer ne casse rien.
set -euo pipefail

NEW="${1:-}"
cd "$(dirname "$(readlink -f "$0")")"
HERE="$PWD"

# Le domaine actuellement publie se lit dans mkdocs.yml. Surtout pas une
# constante : apres une premiere bascule, un ancien domaine code en dur ne
# correspond plus a rien et tout ce qui s'appuie dessus devient silencieux.
OLD="$(sed -n 's#^site_url: *https\?://\([^/]*\)/.*#\1#p' mkdocs.yml | head -1)"

die() { echo "ARRET : $*" >&2; exit 1; }
step() { echo; echo "== $* =="; }

[ -n "$NEW" ] || die "usage : sudo $0 <nouveau-domaine>"
[ -n "$OLD" ] || die "site_url introuvable dans mkdocs.yml"
[ "$NEW" != "$OLD" ] || die "le site est deja publie sur $NEW"
[ "$(id -u)" = 0 ] || die "a lancer en root : sudo $0 $NEW"

# L'utilisateur non privilegie qui possede les sources et lance le build. SUDO_USER vaut « root » quand le script est lance
# depuis un shell root : le prendre au mot ferait construire site/ en root, et
# les builds suivants echoueraient en PermissionError. On retombe alors sur le
# proprietaire des sources.
OWNER="${SUDO_USER:-}"
if [ -z "$OWNER" ] || [ "$OWNER" = root ]; then
    OWNER="$(stat -c %U "$HERE")"
fi
id "$OWNER" >/dev/null 2>&1 || die "utilisateur « $OWNER » inconnu"

# ---------------------------------------------------------------- 1. DNS
step "1/6  DNS"
MYIP="$(curl -s -4 --max-time 10 ifconfig.me || true)"
NEWIP="$(getent hosts "$NEW" | awk '{print $1; exit}' || true)"
[ -n "$NEWIP" ] || die "$NEW ne resout pas. Ajouter un enregistrement A vers ${MYIP:-cette machine}."
echo "  $NEW -> $NEWIP"
if [ -n "$MYIP" ] && [ "$NEWIP" != "$MYIP" ]; then
    die "$NEW pointe sur $NEWIP, or cette machine est $MYIP."
fi

# --------------------------------------------------------------- 2. vhost
step "2/6  vhost Apache"
CONF="deploy/$NEW.conf"
if [ ! -f "$CONF" ]; then
    echo "  $CONF absent : je le derive de deploy/$OLD.conf"
    sed "s/$OLD/$NEW/g; s/rubik_error/${NEW%%.*}_error/; s/rubik_access/${NEW%%.*}_access/" \
        "deploy/$OLD.conf" > "$CONF"
    chown "$OWNER" "$CONF"
fi
install -m 644 "$CONF" "/etc/apache2/sites-available/$NEW.conf"
a2ensite "$NEW.conf" >/dev/null
apache2ctl configtest
systemctl reload apache2
echo "  vhost actif"

# ---------------------------------------------------------- 3. certificat
step "3/6  certificat TLS"
if certbot certificates 2>/dev/null | grep -q "Domains:.*\b$NEW\b"; then
    echo "  certificat deja present, rien a faire"
else
    certbot --apache -d "$NEW" --non-interactive --agree-tos --keep-until-expiring
fi
apache2ctl configtest
systemctl reload apache2

curl -sf -o /dev/null --max-time 15 "https://$NEW/" \
    || die "https://$NEW/ ne repond pas encore : verifier le certificat avant de continuer."
echo "  https://$NEW/ repond"

# ------------------------------------------------------ 4. redirection 301
step "4/6  redirection 301 depuis $OLD"
if true; then
    # Vhost de redirection ecrit ici plutot que lu dans deploy/ : un fichier par
    # ancien domaine ne survit pas a la premiere bascule.
    cat > "/etc/apache2/sites-available/$OLD.conf" <<REDIREOF
# Ancien domaine : redirection permanente vers $NEW.
# Le 301 conserve le referencement acquis — Google transfere le classement de
# l'ancienne URL vers la nouvelle, page par page (le chemin est preserve).
<VirtualHost *:80>
    ServerName $OLD
    RedirectPermanent / https://$NEW/
    ErrorLog  \${APACHE_LOG_DIR}/${OLD%%.*}_error.log
    CustomLog \${APACHE_LOG_DIR}/${OLD%%.*}_access.log combined
</VirtualHost>
REDIREOF
    chmod 644 "/etc/apache2/sites-available/$OLD.conf"
    # Le vhost TLS de l'ancien domaine doit rediriger lui aussi : sans ca,
    # https://ancien/ continue de servir le site et Google voit deux copies.
    # On regenere un vhost minimal plutot que de bricoler l'existant, en
    # reprenant les chemins de certificat deja en place.
    SSLCONF="/etc/apache2/sites-available/$OLD-le-ssl.conf"
    if [ -f "$SSLCONF" ] && ! grep -q RedirectPermanent "$SSLCONF"; then
        CERT="$(awk '/SSLCertificateFile/    {print $2; exit}' "$SSLCONF")"
        KEY="$(awk '/SSLCertificateKeyFile/ {print $2; exit}' "$SSLCONF")"
        [ -n "$CERT" ] && [ -n "$KEY" ] || die "certificat de $OLD introuvable dans $SSLCONF"
        cp -a "$SSLCONF" "$SSLCONF.bak.$(date +%Y%m%d-%H%M%S)"
        cat > "$SSLCONF" <<SSLCONFEOF
<IfModule mod_ssl.c>
<VirtualHost *:443>
    ServerName $OLD
    RedirectPermanent / https://$NEW/

    ErrorLog  \${APACHE_LOG_DIR}/${OLD%%.*}_error.log
    CustomLog \${APACHE_LOG_DIR}/${OLD%%.*}_access.log combined

    SSLCertificateFile $CERT
    SSLCertificateKeyFile $KEY
    Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
</IfModule>
SSLCONFEOF
        echo "  ancien vhost TLS sauvegarde puis remplace par la redirection"
    fi
    apache2ctl configtest
    systemctl reload apache2
    echo "  $OLD redirige en 301 vers $NEW"
fi

# --------------------------------------------------- 5. sources et rebuild
step "5/6  sources et reconstruction (utilisateur $OWNER)"
sudo -u "$OWNER" -H bash -lc "cd '$HERE' && python3 tools/switch_domain.py '$NEW'"
sudo -u "$OWNER" -H bash -lc "cd '$HERE' && ./build.sh"

# ------------------------------------------------------------ 6. controle
step "6/6  verification"
fail=0
for path in / /en/ /bis/ /sitemap.xml /robots.txt; do
    code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "https://$NEW$path")"
    printf '  %-16s %s\n' "$path" "$code"
    [ "$code" = 200 ] || fail=1
done
code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "http://$OLD/")"
printf '  %-16s %s (301 attendu)\n' "$OLD" "$code"
[ "$code" = 301 ] || fail=1

canon="$(curl -s --max-time 15 "https://$NEW/" | grep -o 'rel="canonical" href="[^"]*"' | head -1)"
echo "  $canon"
echo "$canon" | grep -q "$NEW" || fail=1

echo
[ "$fail" = 0 ] && echo "OK — le site est servi sur https://$NEW/ et $OLD redirige." \
                || die "des controles ont echoue, voir ci-dessus."
