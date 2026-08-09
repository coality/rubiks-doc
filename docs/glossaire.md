# Glossaire

## Les termes du cube

**Algorithme** (ou *algo*)
: Une suite de mouvements mémorisée qui produit un effet précis, en laissant le
  reste du cube intact.

**Arête**
: Pièce à **deux** autocollants, entre deux centres. Il y en a 12.

**AUF** (*Adjust Upper Face*)
: Le petit `U` ou `U'` qu'on fait avant ou après un algorithme pour l'aligner.
  Ne compte pas comme faisant partie de l'algorithme.

**Centre**
: Pièce à **un** autocollant. Les six centres ne bougent jamais les uns par
  rapport aux autres : ils définissent la couleur de chaque face.

**Coin**
: Pièce à **trois** autocollants, à un sommet du cube. Il y en a 8.

**Commutateur**
: Séquence de la forme « faire A, faire B, défaire A, défaire B ». Elle ne
  dérange qu'une toute petite partie du cube. `R' D' R D` en est un.

**Fente** (*slot*)
: L'emplacement d'une paire coin + arête dans les deux premières couronnes. Il y
  en a quatre.

**Orientation**
: Le **sens** dans lequel une pièce est posée. Une pièce peut être au bon endroit
  et mal orientée.

**Paire**
: Un coin et l'arête qui va juste à côté, traités ensemble. Base du F2L.

**Permutation**
: La **place** de chaque pièce, indépendamment de son sens.

**Phares** (*headlights*)
: Deux coins de même couleur sur une face, avec une arête différente entre eux.
  Sert à reconnaître les cas de PLL.

## Les méthodes et étapes

**CFOP** (ou *méthode Fridrich*)
: La méthode de compétition : **C**ross, **F**2L, **O**LL, **P**LL. 78
  algorithmes au total.

**Cross**
: La croix de première couche. Première étape du CFOP.

**F2L** (*First Two Layers*)
: Les deux premières couronnes, résolues par paires coin + arête. 41 cas, mais
  s'apprend intuitivement.

**4LLL** (*4-Look Last Layer*)
: La dernière couche en quatre étapes au lieu de deux. **16 algorithmes** au lieu
  de 78. Le pont naturel entre la méthode débutant et le CFOP.

**OLL** (*Orientation of the Last Layer*)
: Rendre toute la face du haut jaune, sans se soucier des places. 57 cas.

**PLL** (*Permutation of the Last Layer*)
: Mettre chaque pièce de la dernière couche à sa place. 21 cas.

**Lecture anticipée** (*lookahead*)
: Chercher la pièce suivante des yeux pendant que les doigts exécutent la
  séquence en cours. La compétence qui sépare les niveaux.

## Les algorithmes qui ont un nom

**Sexy move**
: `R U R' U'`. La séquence la plus utilisée du cube. Répétée six fois, elle
  ramène au point de départ.

**Sune**
: `R U R' U R U2 R'`. Oriente trois coins. Avec son miroir l'**anti-Sune**
  (`R U2 R' U' R U' R'`), c'est le premier vrai algorithme d'OLL à apprendre.

**T-perm**
: `R U R' U' R' F R2 U' R' U' R U R' F'`. Le PLL le plus connu : il échange deux
  coins et deux arêtes.

**Perms nommées** (A, E, F, G, H, J, N, R, T, U, V, Y, Z)
: Les 21 cas de PLL, nommés d'après la forme dessinée par les flèches de
  déplacement.

## Les mesures

**Ao5, Ao12** (*average of 5 / of 12*)
: Moyenne sur 5 ou 12 résolutions, **en retirant le meilleur et le pire temps**.
  C'est la mesure officielle en compétition, bien plus fiable qu'un record isolé.

**HTM** (*Half Turn Metric*)
: Façon de compter les mouvements : un demi-tour (`R2`) compte pour **un** seul
  mouvement.

**Inspection**
: Les 15 secondes accordées avant de lancer le chrono, pour planifier la croix.
