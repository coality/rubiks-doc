# Tutoriel Rubik's Cube — rubik.coality.net

Tutoriel complet, du premier cube résolu au CFOP, en **trois langues** :
[français](https://rubik.coality.net/) ·
[English](https://rubik.coality.net/en/) ·
[Bisaya](https://rubik.coality.net/bis/).

Site statique (MkDocs Material) servi directement par Apache. Aucun service ne
tourne : le site est un dossier de fichiers HTML.

**La particularité du projet** : les schémas et les algorithmes ne sont pas
recopiés d'ailleurs, ils sont **calculés et vérifiés par un moteur de cube
maison**. Un schéma ne peut pas contredire l'algorithme qu'il illustre, une
flèche ne peut pas pointer dans le mauvais sens, et une liste d'algorithmes est
*prouvée* complète. Le build échoue si ce n'est pas le cas.

Ce principe a déjà payé : le moteur a mis en évidence une erreur du texte de
l'étape 2 (« répéter 2 ou 4 fois » — en réalité 1, 3 ou 5, un nombre pair
ramenant le coin d'où il vient).

## Prérequis

Python 3 (bibliothèque standard uniquement) et Docker, pour le conteneur
éphémère MkDocs Material. Rien à installer d'autre.

## Modifier le contenu

Les pages sont en Markdown, un dossier par langue : `docs/` (fr), `docs-en/`,
`docs-bis/`. Édite, puis :

    ./build.sh

C'est tout — Apache sert `site/` immédiatement, il n'y a rien à recharger.

`build.sh` enchaîne : auto-tests du moteur et du rendu 3D → vérification des
algorithmes → génération des schémas → construction des trois sites →
référencement. Il s'arrête à la première erreur, donc un algorithme faux — ou
une flèche à l'envers — ne peut pas être publié.

## Multilingue

Pas de plugin i18n : un fichier de configuration et un dossier de sources par
langue, trois builds successifs dans le même `site/`.

| Langue | Config | Sources | Sortie | URL |
|---|---|---|---|---|
| fr | `mkdocs.yml` | `docs/` | `site/` | `/` |
| en | `mkdocs.en.yml` | `docs-en/` | `site/en/` | `/en/` |
| bis | `mkdocs.bis.yml` | `docs-bis/` | `site/bis/` | `/bis/` |

⚠️ Le français doit être construit **en premier** : MkDocs nettoie son
`site_dir`, et le build à la racine effacerait sinon `site/en` et `site/bis`.

Les libellés générés (titres de schémas, noms des cas, intros des pages de
référence) vivent dans `data/i18n.json`, `data/names.<lang>.json` et
`data/intros/<lang>/` — pas dans les `.md`.

## Ce qui est généré, ce qui est écrit à la main

| Écrit à la main | Généré par `build.sh` |
|---|---|
| `docs*/**.md` (sauf ci-contre) | `docs/avance/*.md`, `docs-{en,bis}/advanced/*.md` |
| `data/oll.json`, `data/pll.json` | `docs*/assets/cubes/*.svg` (153 schémas × 3) |
| `data/i18n.json`, `data/names.*.json`, `data/intros/` | `data/f2l_raw.json` (recherche exhaustive) |
| `mkdocs*.yml`, `docs/assets/extra.css` | |

Les fichiers générés ne sont pas versionnés : lance `./build.sh` après un clone.

**Ne modifie pas** les pages de référence : elles sont réécrites à chaque build.
Pour changer un algorithme d'OLL ou de PLL, édite `data/oll.json` / `data/pll.json`
— le schéma correspondant sera régénéré à partir du nouvel algorithme, donc les
deux ne peuvent pas diverger.

## Les outils

| Fichier | Rôle |
|---|---|
| `tools/cube.py` | Moteur de cube 3×3, modèle géométrique (position, normale) |
| `tools/test_cube.py` | 30 auto-tests du moteur |
| `tools/render.py` | Rendu SVG : patron déplié + vue de dessus, flèches PLL |
| `tools/render3d.py` | Rendu SVG isométrique : trajets de pièces, sens des mouvements |
| `tools/test_render3d.py` | 108 vérifications du rendu 3D et du sens des flèches |
| `tools/seo.py` | hreflang, meta, robots.txt, sitemap index (après les builds) |
| `tools/check_algs.py` | Valide chaque algo et **prouve** la complétude des listes |
| `tools/fast.py` | Représentation rapide pour la recherche |
| `tools/f2l_search.py` | Recherche exhaustive des 41 algorithmes de F2L |
| `tools/build.py` | Génère les schémas et les pages de référence |

### Comment les algorithmes sont vérifiés

- **Chaque algo** doit ne toucher qu'à la dernière couche (les deux premières
  couronnes doivent être intactes après exécution sur un cube résolu).
- **Les listes sont prouvées complètes** : il existe exactement 57 classes d'OLL
  et 21 de PLL à AUF près. Comme les 57 (resp. 21) entrées donnent 57 (resp. 21)
  signatures distinctes, aucune ne manque et aucune n'est en double.
- **Les 41 F2L** ne sont pas recopiés : ils sont trouvés par recherche en
  profondeur itérative sur `<R,U,F>`, donc chacun est le plus court possible.
- **Les schémas sont calculés depuis les algorithmes**, jamais dessinés à part :
  un schéma ne peut pas contredire l'algo qu'il illustre.
- **Les flèches des vues 3D** viennent du moteur : on étiquette chaque facette
  par son origine, on applique l'algorithme, et on lit où elle est arrivée. Le
  sens de rotation est vérifié face par face par `tools/test_render3d.py`.

## Réinstaller ailleurs

`deploy/rubik.coality.net.conf` est le vhost Apache ; `install.sh` fait
l'installation complète (déplacement sous `/opt`, vhost, certbot).
