# 5 · Placer les arêtes jaunes

Tu as une croix jaune, mais ses branches ne sont probablement pas devant les
bonnes faces. On va les mettre en place **sans toucher au reste**.

## Vérifier ce que tu as

Fais tourner `U` lentement et observe les côtés des quatre arêtes de la croix.
Cherche une position où **au moins deux arêtes** sont assorties au centre de leur
face.

- **Deux arêtes bien placées** → c'est le cas normal, continue ci-dessous.
- **Les quatre sont bien placées** → cette étape est déjà finie, passe à la
  [suivante](6-coins-places.md).

## L'algorithme

<div class="fiche" markdown>
![Permutation de trois arêtes](../assets/cubes/pll-ua.svg)
<div class="corps" markdown>
<span class="move">R U' R U R U R U' R' U' R2</span>
<p>Il fait tourner <b>trois arêtes</b> entre elles et laisse la quatrième
tranquille. Les coins ne bougent pas.</p>
</div>
</div>

## Comment le placer

1. Trouve les **deux arêtes déjà bien placées**.
2. Si elles sont **côte à côte** (adjacentes) : tourne le cube pour les avoir à
   l'**arrière** et à **droite**. Applique l'algorithme une fois.
3. Si elles sont **opposées** (face à face) : applique l'algorithme depuis
   n'importe quelle position. Tu retombes sur le cas « côte à côte ». Recommence
   au point 2.

!!! tip "Tourner le cube, pas la face du haut"
    À cette étape tu peux faire pivoter le cube entier autour de l'axe vertical
    (le jaune reste en haut) — ça ne casse rien. Ce qui casse tout, c'est de
    retourner le cube pour mettre le jaune ailleurs.

!!! success "Vérification"
    Les quatre arêtes du dessus sont assorties aux centres de leur face. Tu vois
    un petit **T de couleur unie** sur chacune des quatre faces latérales. Seuls
    les coins restent à traiter.
