# Contexte : Tutoriel Rubik's Cube (rubik.coality.net)

Site **statique** MkDocs Material. Aucun service ne tourne : le site est un
dossier de fichiers HTML servi par Apache. Projet indépendant du bot Telegram
et des autres projets — ne pas mélanger.

## État actuel (2026-08-10)

**En ligne et trilingue.** Sources sous `/opt/rubiks-doc`, vhost Apache +
certificat en place, `https://rubik.coality.net` répond.

- **3 langues**, une par sous-site : `/` français, `/en/` anglais,
  `/bis/` bisaya (cebuano). 20 pages × 3 = 60 pages HTML, 153 schémas × 3
  (dont 11 vues **isométriques** avec flèches de trajet et de mouvement).
- `tools/test_cube.py` → tous les tests passent ;
  `tools/check_algs.py` → 57 OLL + 21 PLL valides, complétude prouvée

### Le multilingue (sans plugin)

Pas de `mkdocs-static-i18n` : **un `mkdocs*.yml` et un dossier `docs*` par
langue**, trois builds successifs dans le même `site/`. Aucun outil de plus,
conformément au choix « ne pas multiplier les outils ».

| Langue | Config | Sources | Sortie | URL |
|---|---|---|---|---|
| fr | `mkdocs.yml` | `docs/` | `site/` | `/` |
| en | `mkdocs.en.yml` | `docs-en/` | `site/en/` | `/en/` |
| bis | `mkdocs.bis.yml` | `docs-bis/` | `site/bis/` | `/bis/` |

⚠️ **Le français doit être construit en premier** : MkDocs nettoie son
`site_dir`, et le build FR (racine `site/`) effacerait sinon `site/en` et
`site/bis`. `build.sh` respecte cet ordre.

- Les slugs d'URL sont **en anglais** pour `/en/` et `/bis/`
  (`/en/beginner/1-white-cross/`), en français pour la racine. La table de
  correspondance vit dans `tools/seo.py` (`PATHS`) — la mettre à jour si une
  page est ajoutée ou renommée.
- Le registre du bisaya est le **cebuano naturel avec les termes techniques en
  anglais** (corner, edge, layer, slot, algorithm) : c'est ainsi qu'on en parle
  réellement. Les noms des 78 cas OLL/PLL restent en anglais (jargon).
- Le thème Material ne connaît pas `ceb` : le site bisaya est buildé en
  `language: en` et `tools/seo.py` remet `<html lang="ceb">`.
- Les **schémas sont régénérés par langue** (`docs*/assets/cubes/`) pour que le
  `<title>` / `aria-label` du SVG soit traduit. Les blocs HTML bruts référencent
  les images en absolu avec le préfixe de langue (`/en/assets/...`) : MkDocs ne
  réécrit pas les `src` dans du HTML brut.

### Référencement

`tools/seo.py` s'exécute **après** les trois builds (étape 5 de `build.sh`) et
post-traite le HTML :

- `<link rel="alternate" hreflang>` croisés fr/en/ceb **au niveau de la page**
  + `x-default` — et **suppression** de ceux générés par `extra.alternate`, qui
  pointent tous vers les pages d'accueil et seraient en conflit ;
- `<meta name="description">` par page, tirée du premier vrai paragraphe
  (sinon MkDocs met la même description partout) ;
- Open Graph + Twitter Card, JSON-LD `WebSite` sur les trois accueils ;
- `robots.txt` et `/sitemap.xml` = **index** des trois sitemaps de langue (le
  sitemap FR est déplacé en `/sitemap-fr.xml` pour libérer le nom canonique).

Le script est idempotent (marqueur `<!--seo-->`) et échoue si une page attendue
manque du site.

## Décisions structurantes (avec Jérôme)

- **WordPress écarté** : une doc, c'est de la mise en page répétée, pas de la
  composition libre.
- **Apache réutilisé** plutôt qu'ajouter Caddy — ne pas multiplier les outils.
  (L'edge du serveur est Apache 2 + certbot, ~18 vhosts.)
- Progression calquée sur celle de JPerm (débutant → 4LLL → CFOP complet) mais
  **rédigée en propre** : recopier les textes de jperm.net serait du plagiat ;
  seuls les algorithmes (des faits) sont repris.

## Pipeline de build

`./build.sh` enchaîne, et **s'arrête à la première erreur** — un algorithme faux
ne peut donc pas être publié :

1. `tools/test_cube.py` — 30 auto-tests du moteur de cube, et
   `tools/test_render3d.py` — 108 verifications du rendu 3D et du **sens des
   fleches** (une fleche a l'envers est un bug silencieux : le schema reste joli)
2. `tools/check_algs.py` — valide chaque algo + prouve la complétude des listes
3. `tools/build.py` — génère les schémas SVG et les pages de référence,
   **pour les trois langues**
4. trois `mkdocs build --strict` (fr, puis en, puis bis)
5. `tools/seo.py` — hreflang, meta, robots.txt, sitemap index

Apache sert `site/` immédiatement après : rien à recharger.

⚠️ Le conteneur MkDocs tourne en `--user $(id -u):$(id -g)` : sans ça il écrit
`site/` en **root** et `seo.py` échoue en `PermissionError`.

## Écrit à la main vs généré

| Écrit à la main | Généré par `build.sh` (NE PAS ÉDITER) |
|---|---|
| `docs/*.md`, `docs-en/*.md`, `docs-bis/*.md` (sauf ci-contre) | `docs/avance/{oll,pll,f2l}.md` et `docs-{en,bis}/advanced/*.md` |
| `data/oll.json`, `data/pll.json` (source FR) | `docs*/assets/cubes/*.svg` (142 schémas × 3) |
| `data/i18n.json`, `data/names.{en,bis}.json`, `data/intros/<lang>/*.md` | `data/f2l_raw.json` (recherche exhaustive) |
| `mkdocs*.yml`, `docs/assets/extra.css` (copiée vers les autres langues) | |

**Traduire un élément généré** : les libellés de groupes, titres de schémas et
intros ne sont pas dans les `.md` — ils sont dans `data/i18n.json`,
`data/names.<lang>.json` et `data/intros/<lang>/`. `build.py` vérifie qu'aucun
libellé ne manque dans une langue.

Pour changer un algo d'OLL/PLL : éditer `data/oll.json` / `data/pll.json`. Le
schéma est recalculé **depuis l'algorithme**, donc les deux ne peuvent pas
diverger.

## Les outils (`tools/`)

| Fichier | Rôle |
|---|---|
| `cube.py` | Moteur de cube 3×3, modèle géométrique (position, normale) |
| `test_cube.py` | 30 auto-tests du moteur |
| `render.py` | Rendu SVG : patron déplié + vue de dessus, flèches PLL |
| `check_algs.py` | Valide chaque algo et prouve la complétude des listes |
| `fast.py` | Représentation rapide pour la recherche |
| `f2l_search.py` | Recherche exhaustive des 41 algorithmes de F2L |
| `render3d.py` | Rendu **isométrique** SVG : trajets de pièces, sens des mouvements |
| `test_render3d.py` | Vérifie que les flèches disent ce que fait le moteur |
| `build.py` | Génère les schémas et les pages de référence |

### Les schémas 3D (`render3d.py`)

Vue isométrique en SVG pur, sans dépendance ni ressource externe, complémentaire
du patron déplié. Elle sert à montrer **d'où part une pièce et où elle arrive**.

- Le moteur repère chaque autocollant par `(position, normale)` dans
  `{-1,0,1}³` : la géométrie 3D est donc directement disponible.
- `travel(alg, facettes)` applique l'algorithme à un cube dont chaque facette
  porte son origine, et renvoie les couples départ → arrivée. **Une flèche de
  trajet ne peut donc pas contredire l'algorithme annoncé.**
- `turn_points(face, clockwise)` trace l'arc d'un mouvement. Convention vérifiée
  par les tests : avec la base directe `(u, v, n)`, un mouvement **sans prime**
  parcourt θ **décroissant** (horaire vu de l'extérieur de la face). L'arc est
  centré sur la direction de la face qui fait face à la caméra, sinon la flèche
  passe derrière le cube.
- ⚠️ Piège corrigé : les quads doivent être **projetés avant** la mise à
  l'échelle. Sans ça les faces U et R sortent aplaties (aire nulle) et seule la
  face F s'affiche. `test_projection_is_not_degenerate` verrouille ce cas.
- La face `D` n'est pas visible depuis la caméra : pas de figure 3D pour `D`.

### Erreur de contenu trouvée par le moteur (2026-08-10)

L'étape 2 disait « répéter `R' D' R D` **2 ou 4 fois** ». C'est **faux**, et le
moteur le prouve : cette séquence échange URF ↔ DRF, donc un nombre **pair** de
répétitions ramène le coin exactement d'où il vient. Quand le coin blanc attend
en haut, il faut **1, 3 ou 5** répétitions, selon l'endroit où pointe le blanc :

| Blanc vers… | Répétitions |
|---|---|
| l'avant (F) | 1 |
| le haut (U) | 3 |
| la droite (R) | 5 |

Corrigé dans les trois langues, illustré par trois schémas 3D, et **verrouillé
par des assertions** dans `gen_3d()` : le build vérifie que `k` répétitions
terminent la première couronne et que `k±1` ne la terminent pas.

(L'étape 7 dit aussi « 2 ou 4 fois » : là c'est **correct**, le coin est déjà à
sa place et la séquence ne fait que le tourner.)

`build.py` produit aussi les **schémas pédagogiques** de la méthode débutant
(`gen_teaching`) : les trois familles de pièces, la marguerite, la croix mal
assortie, coin/arête vs centres, l'arête intruse en 2e couronne, et le cube
« qui a l'air détruit » à l'étape 7. Chaque état est calculé par le moteur puis
**vérifié par une assertion** — une figure fausse fait échouer le build.

Règles de vérification :
- chaque algo ne doit toucher **que** la dernière couche (les deux premières
  couronnes intactes après exécution sur un cube résolu) ;
- listes **prouvées complètes** : 57 classes d'OLL et 21 de PLL à AUF près, et
  les entrées donnent autant de signatures distinctes → rien ne manque, rien
  n'est en double ;
- les 41 F2L sont **trouvés** par recherche en profondeur itérative sur
  `<R,U,F>` (donc les plus courts), pas recopiés.

## Déploiement

`deploy/rubik.coality.net.conf` = vhost Apache (DocumentRoot
`/opt/rubiks-doc/site`, deflate, expires, en-têtes de sécurité).
`install.sh` fait l'installation complète, en root, une seule fois.

⚠️ Prudence réseau : jamais de `systemctl restart apache2` (couperait les ~18
autres sites) — toujours `apache2ctl configtest` puis `systemctl reload`.
