#!/usr/bin/env bash
# Bascule Apache vers le nouveau domaine. A lancer en root, une seule fois.
#
# Prudence : on ne redemarre JAMAIS Apache (cela couperait les autres vhosts).
# On teste la configuration, puis on recharge.
set -euo pipefail
NEW="${1:-rubiks.coality.net}"
OLD="rubik.coality.net"
cd "$(dirname "$(readlink -f "$0")")"

[ "$(id -u)" = 0 ] || { echo "A lancer en root (sudo)."; exit 1; }

echo "== 1/5  le DNS doit deja pointer ici =="
getent hosts "$NEW" || { echo "ARRET : $NEW ne resout pas. Ajouter l'enregistrement A."; exit 1; }

echo "== 2/5  vhost du nouveau domaine =="
install -m 644 "deploy/$NEW.conf" "/etc/apache2/sites-available/$NEW.conf"
a2ensite "$NEW.conf" >/dev/null
apache2ctl configtest
systemctl reload apache2

echo "== 3/5  certificat =="
certbot --apache -d "$NEW" --non-interactive --agree-tos --keep-until-expiring

echo "== 4/5  redirection 301 de l'ancien domaine =="
install -m 644 "deploy/$OLD-redirect.conf" "/etc/apache2/sites-available/$OLD.conf"
apache2ctl configtest
systemctl reload apache2

echo "== 5/5  verification =="
curl -sI "https://$NEW/" | head -1
curl -sI "http://$OLD/" | head -1
echo
echo "Ensuite, cote sources :  python3 tools/switch_domain.py $NEW && ./build.sh"
