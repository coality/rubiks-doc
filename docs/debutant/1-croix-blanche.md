# 1 · La croix blanche

<div class="objectif" markdown>
![Croix blanche terminée](../assets/cubes/but-croix.svg)
<figcaption>L'objectif : une croix blanche en bas, et chaque branche assortie au
centre de sa face. Le reste n'a aucune importance.</figcaption>
</div>

Regarde bien le schéma : sur les faces latérales, il y a **un autocollant coloré
sous chaque branche**, et il est de la même couleur que le centre de sa face.
C'est ça qui compte. Une croix blanche dont les côtés ne sont pas assortis ne
sert à rien.

<div class="objectif" markdown>
![croix ratee](../assets/cubes/croix-mauvaise.svg)
<figcaption>Croix blanche <b>ratée</b> : les branches sont bien blanches, mais aucun côté n'est assorti à son centre. Il faut recommencer.</figcaption>
</div>

## La méthode de la marguerite

C'est le chemin le plus simple, et il évite complètement de retourner le cube.

### Étape A — fabriquer la marguerite

Tiens le cube **jaune en haut**. Amène les **quatre arêtes qui contiennent du
blanc** autour du centre jaune, blanc vers le haut. Tu obtiens une fleur : un
cœur jaune, quatre pétales blancs.

Il n'y a pas d'algorithme : tu cherches une arête blanche, tu la fais monter.

<div class="objectif" markdown>
![marguerite](../assets/cubes/marguerite.svg)
<figcaption>La marguerite : quatre arêtes blanches autour du centre jaune, blanc vers le haut. Les coins sont grisés : ils ne comptent pas encore.</figcaption>
</div>

- **Arête blanche dans la couche du bas ?** Tourne cette face deux fois (`F2` par
  exemple) pour la faire remonter tout droit.
- **Arête blanche dans la couche du milieu ?** Un quart de tour de la face de
  droite ou de gauche la fait monter. Si ça déplace un pétale déjà en place,
  tourne `U` avant pour mettre le pétale à l'abri.
- **Arête blanche déjà en haut mais blanc sur le côté ?** Laisse-la, on la
  corrigera à l'étape B.

!!! tip "Le réflexe qui débloque tout"
    Si un mouvement casse un pétale déjà placé, ce n'est pas grave : tourne `U`
    d'un quart pour déplacer les pétales, fais ton mouvement, remets `U`. Cette
    idée — *mettre à l'abri, agir, remettre* — est le fondement de tout le cube.

### Étape B — descendre chaque pétale

<div class="objectif" markdown>
![3d-petale-descend](../assets/cubes/3d-petale-descend.svg)
<figcaption>Le pétale rouge est aligné au-dessus du centre rouge : un demi-tour de cette face le pose exactement à sa place.</figcaption>
</div>

Prends un pétale. Regarde sa **deuxième couleur**, celle qui est sur le côté.

1. Tourne `U` jusqu'à ce que cette couleur soit **juste au-dessus du centre de la
   même couleur**. Le pétale rouge doit se trouver sur la face dont le centre est
   rouge.
2. Tourne cette face d'un **demi-tour**. L'arête descend et se met en place.


Répète pour les quatre pétales. Attention : ne descends jamais un pétale sans
avoir aligné sa couleur — c'est la seule erreur possible à cette étape.

!!! success "Vérification"
    Retourne le cube pour regarder la face blanche : tu dois voir une croix
    blanche. Puis regarde les quatre faces de côté : sous chaque branche, un
    autocollant assorti à son centre. Si oui, l'étape est finie.

## Combien de temps

Cette étape est la seule entièrement libre. Au début, prends ton temps. Plus tard
elle se fait en huit mouvements et quelques secondes — voir
[La croix efficace](../cfop/croix.md).
