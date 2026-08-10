# 6 · Placer les coins jaunes

<div class="objectif" markdown>
![Les quatre coins à leur place, mais encore mal tournés](../assets/cubes/but-coins-places.svg)
<figcaption>L'objectif : chaque coin est à sa place — ses trois couleurs sont celles des
trois faces qu'il touche. Elles ne sont pas encore du bon côté, et c'est
l'étape 7 qui s'en charge.</figcaption>
</div>

On met chaque coin **au bon endroit**, sans se soucier de son orientation. Un
coin peut donc être à sa place tout en montrant du jaune sur le côté : c'est
correct à cette étape.

## Reconnaître un coin bien placé

Un coin est **au bon endroit** si ses trois couleurs correspondent aux trois
faces qu'il touche, **quel que soit l'ordre**.

Exemple : le coin jaune-vert-orange est bien placé s'il se trouve à
l'intersection des faces jaune, verte et orange. Peu importe que le jaune soit
sur le dessus ou sur le côté.

!!! tip "La méthode sûre pour vérifier"
    Prends un coin, note ses trois couleurs, et regarde les trois centres autour
    de lui. Si les deux trios sont les mêmes, il est bien placé.

Cherche maintenant combien de coins sont bien placés. Il y en a forcément **zéro,
un, ou quatre**.

## L'algorithme

<div class="fiche" markdown>
![Permutation de trois coins](../assets/cubes/coins-placer.svg)
<div class="corps" markdown>
<span class="move">U R U' L' U R' U' L</span>
<p>Il fait tourner <b>trois coins</b> entre eux et laisse le quatrième
tranquille. Il retourne les coins au passage : c'est normal, l'étape 7 s'en
occupe.</p>
</div>
</div>

<div class="objectif" markdown>
![Trois coins tournent entre eux ; le quatrième ne bouge pas](../assets/cubes/3d-coins-cycle.svg)
<figcaption>Trois coins tournent entre eux ; le quatrième reste en place. Seul le
<b>placement</b> compte ici — l'orientation est le sujet de l'étape 7.</figcaption>
</div>

<figure class="film">
<img src="/assets/cubes/film-coins-places.svg" alt="U R U' L' U R' U' L — la séquence pas à pas">
<figcaption>La séquence pas à pas : chaque vignette montre l'état <b>avant</b> de tourner, et la flèche le mouvement à faire.</figcaption>
</figure>

## Comment le placer

=== "Un coin est bien placé"

    Tiens le cube pour que ce coin soit **en haut à droite devant toi**. C'est
    lui que l'algorithme va épargner.

    Applique l'algorithme. Si les quatre coins ne sont pas encore bien placés,
    applique-le une seconde fois depuis la même position.

=== "Aucun coin n'est bien placé"

    Applique l'algorithme depuis n'importe quelle position. Tu obtiens alors un
    coin bien placé. Reprends le cas ci-contre.

=== "Les quatre sont bien placés"

    L'étape est finie. Passe à la [dernière](7-coins-orientes.md).

!!! success "Vérification"
    Les quatre coins sont au bon endroit. Le cube a l'air **plus mélangé
    qu'avant** sur le dessus, parce que les coins sont tournés n'importe comment.
    C'est le signe que tout va bien : il ne reste qu'une seule étape.
