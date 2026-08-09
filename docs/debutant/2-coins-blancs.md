# 2 · Les coins blancs

<div class="objectif" markdown>
![Première couronne terminée](../assets/cubes/but-couronne1.svg)
<figcaption>L'objectif : toute la couche du bas, plus une bande complète de la
bonne couleur sur chaque face latérale.</figcaption>
</div>

Il reste quatre coins à placer : ceux qui contiennent du blanc. Tu vas les
insérer un par un, toujours de la même façon.

## Le principe

Un coin va **entre trois centres**. Le coin blanc-vert-orange va donc à
l'intersection des faces blanche, verte et orange — il n'y a pas d'autre endroit
possible.

<div class="objectif" markdown>
![coin/centres](../assets/cubes/coin-trois-centres.svg)
<figcaption>Le coin blanc-vert-orange n'a qu'une seule destination : l'intersection des centres blanc, vert et orange.</figcaption>
</div>

## La manœuvre

1. **Trouve un coin blanc** dans la couche du haut.

<div class="objectif" markdown>
![coin en haut](../assets/cubes/coin-en-haut.svg)
<figcaption>Un coin blanc en attente dans la couche du haut. Tourne <code>U</code> pour l'amener juste au-dessus de son trou, puis <code>R' D' R D</code>.</figcaption>
</div>
2. **Tourne `U`** pour l'amener **juste au-dessus du trou où il doit aller**.
   Le coin doit être exactement au-dessus de sa place, un étage plus haut.
3. Tiens le cube pour que ce coin soit **en haut à droite devant toi**.
4. Répète cette séquence jusqu'à ce que le coin tombe en place, correctement
   orienté :

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">R' D' R D</span>
<p>Le coin descend dans la fente, se retourne, remonte, et finit par se poser
dans le bon sens. <b>Ne t'arrête jamais en cours de route.</b></p>
</div>
</div>

Le nombre de répétitions dépend uniquement de **l'endroit où se trouve
l'autocollant blanc** de ce coin. Il est toujours **impair** :

<div class="algs">
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-avant.svg" alt="Blanc devant"><figcaption><b>Blanc devant</b><br><code>1 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-haut.svg" alt="Blanc dessus"><figcaption><b>Blanc dessus</b><br><code>3 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-droite.svg" alt="Blanc à droite"><figcaption><b>Blanc à droite</b><br><code>5 fois</code></figcaption></figure>
</div>

!!! tip "Tu n'as pas besoin de compter"
    Répète simplement jusqu'à ce que le coin soit posé, blanc en bas. Le tableau
    ci-dessus n'est là que pour te rassurer quand ça semble long : cinq
    répétitions, c'est normal, ce n'est pas une erreur.

    En revanche, **2 et 4 ne marchent jamais** ici : un nombre pair ramène le
    coin exactement d'où il vient.

!!! warning "Ne t'arrête pas au milieu"
    Entre deux répétitions, le bas du cube a l'air cassé. C'est normal : la
    séquence sort une pièce et la remet. Si tu t'arrêtes en cours de route, tu
    casses la croix. **Va toujours jusqu'à ce que le coin soit posé.**

## Le coin est coincé en bas mais mal placé

Ça arrive souvent : un coin blanc est déjà dans la couche du bas, mais au mauvais
endroit ou dans le mauvais sens.

Mets-le en bas à droite devant toi, et fais `R' D' R D` **une fois**. Le coin part
dans la couche du haut. Tu peux maintenant le traiter normalement.

!!! success "Vérification"
    La face blanche est entièrement blanche, et les quatre faces latérales ont
    une bande du bas d'une seule couleur. Un tiers du cube est fait.

## Pourquoi cette séquence

`R' D' R D` est un **commutateur** : elle fait quelque chose, fait autre chose,
puis défait le premier geste. Résultat : elle ne dérange qu'un coin et le remet
en place tourné différemment. Tu retrouveras exactement la même séquence à
l'[étape 7](7-coins-orientes.md) — c'est le seul algorithme utilisé deux fois.
