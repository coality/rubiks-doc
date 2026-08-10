# F2L — les deux premières couronnes

C'est **le** changement qui fait gagner le plus de temps, et il ne demande
aucun algorithme à apprendre. Prends le temps qu'il faut sur cette page.

## L'idée

En méthode débutant, tu poses un coin blanc, puis, plus tard, l'arête qui va
juste à côté. Tu passes donc deux fois au même endroit.

Le F2L pose **les deux ensemble**. Le coin blanc-vert-orange et l'arête
vert-orange forment une **paire** : tu les assembles dans la couche du haut, puis
tu ranges la paire d'un seul geste.

Quatre paires, quatre fentes, et les deux tiers du cube sont faits.

!!! success "Le gain chiffré"
    Méthode débutant : environ 8 mouvements par coin + 8 par arête, soit **64
    mouvements** pour les deux couronnes.
    F2L : environ **7 mouvements par paire**, soit **28 mouvements**. Pour le
    même résultat.

## Le seul mouvement à comprendre

Tout le F2L repose sur une observation : le trio `R U R'` **sort la paire de la
fente**, et `R U' R'` **l'y range**.

<figure class="film">
<img src="/assets/cubes/film-trigger-droit.svg" alt="R U R' — la séquence pas à pas">
<figcaption>La séquence pas à pas : chaque vignette montre l'état <b>avant</b> de tourner, et la flèche le mouvement à faire.</figcaption>
</figure>

<figure class="film">
<img src="/assets/cubes/film-trigger-droit-inverse.svg" alt="R U' R' — la séquence pas à pas">
</figure>

Prends un cube résolu et fais `R U R'`. Regarde la fente avant-droite : le coin
et l'arête en sont sortis, ensemble, dans la couche du haut. Fais `R U' R'` pour
les remettre.

C'est tout le F2L. Le reste consiste à amener la paire dans la bonne
configuration avant de la ranger.

## La méthode en trois questions

Devant une paire, pose-toi ces trois questions dans l'ordre.

### 1. Où est le coin ?

- **Dans la couche du haut** → parfait, tu peux travailler.
- **Coincé dans une fente** → sors-le avec `R U R'` (ou son équivalent du côté
  concerné), puis reviens à la question 1.

### 2. Où est l'arête ?

- **Dans la couche du haut** → parfait.
- **Coincée dans une fente** → sors-la, comme pour le coin.

### 3. Comment les assembler ?

Les deux pièces sont en haut. Il faut les mettre côte à côte, dans le bon sens,
puis ranger la paire. C'est là qu'est tout le travail intuitif :

- **Ouvre la fente** avec `R U R'` ou `F' U' F` — ça crée la place.
- **Amène l'autre pièce** au-dessus avec `U`, `U'` ou `U2`.
- **Referme** en inversant le mouvement d'ouverture.

!!! tip "Le réflexe qui débloque 90 % des cas"
    Si tu ne vois pas quoi faire : **ouvre la fente** (`R U R'`), regarde ce qui
    se passe, `U` pour repositionner, **referme**. Dans la grande majorité des
    cas, la paire se forme ou se rapproche nettement.

## Les trois cas de base

Ce sont les seuls à connaître pour démarrer. Tous les autres se ramènent à
eux en un ou deux mouvements.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/f2l-01.svg" alt="Cas de base 1"><figcaption><b>Paire déjà formée</b><br>Insertion directe</figcaption></figure>
<figure class="alg"><img src="/assets/cubes/f2l-02.svg" alt="Cas de base 2"><figcaption><b>Pièces séparées</b><br>Ouvrir, aligner, refermer</figcaption></figure>
<figure class="alg"><img src="/assets/cubes/f2l-03.svg" alt="Cas de base 3"><figcaption><b>Paire à l'envers</b><br>Défaire puis reformer</figcaption></figure>
</div>

## Quatre conseils qui changent tout

!!! tip "Travaille les quatre fentes, pas seulement celle de droite"
    Beaucoup tournent le cube pour toujours travailler à l'avant-droite. C'est
    une rotation perdue à chaque paire. Apprends à insérer aussi à
    **l'avant-gauche** avec `F' U' F` et `F' U F`, qui en est le miroir.

<figure class="film">
<img src="/assets/cubes/film-trigger-gauche.svg" alt="F' U' F — la séquence pas à pas">
</figure>

<figure class="film">
<img src="/assets/cubes/film-trigger-gauche-inverse.svg" alt="F' U F — la séquence pas à pas">
</figure>

!!! tip "Choisis ta paire, ne subis pas"
    Après la croix, regarde les quatre paires et commence par la **plus facile**
    — celle dont les deux pièces sont déjà visibles en haut. Pendant que tu
    l'insères, tu as le temps de repérer la suivante.

!!! tip "Ralentis pour aller plus vite"
    Un F2L exécuté à toute vitesse mais suivi de trois secondes à chercher la
    paire suivante est **plus lent** qu'un F2L calme où tu cherches en même temps
    que tu tournes. C'est la lecture anticipée, et c'est le vrai sujet.

!!! warning "Ne va pas voir les 41 cas tout de suite"
    La [liste complète](../avance/f2l.md) existe, et elle est utile — plus tard.
    Un F2L appris par cœur sans être compris te bloque durablement, parce que tu
    ne sauras pas quoi faire des cas que tu n'as pas mémorisés.

    Utilise-la comme un dictionnaire : quand un cas précis te fait perdre du
    temps à répétition, va voir comment on le fait bien.
