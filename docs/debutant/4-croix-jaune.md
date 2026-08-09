# 4 · La croix jaune

<div class="objectif" markdown>
![Croix jaune](../assets/cubes/but-croix-jaune.svg)
<figcaption>L'objectif : une croix jaune sur le dessus. Seules les arêtes
comptent — les coins peuvent être de n'importe quelle couleur.</figcaption>
</div>

!!! info "On ne regarde que les arêtes"
    À cette étape, **ignore complètement les quatre coins**. Regarde uniquement
    le centre jaune et les quatre arêtes autour. Les coins seront traités aux
    étapes 6 et 7.

## Un seul algorithme

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>Il retourne des arêtes du dessus. Selon ce que tu as, il faut l'appliquer
une, deux ou trois fois — c'est tout le contenu de cette étape.</p>
</div>
</div>

## Les trois cas

<div class="algs">
<figure class="alg"><img src="/assets/cubes/eo-point.svg" alt="Le point"><figcaption><b>Le point</b><br>Aucune arête jaune.<br><code>3 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/eo-equerre.svg" alt="L'équerre"><figcaption><b>L'équerre</b><br>Deux arêtes en angle.<br><code>2 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/eo-barre.svg" alt="La barre"><figcaption><b>La barre</b><br>Deux arêtes alignées.<br><code>1 fois</code></figcaption></figure>
</div>

### Comment tenir le cube

C'est le seul point délicat de l'étape, et il est simple une fois compris.

=== "Le point"

    Aucune orientation particulière. Applique l'algorithme : tu obtiens
    l'équerre ou la barre. Continue avec le cas obtenu.

=== "L'équerre"

    Tourne `U` pour placer l'équerre **en haut à gauche**, comme sur le schéma :
    les deux branches pointent vers le **haut** et vers la **gauche**.

    Applique l'algorithme : tu obtiens la barre. Applique-le encore une fois.

=== "La barre"

    Tourne `U` pour que la barre soit **horizontale**, de gauche à droite.

    Applique l'algorithme une fois : la croix apparaît.

!!! tip "Le raccourci"
    Point → équerre → barre → croix. Chaque application te fait avancer d'un cran
    dans cette chaîne. Si tu te trompes d'orientation, tu reviens en arrière dans
    la chaîne sans jamais rien casser d'autre — c'est sans risque.

!!! success "Vérification"
    Une croix jaune bien nette sur le dessus. Les coins jaunes, eux, sont dans
    tous les sens : c'est normal et attendu.
