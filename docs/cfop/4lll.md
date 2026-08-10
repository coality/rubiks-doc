# La dernière couche en 4 temps

Le CFOP complet demande 78 algorithmes. Le **4LLL** (*4-Look Last Layer*) fait le
même travail avec **16**, en découpant chaque étape en deux.

C'est le pont que presque tous les cubeurs empruntent, et beaucoup s'y arrêtent
très longtemps : bien exécuté, il permet largement de descendre sous la minute.

| Temps | Ce qu'on fait | Cas |
|---|---|---|
| 1 | Orienter les arêtes → la croix jaune | 3 |
| 2 | Orienter les coins → la face jaune | 7 |
| 3 | Permuter les coins | 3 |
| 4 | Permuter les arêtes | 4 |

Tu connais déjà le temps 1 : c'est l'[étape 4](../debutant/4-croix-jaune.md) de
la méthode débutant, inchangée.

---

## Temps 1 — orienter les arêtes

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>Point → équerre → barre → croix. Voir
<a href="../../debutant/4-croix-jaune/">l'étape 4</a> pour l'orientation du cube
dans chaque cas.</p>
</div>
</div>

<figure class="film">
<img src="/assets/cubes/film-croix-jaune.svg" alt="F R U R' U' F' — la séquence pas à pas">
<figcaption><code>F R U R' U' F'</code> — la séquence pas à pas</figcaption>
</figure>

<div class="algs">
<figure class="alg"><img src="/assets/cubes/eo-point.svg" alt="Le point"><figcaption><b>Le point</b><br><code>3 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/eo-equerre.svg" alt="L'équerre"><figcaption><b>L'équerre</b><br><code>2 fois</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/eo-barre.svg" alt="La barre"><figcaption><b>La barre</b><br><code>1 fois</code></figcaption></figure>
</div>

---

## Temps 2 — orienter les coins

Sept cas. Ce sont exactement les sept OLL où la croix est déjà faite, donc **rien
ne sera à réapprendre** le jour où tu passeras à l'OLL complet.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/oll-27.svg" alt="Sune"><figcaption><b>Sune</b><br><code>R U R' U R U2 R'</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-26.svg" alt="Anti-Sune"><figcaption><b>Anti-Sune</b><br><code>R U2 R' U' R U' R'</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-21.svg" alt="Double Sune"><figcaption><b>Double Sune</b><br><code>R U2 R' U' R U R' U' R U' R'</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-22.svg" alt="Pi"><figcaption><b>Pi</b><br><code>R U2 R2 U' R2 U' R2 U2 R</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-23.svg" alt="Tête"><figcaption><b>Tête</b><br><code>R2 D' R U2 R' D R U2 R</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-24.svg" alt="Chaussette"><figcaption><b>Chaussette</b><br><code>r U R' U' r' F R F'</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/oll-25.svg" alt="Nœud papillon"><figcaption><b>Nœud papillon</b><br><code>F' r U R' U' r' F R</code></figcaption></figure>
</div>

<details class="film">
<summary>Sune · <code>R U R' U R U2 R'</code></summary>
<img src="/assets/cubes/film-sune.svg" alt="R U R' U R U2 R' — la séquence pas à pas">
</details>
<details class="film">
<summary>Anti-Sune · <code>R U2 R' U' R U' R'</code></summary>
<img src="/assets/cubes/film-antisune.svg" alt="R U2 R' U' R U' R' — la séquence pas à pas">
</details>
<details class="film">
<summary>Double Sune · <code>R U2 R' U' R U R' U' R U' R'</code></summary>
<img src="/assets/cubes/film-double-sune.svg" alt="R U2 R' U' R U R' U' R U' R' — la séquence pas à pas">
</details>
<details class="film">
<summary>Pi · <code>R U2 R2 U' R2 U' R2 U2 R</code></summary>
<img src="/assets/cubes/film-pi.svg" alt="R U2 R2 U' R2 U' R2 U2 R — la séquence pas à pas">
</details>
<details class="film">
<summary>Tête · <code>R2 D' R U2 R' D R U2 R</code></summary>
<img src="/assets/cubes/film-tete.svg" alt="R2 D' R U2 R' D R U2 R — la séquence pas à pas">
</details>
<details class="film">
<summary>Chaussette · <code>r U R' U' r' F R F'</code></summary>
<img src="/assets/cubes/film-chaussette.svg" alt="r U R' U' r' F R F' — la séquence pas à pas">
</details>
<details class="film">
<summary>Nœud papillon · <code>F' r U R' U' r' F R</code></summary>
<img src="/assets/cubes/film-noeud-papillon.svg" alt="F' r U R' U' r' F R — la séquence pas à pas">
</details>

!!! tip "Commence par ces deux-là"
    **Sune** et **Anti-Sune** sont miroirs l'un de l'autre et couvrent à eux
    seuls une bonne partie des cas. Les cinq autres peuvent d'ailleurs tous se
    résoudre en appliquant Sune deux fois — plus lent, mais ça dépanne le temps
    de les apprendre.

---

## Temps 3 — permuter les coins

Trois cas. Repère les **paires de couleurs identiques** sur les côtés (les
« phares ») : la face qui en a deux est celle qui a ses coins déjà bien placés.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/pll-aa.svg" alt="A-perm a"><figcaption><b>A-perm a</b><br><code>x R' U R' D2 R U' R' D2 R2</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/pll-ab.svg" alt="A-perm b"><figcaption><b>A-perm b</b><br><code>x R2 D2 R U R' D2 R U' R</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/pll-e.svg" alt="E-perm"><figcaption><b>E-perm</b><br><code>x' R U' R' D R U R' D' R U R' D R U' R' D'</code></figcaption></figure>
</div>

<details class="film">
<summary>A-perm a · <code>x R' U R' D2 R U' R' D2 R2</code></summary>
<img src="/assets/cubes/film-aperm-a.svg" alt="x R' U R' D2 R U' R' D2 R2 — la séquence pas à pas">
</details>
<details class="film">
<summary>A-perm b · <code>x R2 D2 R U R' D2 R U' R</code></summary>
<img src="/assets/cubes/film-aperm-b.svg" alt="x R2 D2 R U R' D2 R U' R — la séquence pas à pas">
</details>
<details class="film">
<summary>E-perm · <code>x' R U' R' D R U R' D' R U R' D R U' R' D'</code></summary>
<img src="/assets/cubes/film-eperm.svg" alt="x' R U' R' D R U R' D' R U R' D R U' R' D' — la séquence pas à pas">
</details>

!!! info "Les A-perms tournent le cube"
    Le `x` du début est une rotation du cube entier : tu bascules le cube vers
    l'arrière avant d'exécuter, et tu finis en le tenant autrement. C'est normal.

---

## Temps 4 — permuter les arêtes

Quatre cas, et les meilleurs algorithmes du cube : courts, rapides, et fondés
sur la tranche `M`.

<div class="algs">
<figure class="alg"><img src="/assets/cubes/pll-ua.svg" alt="U-perm a"><figcaption><b>U-perm a</b><br><code>M2 U M U2 M' U M2</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/pll-ub.svg" alt="U-perm b"><figcaption><b>U-perm b</b><br><code>M2 U' M U2 M' U' M2</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/pll-h.svg" alt="H-perm"><figcaption><b>H-perm</b><br><code>M2 U M2 U2 M2 U M2</code></figcaption></figure>
<figure class="alg"><img src="/assets/cubes/pll-z.svg" alt="Z-perm"><figcaption><b>Z-perm</b><br><code>M' U M2 U M2 U M' U2 M2</code></figcaption></figure>
</div>

<details class="film">
<summary>U-perm a · <code>M2 U M U2 M' U M2</code></summary>
<img src="/assets/cubes/film-uperm-a.svg" alt="M2 U M U2 M' U M2 — la séquence pas à pas">
</details>
<details class="film">
<summary>U-perm b · <code>M2 U' M U2 M' U' M2</code></summary>
<img src="/assets/cubes/film-uperm-b.svg" alt="M2 U' M U2 M' U' M2 — la séquence pas à pas">
</details>
<details class="film">
<summary>H-perm · <code>M2 U M2 U2 M2 U M2</code></summary>
<img src="/assets/cubes/film-hperm.svg" alt="M2 U M2 U2 M2 U M2 — la séquence pas à pas">
</details>
<details class="film">
<summary>Z-perm · <code>M' U M2 U M2 U M' U2 M2</code></summary>
<img src="/assets/cubes/film-zperm.svg" alt="M' U M2 U M2 U M' U2 M2 — la séquence pas à pas">
</details>

!!! tip "Ces quatre-là sont à apprendre en premier"
    Ils sont courts, ils reviennent tout le temps, et ils font partie des 21 PLL
    complets. Aucun effort perdu.

---

## Et ensuite

Quand le 4LLL est fluide, la suite logique est le [PLL complet](../avance/pll.md) :
tu remplaces les temps 3 et 4 par un seul algorithme. Tu en connais déjà 7 sur 21.

L'[OLL complet](../avance/oll.md) vient en dernier : il remplace les temps 1 et 2,
et tu en connais déjà 7 sur 57.
