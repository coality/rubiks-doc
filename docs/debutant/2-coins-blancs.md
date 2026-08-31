# 2 · Les coins blancs

<div class="objectif" markdown>
![Première couronne terminée](../assets/cubes/but-couronne1.svg)
<figcaption>L'objectif : toute la couche du bas, plus une bande complète de la
bonne couleur sur chaque face latérale.</figcaption>
</div>

Il reste quatre coins à placer : ceux qui contiennent du blanc. Tu vas les
insérer un par un, toujours de la même façon.

## Comment tenir le cube

Le jaune est **en haut**, et la croix blanche que tu viens de faire est **en
bas**. Tu ne retournes pas le cube de toute l'étape.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/3d-tenue-dessus.svg" alt="Ce que tu vois"><figcaption><b>Ce que tu vois</b><br><code>le jaune en haut</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-tenue-dessous.svg" alt="Ce qu'il y a dessous"><figcaption><b>Ce qu'il y a dessous</b><br><code>la croix blanche</code></figcaption></figure>
</div>

Les schémas de cette page qui montrent le cube **par en dessous** se lisent donc
comme la figure de droite : tu regardes ton cube d'en bas, sans le retourner.

!!! info "Tu as appris ailleurs avec le blanc en haut ?"
    C'est une autre convention, tout aussi valable, et c'est **le même geste vu
    de l'autre côté** : avec le blanc en haut il s'écrit `R' U' R U`, avec le
    blanc en bas `R' D' R D`. Retourner le cube échange les deux — et `R' D' R D`
    ne donne rien de bon si tu as le blanc en haut. Sur ce site, le blanc reste
    en bas du début à la fin.

## Le principe

Un coin va **entre trois centres**. Le coin blanc-vert-orange va donc à
l'intersection des faces blanche, verte et orange — il n'y a pas d'autre endroit
possible.

<div class="objectif" markdown>
![coin entre trois centres](../assets/cubes/3d-coin-trois-centres.svg)
<figcaption>Vu <b>par en dessous</b>, cube résolu : le coin blanc-vert-orange
touche exactement les trois centres blanc, vert et orange. C'est sa seule
destination possible — tout le reste est grisé.</figcaption>
</div>

## La manœuvre

Toutes les illustrations de cette section montrent l'état **avant** de tourner :
regarde-les, identifie ton cas, et seulement ensuite exécute.

<div class="objectif" markdown>
![la fente d'arrivée](../assets/cubes/3d-coin-fente.svg)
<figcaption>Le point de départ, toujours vu <b>par en dessous</b> : le coin blanc
attend en haut, et la flèche montre le trou où il doit descendre. Ce qui occupe
ce trou pour l'instant n'a aucune importance — il en sera éjecté.</figcaption>
</div>

1. **Trouve un coin blanc** dans la couche du haut.
2. **Tourne `U`** pour l'amener **juste au-dessus du trou où il doit aller**.
   Le coin doit être exactement au-dessus de sa place, un étage plus haut.
3. Tiens le cube pour que ce coin soit **en haut à droite devant toi**.
4. **Regarde où pointe son autocollant blanc.** C'est lui, et lui seul, qui
   décide du nombre de répétitions — toujours **impair** :

<div class="algs">
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-avant.svg" alt="Blanc devant"><figcaption><b>Blanc devant</b><br><code>1 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-haut.svg" alt="Blanc dessus"><figcaption><b>Blanc dessus</b><br><code>3 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/3d-coin-blanc-droite.svg" alt="Blanc à droite"><figcaption><b>Blanc à droite</b><br><code>5 fois</code></figcaption></figure>
</div>

La flèche montre le trajet réel du blanc : il part de la couche du haut et
finit sous le cube, à sa place.

**Exécute alors la séquence ce nombre de fois :**

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">R' D' R D</span>
<p>Le coin descend dans la fente, se retourne, remonte, et finit par se poser
dans le bon sens. <b>Ne t'arrête jamais en cours de route.</b></p>
</div>
</div>

La séquence est reprise **pas à pas** ci-dessous : chaque vignette montre
l'état avant de tourner, et la flèche le mouvement à faire.

<figure class="film">
<img src="/assets/cubes/film-coin-blanc.svg" alt="R' D' R D — la séquence pas à pas">
<figcaption><code>R' D' R D</code> — le cas le plus simple : le blanc pointe vers <b>l'avant</b>, une seule répétition suffit. Si ton blanc pointe ailleurs, c'est la même séquence à refaire 3 ou 5 fois, et ton cube ne ressemblera à la dernière vignette qu'à la toute fin.</figcaption>
</figure>

!!! warning "Ne t'arrête jamais en cours de route"
    Pendant la manœuvre, le bas du cube a l'air cassé : c'est normal, la séquence
    sort une pièce et la remet.

    À l'**avant-dernier mouvement**, c'est l'inverse : tout a l'air fini, la face
    blanche est complète. Elle est pourtant décalée d'un quart de tour, et c'est
    le dernier mouvement qui la remet en place. Va toujours jusqu'au bout.

!!! tip "Tu n'as pas besoin de compter"
    Répète simplement jusqu'à ce que le coin soit posé, blanc en bas. Les
    schémas ci-dessus ne sont là que pour te rassurer quand ça semble long :
    cinq répétitions, c'est normal, ce n'est pas une erreur.

    En revanche, **2 et 4 ne marchent jamais** ici : un nombre pair ramène le
    coin exactement d'où il vient.

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
