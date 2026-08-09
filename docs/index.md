# Commencer ici

Ce site apprend à résoudre un Rubik's Cube 3×3, **en partant de zéro** et en allant
jusqu'aux méthodes de compétition. Tout est sur une seule progression : tu ne
réapprends jamais deux fois la même chose, chaque étape réutilise la précédente.

## Choisis ton point d'entrée

<div class="grid cards" markdown>

- :material-numeric-1-circle: **Je n'ai jamais résolu un cube**

    Va directement à la [méthode débutant](debutant/index.md). Sept étapes,
    **six algorithmes** à retenir en tout. Compte deux heures pour ton premier
    cube résolu, et quelques jours pour le refaire sans regarder.

- :material-numeric-2-circle: **Je sais le résoudre, je veux aller plus vite**

    Lis [Passer au CFOP](cfop/index.md). Tu garderas ta méthode le temps de la
    transition. Le premier vrai gain n'est pas d'apprendre des algorithmes,
    c'est le [F2L](cfop/f2l.md).

- :material-numeric-3-circle: **Je fais déjà du CFOP**

    Les pages de référence : [57 OLL](avance/oll.md), [21 PLL](avance/pll.md),
    [41 cas de F2L](avance/f2l.md). Tout est filtrable et lisible sur téléphone,
    cube en main.

</div>

## Comment lire les schémas

Deux vues reviennent partout dans le site.

<div class="objectif" markdown>
![Cube résolu, patron déplié](assets/cubes/but-resolu.svg)
<figcaption>Le <b>patron déplié</b> : la face du haut est au-dessus, les quatre
faces latérales au milieu (gauche, avant, droite, arrière), la face du bas en
dessous. C'est le cube « ouvert à plat ».</figcaption>
</div>

<div class="objectif" markdown>
![Vue de dessus de la dernière couche](assets/cubes/oll-27.svg)
<figcaption>La <b>vue de dessus</b> : le grand carré est la face du haut, les
petites languettes autour sont les autocollants visibles sur les côtés. C'est la
vue standard pour la dernière couche.</figcaption>
</div>

!!! info "Le gris n'est pas une couleur"
    Une case grise veut dire **« peu importe »**. Elle n'est pas à ignorer par
    paresse : elle signale que cette pièce ne compte pas pour l'étape en cours.

## Les couleurs utilisées ici

Tout le site suppose le schéma de couleurs standard, cube tenu **blanc en bas,
vert devant** :

| Face | Couleur | | Face | Couleur |
|---|---|---|---|---|
| Haut (U) | 🟡 jaune | | Bas (D) | ⬜ blanc |
| Avant (F) | 🟩 vert | | Arrière (B) | 🟦 bleu |
| Droite (R) | 🟧 orange | | Gauche (L) | 🟥 rouge |

Si ton cube a d'autres couleurs, rien ne change : remplace simplement « blanc »
par la couleur que tu commences, et « jaune » par celle d'en face.

!!! question "Pourquoi on commence par le blanc **en bas** ?"
    Beaucoup d'anciens tutoriels font la croix blanche en haut, puis retournent
    le cube. C'est une étape perdue, et surtout ça t'oblige à réapprendre tes
    repères plus tard. Ici on construit **de bas en haut** du début à la fin :
    c'est ce que font toutes les méthodes rapides.

## Une garantie sur le contenu

Les schémas de ce site ne sont pas des images récupérées ailleurs : ils sont
**calculés** à partir des algorithmes eux-mêmes par un simulateur de cube. Un
schéma ne peut donc pas être en désaccord avec l'algorithme qu'il illustre.

Chaque algorithme a été vérifié par ce simulateur : qu'il fait bien ce qui est
annoncé, et qu'il ne casse rien de ce qui était déjà résolu. Les listes de 57
OLL, 21 PLL et 41 F2L ont été vérifiées **complètes et sans doublon**.
