# 3 · La deuxième couronne

<div class="objectif" markdown>
![Deux couronnes terminées](../assets/cubes/but-couronne2.svg)
<figcaption>L'objectif : les deux tiers du cube. Seule la couche du haut reste
mélangée.</figcaption>
</div>

Il reste quatre arêtes à placer, celles du milieu. **Aucune ne contient de
jaune** — c'est ainsi que tu les reconnais dans la couche du haut.

<div class="objectif" markdown>
![arete/centres](../assets/cubes/arete-deux-centres.svg)
<figcaption>L'arête vert-orange va entre le centre vert et le centre orange — et nulle part ailleurs.</figcaption>
</div>

## Repérer la bonne arête

Regarde la couche du haut et cherche une arête **sans jaune**. Par exemple une
arête vert-orange.

Tourne `U` jusqu'à ce que **sa couleur de face** coïncide avec le centre de cette
face : si l'arête montre du vert sur le côté, amène-la sur la face verte. Tu vois
alors un **T renversé** de couleur unie sur la face avant.

L'autre couleur de l'arête (l'orange, sur le dessus) t'indique **de quel côté**
elle doit descendre : vers la face orange.

## Les deux cas

Il n'y en a que deux, et le second est le miroir exact du premier.

<div class="objectif" markdown>
![3d-arete-insere](../assets/cubes/3d-arete-insere.svg)
<figcaption>L'arête quitte la couche du haut et descend dans la fente avant-droite. C'est tout ce que fait l'algorithme.</figcaption>
</div>

<div class="fiche" markdown>
![Insertion à droite](../assets/cubes/couronne2-droite.svg)
<div class="corps" markdown>
<span class="move">U R U' R' U' F' U F</span>
<p><b>L'arête doit partir à droite.</b> Le T est devant toi, et la couleur du
dessus correspond au centre de la face de droite.</p>
</div>
</div>

<div class="fiche" markdown>
![Insertion à gauche](../assets/cubes/couronne2-gauche.svg)
<div class="corps" markdown>
<span class="move">U' L' U L U F U' F'</span>
<p><b>L'arête doit partir à gauche.</b> Exactement la même séquence, en miroir :
chaque <code>R</code> devient <code>L</code>, et chaque sens s'inverse.</p>
</div>
</div>

!!! tip "Comment retenir deux algorithmes d'un coup"
    Ne les apprends pas séparément. Retiens la version de droite, puis retiens la
    règle : **on remplace `R` par `L`, `U` par `U'` et `F` par `F'`**. Regarde les
    deux lignes côte à côte, la symétrie saute aux yeux.

## Aucune arête utilisable en haut ?

Il arrive que les quatre arêtes du haut contiennent toutes du jaune, alors que la
deuxième couronne n'est pas finie. C'est qu'une arête est **déjà dans la couronne,
mais mal placée ou à l'envers**.

<div class="objectif" markdown>
![intrus](../assets/cubes/couronne2-intrus.svg)
<figcaption>Une arête <b>étrangère</b> est coincée dans la fente avant-droite (on voit du jaune sur le côté). Il faut l'éjecter avec l'algorithme de droite.</figcaption>
</div>

Il faut l'éjecter : mets-la à la place « avant-droite », et applique l'algorithme
**de droite** comme si tu insérais quelque chose. L'intrus remonte dans la couche
du haut, et tu peux le traiter normalement.

!!! success "Vérification"
    Les deux tiers du bas du cube sont finis : chaque face latérale montre deux
    bandes complètes de sa couleur. Il ne reste que la couche jaune.

À partir d'ici, **on ne retourne plus jamais le cube** : le jaune reste en haut
jusqu'à la fin.
