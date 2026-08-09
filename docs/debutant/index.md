# Méthode débutant — vue d'ensemble

Cette méthode résout le cube **couche par couche**, de bas en haut. Elle demande
**six algorithmes** en tout, dont deux qui sont l'image miroir l'un de l'autre.

## Le plan

| | Étape | Ce que tu obtiens | Algorithmes |
|---|---|---|---|
| 1 | [La croix blanche](1-croix-blanche.md) | Une croix blanche en bas, côtés assortis | aucun |
| 2 | [Les coins blancs](2-coins-blancs.md) | Toute la couche du bas | 1 |
| 3 | [La deuxième couronne](3-deuxieme-couronne.md) | Les deux tiers du cube | 2 (miroirs) |
| 4 | [La croix jaune](4-croix-jaune.md) | Une croix jaune en haut | 1 |
| 5 | [Placer les arêtes](5-aretes-jaunes.md) | Les arêtes jaunes bien placées | 1 |
| 6 | [Placer les coins](6-coins-places.md) | Les coins au bon endroit | 1 |
| 7 | [Orienter les coins](7-coins-orientes.md) | **Cube résolu** | 0 (on réutilise) |

## Trois conseils avant de commencer

!!! tip "Ne cherche pas à comprendre les algorithmes"
    Les étapes 1 à 3 se font **par la logique** : tu vois où va la pièce, tu la
    mets. Les étapes 4 à 7 utilisent des algorithmes : là, tu appliques sans
    chercher pourquoi. La compréhension viendra en les répétant, pas en les
    fixant du regard.

!!! tip "Fais chaque étape jusqu'au bout avant de passer à la suivante"
    Chaque étape suppose que la précédente est **entièrement** finie. Une croix
    blanche « presque bonne » fait rater tout le reste.

!!! danger "Un cube qui semble impossible"
    Si tu arrives à la fin avec **une seule** arête retournée, ou **un seul**
    coin tourné, ce n'est pas une erreur de ta part : ton cube a été démonté et
    remonté n'importe comment. Voir [Dépannage](../depannage.md).

## L'état de départ

Tu tiens le cube avec le **centre blanc en bas** et le **centre jaune en haut**.
Ces deux centres ne bougeront plus jusqu'à la fin.

<div class="objectif" markdown>
![Cube résolu](../assets/cubes/but-resolu.svg)
<figcaption>L'objectif final, en patron déplié.</figcaption>
</div>
