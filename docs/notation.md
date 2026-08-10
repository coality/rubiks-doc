# Le cube et la notation

## Les trois sortes de pièces

Un 3×3 n'a pas 26 pièces interchangeables. Il en a trois familles, et **une pièce
ne change jamais de famille**. C'est l'idée la plus importante de toute la page.

| | Nombre | Autocollants | Particularité |
|---|---|---|---|
| **Centres** | 6 | 1 | Ils ne bougent **jamais** les uns par rapport aux autres |
| **Arêtes** | 12 | 2 | Entre deux centres |
| **Coins** | 8 | 3 | Aux huit sommets |

!!! tip "Les centres définissent les couleurs"
    Tourner une face ne déplace pas son centre. Donc le centre vert **est** la
    face verte, par définition — même sur un cube complètement mélangé. Quand tu
    cherches où va une pièce, regarde les centres, jamais les autres pièces.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/familles-centres.svg" alt="Les 6 centres"><figcaption><b>Les 6 centres</b></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/familles-aretes.svg" alt="Les 12 arêtes"><figcaption><b>Les 12 arêtes</b></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/familles-coins.svg" alt="Les 8 coins"><figcaption><b>Les 8 coins</b></figcaption></figure>
</div>

Une pièce ne change jamais de famille : ces trois jeux ne se mélangent jamais.

    C'est aussi pour ça qu'une arête bleu-orange ne pourra jamais aller entre le
    centre vert et le centre rouge : elle n'a pas les bonnes couleurs.

## Tenir le cube

Une seule règle, valable sur tout le site : **la face qui compte est en haut, et
on ne retourne pas le cube en cours d'algorithme.**

Le cube a trois axes de lecture :

- **U** (*Up*) en haut, **D** (*Down*) en bas
- **F** (*Front*) devant toi, **B** (*Back*) derrière
- **R** (*Right*) à droite, **L** (*Left*) à gauche

<div class="objectif" markdown>
![3d-faces](assets/cubes/3d-faces.svg)
<figcaption>Les trois faces que tu vois : <b>U</b> en haut, <b>F</b> devant toi, <b>R</b> à droite. Ces lettres désignent des positions, pas des couleurs.</figcaption>
</div>

Ces lettres désignent **une position, pas une couleur**. `R` veut dire « la face
qui est à ta droite en ce moment », quelle que soit sa couleur.

## La notation

### Les six mouvements de base

Une lettre seule = **un quart de tour de cette face, dans le sens des aiguilles
d'une montre**, en regardant cette face bien en face.

| Notation | Se lit | Effet |
|---|---|---|
| `R` | *R* | La face droite, un quart de tour horaire |
| `R'` | *R prime* | La face droite, un quart de tour **antihoraire** |
| `R2` | *R deux* | La face droite, un **demi**-tour (le sens n'a pas d'importance) |

Et la même chose pour `U`, `D`, `F`, `B`, `L`.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/3d-move-r.svg" alt="R"><figcaption><b>R</b><br><code>la droite monte devant</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-move-rp.svg" alt="R'"><figcaption><b>R'</b><br><code>le sens inverse</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-move-u.svg" alt="U"><figcaption><b>U</b><br><code>la face du haut</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-move-f.svg" alt="F"><figcaption><b>F</b><br><code>la face avant</code></figcaption></figure>
</div>

!!! warning "Le piège du sens horaire"
    « Horaire » s'entend **en regardant la face concernée**. Pour `D` (la face du
    bas), il faut donc s'imaginer sous le cube en train de le regarder d'en bas.
    Vu de dessus, un `D` a l'air antihoraire. C'est l'erreur numéro un des
    débutants — et la raison pour laquelle les bons algorithmes évitent `D`.

### Les mouvements de tranche

La tranche est la couche **du milieu**, celle qui ne contient aucun coin.

| Notation | Se lit | Effet |
|---|---|---|
| `M` | *M* | Tranche entre `L` et `R`, elle suit le sens de `L` |
| `E` | *E* | Tranche entre `U` et `D`, elle suit le sens de `D` |
| `S` | *S* | Tranche entre `F` et `B`, elle suit le sens de `F` |

`M` est de loin le plus utilisé (il sert dans les meilleurs algorithmes d'arêtes).
Retiens juste : **`M` va dans le même sens que `L`**, c'est-à-dire vers toi par le
dessus.

### Les rotations du cube entier

| Notation | Effet |
|---|---|
| `x` | Tout le cube bascule dans le sens de `R` (l'avant monte) |
| `y` | Tout le cube tourne dans le sens de `U` |
| `z` | Tout le cube pivote dans le sens de `F` |

Une rotation ne résout rien : elle change juste la face que tu as devant toi. Tu
n'en as **aucun besoin** pour la méthode débutant.

### Les mouvements larges

Une lettre **minuscule** = la face **et** la tranche derrière elle, deux couches
d'un coup. `r` = `R` + `M'`. On ne s'en sert qu'à partir de l'OLL complet.

## S'entraîner à lire

Prends ton cube résolu, et exécute lentement :

```
R U R' U'
```

Fais-le **six fois de suite**. Le cube revient exactement à l'état résolu. Si ce
n'est pas le cas, c'est que tu as inversé un sens quelque part — recommence
depuis un cube résolu, plus lentement.

!!! success "Pourquoi ça marche"
    Cette séquence s'appelle le *sexy move*, et c'est la suite de mouvements la
    plus utilisée de tout le cube. Elle a la propriété d'être **d'ordre 6** :
    répétée six fois, elle revient à son point de départ. C'est un excellent test
    pour vérifier que tu lis correctement la notation.

Quand `R U R' U'` × 6 te ramène au cube résolu du premier coup, tu sais lire la
notation. Tu peux attaquer la [méthode débutant](debutant/index.md).


<details class="film">
<summary><code>R U R' U'</code> — la séquence pas à pas</summary>
<img src="/assets/cubes/film-sexy.svg" alt="R U R' U' — la séquence pas à pas">
</details>