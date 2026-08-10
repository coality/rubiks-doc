#!/usr/bin/env bash
# Regenere schemas + pages, construit les trois sites (fr / en / bis) dans ./site
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

MK="docker run --rm --user $(id -u):$(id -g) -v $PWD:/docs squidfunk/mkdocs-material:latest"

echo "== 1/6  auto-tests du moteur de cube et du rendu 3D =="
python3 tools/test_cube.py | tail -2
python3 tools/test_render3d.py

echo "== 2/6  verification des algorithmes =="
python3 tools/check_algs.py | tail -4

echo "== 3/6  generation des schemas et des pages (fr, en, bis) =="
python3 tools/build.py

echo "== 4/6  verification du contenu des pages (3 langues) =="
python3 tools/check_content.py

echo "== 5/6  construction des trois sites =="
# le francais est a la racine : il DOIT etre construit en premier, car MkDocs
# nettoie son site_dir et effacerait sinon site/en et site/bis.
$MK build --strict -f mkdocs.yml
$MK build --strict -f mkdocs.en.yml
$MK build --strict -f mkdocs.bis.yml

echo "== 6/6  referencement (hreflang, meta, robots.txt, sitemap index) =="
python3 tools/seo.py

echo
echo "OK -> $PWD/site  ($(du -sh site | cut -f1))"
echo "     fr https://rubiks.coality.net/   en /en/   bis /bis/"
