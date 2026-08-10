#!/usr/bin/env bash
#
# Remet site/ en etat et le reconstruit, en une commande.
#
#     sudo ./repair-site.sh
#
# A lancer quand un build a ete fait en root : MkDocs nettoie son site_dir avant
# de construire, il supprime alors ce qu'il peut et echoue sur le reste en
# PermissionError — resultat, un site amoute (accueil manquante, donc 403).
#
# Fait, dans l'ordre et en s'arretant a la premiere erreur :
#   1. rend site/ a l'utilisateur qui possede les sources
#   2. supprime les arbres site.old* laisses par une reparation precedente
#   3. reconstruit les trois langues sous cet utilisateur
#   4. verifie le resultat en HTTPS
#
# Prudence : on ne touche pas a Apache. Le DocumentRoot ne change pas, le
# contenu est remplace en place — donc jamais de restart (une vingtaine
# d'autres vhosts tournent sur ce serveur), et meme pas de reload.
#
# Le script est idempotent : le relancer ne casse rien.
set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"
HERE="$PWD"
DOMAIN="${1:-rubiks.coality.net}"

die() { echo "ARRET : $*" >&2; exit 1; }
step() { echo; echo "== $* =="; }

[ "$(id -u)" = 0 ] || die "a lancer en root : sudo $0 ${1:-}"
[ -f "$HERE/build.sh" ] || die "$HERE ne ressemble pas aux sources du site"

# Sous qui reconstruire. SUDO_USER vaut « root » quand le script est lance
# depuis un shell root : le prendre au mot refabriquerait le probleme qu'on
# repare. On retombe alors sur le proprietaire des sources.
OWNER="${SUDO_USER:-}"
if [ -z "$OWNER" ] || [ "$OWNER" = root ]; then
    OWNER="$(stat -c %U "$HERE")"
fi
id "$OWNER" >/dev/null 2>&1 || die "utilisateur « $OWNER » inconnu"
GROUP="$(id -gn "$OWNER")"

# ------------------------------------------------------- 1. proprietaire
step "1/4  proprietaire de site/ ($OWNER:$GROUP)"
if [ -d site ]; then
    n="$(find site ! -user "$OWNER" -printf . | wc -c)"
    if [ "$n" -gt 0 ]; then
        chown -R "$OWNER:$GROUP" site
        echo "  $n fichier(s) rendu(s) a $OWNER"
    else
        echo "  deja correct"
    fi
    # Apache doit pouvoir traverser jusqu'au site
    chmod o+x /opt "$HERE" site 2>/dev/null || true
else
    echo "  site/ absent : il sera cree par le build"
fi

# --------------------------------------------------------- 2. anciens arbres
step "2/4  arbres de secours"
found=0
for old in "$HERE"/site.old*; do
    # le glob non resolu vaut le motif lui-meme
    [ -d "$old" ] || continue
    case "$old" in
        "$HERE"/site.old*) ;;
        *) die "chemin inattendu : $old" ;;      # ceinture et bretelles
    esac
    echo "  suppression de $old ($(du -sh "$old" | cut -f1))"
    rm -rf -- "$old"
    found=1
done
[ "$found" = 1 ] || echo "  rien a supprimer"

# ------------------------------------------------------------ 3. rebuild
step "3/4  reconstruction (utilisateur $OWNER)"
sudo -u "$OWNER" -H bash -lc "cd '$HERE' && ./build.sh" | tail -3

# ---------------------------------------------------------- 4. verification
step "4/4  verification de https://$DOMAIN/"
fail=0
for path in / /en/ /bis/ /404.html /robots.txt /sitemap.xml; do
    code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "https://$DOMAIN$path" || echo 000)"
    printf '  %-16s %s\n' "$path" "$code"
    [ "$code" = 200 ] || fail=1
done

echo
[ "$fail" = 0 ] && echo "OK — https://$DOMAIN/ est servi dans les trois langues." \
                || die "des controles ont echoue, voir ci-dessus."
