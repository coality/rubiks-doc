# Dépannage

## « Mon cube est impossible à résoudre »

Neuf fois sur dix, c'est vrai — et ce n'est pas ta faute.

Un cube démonté puis remonté au hasard a **11 chances sur 12** d'être dans un
état impossible. Aucune méthode ne le résoudra, parce qu'aucune suite de
mouvements ne peut y arriver.

Voici les trois signatures d'un cube trafiqué. Toutes apparaissent **à la toute
fin**, quand tout le reste est résolu.

### Une seule arête retournée

Tout est résolu sauf une arête, à sa place mais retournée.

**C'est impossible sur un cube intact.** Les arêtes se retournent forcément par
deux.

### Un seul coin tourné

Tout est résolu sauf un coin, à sa place mais pivoté d'un tiers de tour.

**Impossible également.** La somme des rotations de coins est toujours un
multiple de trois.

### Deux pièces échangées

Tout est résolu sauf deux arêtes — ou deux coins — qui sont à échanger.

**Impossible aussi** : un échange simple change la parité, qu'aucun mouvement de
3×3 ne peut modifier.

### La solution

Démonte et remonte correctement.

1. Tourne la face du haut de 45°, et fais levier sous une **arête** avec un
   tournevis plat ou l'ongle. Elle sort sans casser.
2. Démonte le reste, pièce par pièce.
3. Remonte-le **directement à l'état résolu**, couleur par couleur. Les coins en
   dernier.

!!! warning "Ne remonte jamais un cube au hasard"
    C'est exactement comme ça qu'on crée le problème. Remonte-le toujours résolu.

!!! tip "Autre cause possible : les autocollants"
    Sur les vieux cubes à autocollants, quelqu'un a pu en décoller un. Vérifie
    que tu as bien **9 autocollants de chaque couleur**, et que les paires de
    couleurs opposées sont cohérentes (blanc↔jaune, vert↔bleu, rouge↔orange).

## « Je casse tout à la dernière étape »

C'est de loin le problème le plus fréquent, et il a une seule cause : **tu as
tourné le cube entier** pendant l'[étape 7](debutant/7-coins-orientes.md).

Pendant l'orientation des coins, tu ne dois faire que des `U` entre les
répétitions de `R' D' R D`. Le cube doit rester rigoureusement immobile dans tes
mains.

Si c'est déjà cassé : reprends le cube depuis l'[étape 1](debutant/1-croix-blanche.md).
Ça ira vite, tu connais le chemin.

## « Le cube a l'air détruit au milieu d'un algorithme »

C'est normal et voulu. La plupart des algorithmes **sortent des pièces déjà
résolues**, les manipulent, puis les remettent.

La règle : **ne t'arrête jamais au milieu d'un algorithme**. Va toujours jusqu'au
dernier mouvement. Si tu as un doute sur l'endroit où tu en es, il vaut mieux
recommencer l'algorithme depuis le début que de continuer au jugé.

## « Je n'arrive pas à trouver la pièce dont on parle »

Deux repères qui débloquent presque tout :

- **Les centres ne bougent jamais** les uns par rapport aux autres. Le centre
  vert est la face verte, définitivement. Cherche toujours par rapport aux
  centres.
- **Une pièce ne change jamais de famille.** Un coin a trois couleurs et reste un
  coin ; une arête en a deux et reste une arête. Si tu cherches une pièce
  vert-orange, c'est une **arête** : ne la cherche pas parmi les coins.

## « J'ai deux couleurs identiques côte à côte »

Impossible sur un cube intact : chaque pièce est unique. Si tu vois deux arêtes
vert-orange, ton cube a des autocollants déplacés, ou c'est une contrefaçon avec
un jeu d'autocollants incorrect.
