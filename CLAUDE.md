# Contexte : Tutoriel Rubik's Cube (rubiks.coality.net)

Site **statique** MkDocs Material. Aucun service ne tourne : le site est un
dossier de fichiers HTML servi par Apache. Projet indépendant du bot Telegram
et des autres projets — ne pas mélanger.

## État actuel (2026-08-10)

**En ligne et trilingue.** Sources sous `/opt/rubiks-doc`, vhost Apache +
certificat en place, `https://rubiks.coality.net` répond.

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

### Bascule de domaine vers `rubiks.coality.net` (faite le 2026-08-10)

Le site est passé de `rubik.` à `rubiks.` : vhost, certificat, sources et build
sont à jour, les trois langues répondent en HTTPS et `canonical` / `hreflang` /
sitemaps pointent tous sur `rubiks.`.

**L'ancien domaine est abandonné, c'est décidé** (Jérôme, 2026-08-10) : chez
online.net il n'y a plus que `rubiks`, l'enregistrement `rubik` a été supprimé
et ne sera pas recréé. Ne pas reproposer de le rétablir.

Conséquence assumée : les deux vhosts de redirection **301** sont bien en place
mais injoignables, donc l'autorité acquise sur les anciennes URL n'est pas
transférée — Google les verra mourir au lieu de les suivre. Le site était
récent, l'enjeu est faible.

Conséquence à traiter, elle : le certificat `rubik.coality.net` expire le
**2026-11-07**, et certbot commencera à tenter de le renouveler vers le
**8 octobre**. La validation suppose que le domaine résolve : elle échouera à
chaque passage du timer (deux fois par jour) et fera sortir `certbot renew` en
erreur, ce qui masque les vrais problèmes. D'où :

    sudo ./retire-old-domain.sh rubik.coality.net

qui refuse d'agir tant que le domaine résout ou répond, désactive ses deux
vhosts, `configtest` + `reload`, puis supprime la lignée certbot. ⚠️ Les vhosts
**d'abord** : supprimer le certificat en premier laisserait Apache pointer vers
des fichiers absents, `configtest` échouerait et bloquerait le prochain reload,
même sans rapport.

⚠️ **Ordre obligatoire.** Changer le domaine dans les sources avant que le
nouvel hôte réponde ferait pointer `canonical`, `hreflang` et les sitemaps vers
un hôte injoignable — c'est précisément ce qui détruit un référencement.
`tools/switch_domain.py` refuse donc de s'exécuter tant que le HTTPS du nouveau
domaine n'est pas valide.

⚠️ Le domaine de départ est **lu dans `site_url` de `mkdocs.yml`**, jamais codé
en dur — ni dans `switch_domain.py` ni dans `deploy-domain.sh`. Les deux le
codaient en dur (`rubik.coality.net`) : après la première bascule ce nom
n'apparaissait plus nulle part, et `switch_domain.py` remplaçait zéro
occurrence **en annonçant sa réussite**. Il échoue maintenant si la réécriture
ne touche rien. Le vhost de redirection est écrit par le script lui-même, pour
la même raison : un fichier `deploy/<ancien>-redirect.conf` ne survit pas à la
première bascule.

Une seule commande fait tout, en s'arrêtant à la première erreur :

    sudo ./deploy-domain.sh rubiks.coality.net

Elle enchaîne : contrôle du DNS → vhost + `configtest` + `reload` → certbot →
redirection **301** de l'ancien domaine (les deux vhosts, port 80 **et** 443 —
sans le 443, `https://ancien/` continue de servir le site et Google voit deux
copies) → `switch_domain.py` + `build.sh` sous le compte non privilégié →
vérification HTTPS des trois langues, du sitemap et du canonical.

Le script est idempotent et sauvegarde tout vhost qu'il remplace.

Ne **jamais** faire `systemctl restart apache2` : ~18 autres vhosts tournent
dessus. `apache2ctl configtest` puis `systemctl reload apache2`.

### La vérification du contenu (`tools/check_content.py`)

`check_algs.py` vérifie les **données**. `check_content.py` vérifie ce que les
**pages racontent**, dans les trois langues — 2293 contrôles, bloquants au
build :

- tout algorithme cité est analysable, et ceux recopiés dans la page 4LLL
  résolvent bien un cas de la liste (comparaison des **cas** à l'AUF près, pas
  des écritures : les U-perms en tranche M y sont un choix assumé) ;
- les trois langues citent exactement les mêmes séquences (une coquille dans un
  algorithme traduit est détectée) ;
- toute image référencée existe dans la langue concernée (y compris les
  chemins absolus du site français, que la détection laissait passer) ;
- toute séquence citée dans une page de tutoriel a sa bande « pas à pas », et
  **aucun schéma généré ne reste orphelin** — dans les trois langues. C'est ce
  contrôle qui a fait apparaître qu'aucune figure ne montrait le cycle de
  l'étape 6, et que trois schémas étaient encore fabriqués pour personne ;
- sémantique de la notation : `R2` = deux `R`, `r` = `R` + `M'`, `x` = `R M' L'`,
  `M` suit `L`, les centres ne bougent jamais (200 mélanges) ;
- comptages : 6 centres / 12 arêtes / 8 coins, 9 autocollants par couleur,
  57 + 21 = 78, groupes du 4LLL = 3 + 7 + 3 + 4 ;
- affirmations de la méthode débutant : 6 algorithmes en tout, 1/3/5
  répétitions à l'étape 2, 3-cycles purs aux étapes 5 et 6, insertions miroir à
  l'étape 3, chaîne point → équerre → barre → croix à l'étape 4.

Deux résultats qui méritent d'être connus :

- **la croix en 8 mouvements** : parcours **exhaustif** des 190 080 états
  (position + orientation des 4 arêtes blanches) → distance maximale **8**,
  moyenne **5,812**. Les deux chiffres annoncés par `cfop/croix.md` sont exacts.
- **« zéro, un ou quatre coins bien placés »** à l'étape 6 : vrai *parce que*
  les arêtes ont été placées avant, ce qui impose une permutation paire des
  coins et exclut les transpositions (qui donneraient 2). L'ordre des étapes 5
  et 6 n'est donc pas arbitraire.

Ce qui **n'est pas** vérifiable mécaniquement (durées d'apprentissage, conseils
de matériel, plan d'entraînement, doigtés) reste éditorial et doit être relu à
la main. Ne pas présenter le site comme « intégralement certifié » : c'est le
contenu *cubique* qui l'est.

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
| `data/oll.json`, `data/pll.json` (source FR) | `docs*/assets/cubes/*.svg` (schémas + 26 bandes `film-*.svg`, × 3) |
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

### Les bandes « pas à pas » (`filmstrip`)

Chaque séquence citée dans une page de tutoriel est illustrée par **une bande
d'un seul SVG** : un cube par mouvement, montrant l'état **avant** de tourner,
la flèche de ce mouvement et son nom sous la vignette, plus une dernière
vignette pour le résultat.

- L'état de départ est **le cas que la séquence résout** (`case_state(alg)`),
  comme les schémas à plat : la bande et la fiche ne peuvent pas diverger. Une
  assertion de `gen_films()` vérifie que la dernière vignette est bien un cube
  résolu (à une rotation près, pour les algos qui contiennent `x`).
- Les flèches viennent de `move_arcs()`, qui **déduit** l'axe, les tranches
  concernées et le sens de `MOVES`, la table du moteur. Rien n'est ressaisi :
  une flèche ne peut pas contredire le mouvement qu'elle nomme. Un mouvement
  large (`r`) dessine donc deux arcs, une tranche (`M`) un anneau au milieu du
  cube, une rotation (`x`) un anneau autour du tout.
- Les vignettes d'une bande partagent **une boîte englobante commune** : sans
  ça le cube sauterait d'une vignette à l'autre selon la place prise par les
  flèches.
- `test_render3d.py` rejoue, pour chaque mouvement, la rotation que le moteur
  fait subir aux autocollants et vérifie que l'arc tourne dans le même sens —
  c'est ce qui empêche une bande de montrer un mouvement à l'envers.

⚠️ Mesurer un sens de rotation en comparant seulement le premier et le dernier
point de l'arc **ne marche pas** : un demi-tour ou une rotation dépassent 180°
et la différence se replie en changeant de signe. On somme les pas.

Les bandes sont posées dans les pages en HTML brut : `<figure class="film">`
quand la page enseigne l'algorithme, `<details class="film">` replié quand elle
ne fait que le citer (glossaire) ou qu'elle en liste beaucoup (4LLL).

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

⚠️ `pll_arrows()` ne trace une flèche que si l'autocollant du haut **vient** du
haut. L'algorithme de l'étape 6 retourne les coins en les déplaçant : aucune
flèche n'est donc possible sur son schéma à plat, et le cycle ne se montre
qu'en 3D (`3d-coins-cycle`), où `travel()` suit la pièce quelle que soit son
orientation. Les flèches y relient **le dessus au dessus** : une flèche qui
plongerait vers une face latérale ferait croire à un changement d'étage, alors
que l'étape ne parle que de placement.

`build.py` supprime en fin de génération les schémas qu'il ne produit plus
(`prune()`). Sans ça, renommer une figure laisse l'ancien fichier sur le disque,
MkDocs le copie dans `site/` et le publie sans que rien ne le cite.

Les figures d'**objectif** d'étape sont rendues depuis un état **réel** calculé
par le moteur, pas depuis un cube résolu masqué : à la fin de l'étape 5 les
coins ne sont ni placés ni tournés, et un cube résolu grisé le ferait croire.
`but-coins-places` utilise le cas OLL 21, le seul état où tout est permuté et
où seule l'orientation des coins reste — l'assertion vérifie que les trois
couleurs de chaque coin sont bien celles des trois faces qu'il touche, et que
les quatre sont tournés.

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

`deploy/rubiks.coality.net.conf` = vhost Apache (DocumentRoot
`/opt/rubiks-doc/site`, deflate, expires, en-têtes de sécurité).
`install.sh` fait l'installation complète, en root, une seule fois.

### Quand `site/` a été construit en root

MkDocs **nettoie son `site_dir` avant de construire**. Si un build a été lancé
en root, les fichiers appartiennent à root et le build suivant, non privilégié,
supprime ce qu'il peut avant d'échouer en `PermissionError` : il ne reste plus
d'`index.html` et l'accueil répond **403**. C'est arrivé le 2026-08-10.

    sudo ./repair-site.sh

rend `site/` à l'utilisateur des sources, supprime les arbres `site.old*`
laissés par une réparation, reconstruit sous cet utilisateur et vérifie les
trois langues en HTTPS. Idempotent, et il ne touche pas à Apache : le
DocumentRoot ne bouge pas, le contenu est remplacé en place.

Sans privilège, la parade est de remplacer l'arbre entier — `/opt/rubiks-doc`
appartient à l'utilisateur, donc `cp -r site site.new && mv site site.old && mv
site.new site` suffit à retrouver un `site/` accessible en écriture, avec une
interruption d'une fraction de seconde.

`build.sh` refuse désormais de démarrer si un fichier de `site/` n'est pas
accessible en écriture, et `deploy-domain.sh` n'accepte plus `root` comme
utilisateur de build (`SUDO_USER` vaut `root` quand on lance depuis un shell
root — c'est l'origine de l'incident).

⚠️ Prudence réseau : jamais de `systemctl restart apache2` (couperait les ~18
autres sites) — toujours `apache2ctl configtest` puis `systemctl reload`.
