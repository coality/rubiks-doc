#!/usr/bin/env bash
# Installation : deplace les sources sous /opt, publie le vhost Apache, obtient
# le certificat. A lancer une seule fois, en root.
#
# Prudence : on NE touche a rien du reseau, et on ne fait que des `reload`
# apres un `configtest` reussi -- jamais de restart, pour ne pas couper les
# autres sites du serveur.
set -euo pipefail

DOMAIN=rubik.coality.net
SRC=/home/jerome/rubiks-doc
DST=/opt/rubiks-doc
EMAIL=collette.jerome@gmail.com

[ "$(id -u)" -eq 0 ] || { echo "A lancer avec sudo." >&2; exit 1; }

echo "== 1/5  sources sous /opt =="
if [ -d "$SRC" ] && [ ! -d "$DST" ]; then
    mv "$SRC" "$DST"
    chown -R jerome:jerome "$DST"
    echo "   $SRC -> $DST"
else
    echo "   deja en place ($DST)"
fi
# Apache doit pouvoir traverser jusqu'au site
chmod o+x /opt "$DST" "$DST/site"

echo "== 2/5  vhost Apache =="
install -m 644 "$DST/deploy/$DOMAIN.conf" "/etc/apache2/sites-available/$DOMAIN.conf"
a2ensite "$DOMAIN.conf" >/dev/null

echo "== 3/5  verification de la configuration AVANT tout rechargement =="
apache2ctl configtest

echo "== 4/5  rechargement d'Apache (reload, sans coupure) =="
systemctl reload apache2

echo "== 5/5  certificat Let's Encrypt + redirection HTTPS =="
certbot --apache -d "$DOMAIN" --non-interactive --agree-tos -m "$EMAIL" --redirect
apache2ctl configtest
systemctl reload apache2

echo
echo "Termine -> https://$DOMAIN/"
