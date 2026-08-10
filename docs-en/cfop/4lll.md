# The last layer in 4 looks

Full CFOP needs 78 algorithms. The **4LLL** (*4-Look Last Layer*) does the same
job with **16**, by splitting each step in two.

It is the bridge nearly every cuber crosses, and many stay on it for a long time:
executed well, it is more than enough to get under a minute.

| Look | What you do | Cases |
|---|---|---|
| 1 | Orient the edges → the yellow cross | 3 |
| 2 | Orient the corners → the yellow face | 7 |
| 3 | Permute the corners | 3 |
| 4 | Permute the edges | 4 |

You already know look 1: it is [step 4](../beginner/4-yellow-cross.md) of the
beginner method, unchanged.

---

## Look 1 — orient the edges

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>Dot → L → bar → cross. See
<a href="../../beginner/4-yellow-cross/">step 4</a> for how to hold the cube in
each case.</p>
</div>
</div>

<figure class="film">
<img src="/en/assets/cubes/film-croix-jaune.svg" alt="F R U R' U' F' — the sequence step by step">
<figcaption>The sequence step by step: each frame shows the cube <b>before</b> the turn, and the arrow shows the move to make.</figcaption>
</figure>

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/eo-point.svg" alt="The dot"><figcaption><b>The dot</b><br><code>3 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/eo-equerre.svg" alt="The L"><figcaption><b>The L</b><br><code>2 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/eo-barre.svg" alt="The bar"><figcaption><b>The bar</b><br><code>1 time</code></figcaption></figure>
</div>

---

## Look 2 — orient the corners

Seven cases. They are exactly the seven OLL where the cross is already done, so
**nothing will have to be relearned** the day you move to full OLL.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/oll-27.svg" alt="Sune"><figcaption><b>Sune</b><br><code>R U R' U R U2 R'</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-26.svg" alt="Anti-Sune"><figcaption><b>Anti-Sune</b><br><code>R U2 R' U' R U' R'</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-21.svg" alt="Double Sune"><figcaption><b>Double Sune</b><br><code>R U2 R' U' R U R' U' R U' R'</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-22.svg" alt="Pi"><figcaption><b>Pi</b><br><code>R U2 R2 U' R2 U' R2 U2 R</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-23.svg" alt="Headlights"><figcaption><b>Headlights</b><br><code>R2 D' R U2 R' D R U2 R</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-24.svg" alt="Sock"><figcaption><b>Sock</b><br><code>r U R' U' r' F R F'</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/oll-25.svg" alt="Bowtie"><figcaption><b>Bowtie</b><br><code>F' r U R' U' r' F R</code></figcaption></figure>
</div>

<details class="film">
<summary>Sune · <code>R U R' U R U2 R'</code></summary>
<img src="/en/assets/cubes/film-sune.svg" alt="R U R' U R U2 R' — the sequence step by step">
</details>
<details class="film">
<summary>Anti-Sune · <code>R U2 R' U' R U' R'</code></summary>
<img src="/en/assets/cubes/film-antisune.svg" alt="R U2 R' U' R U' R' — the sequence step by step">
</details>
<details class="film">
<summary>Double Sune · <code>R U2 R' U' R U R' U' R U' R'</code></summary>
<img src="/en/assets/cubes/film-double-sune.svg" alt="R U2 R' U' R U R' U' R U' R' — the sequence step by step">
</details>
<details class="film">
<summary>Pi · <code>R U2 R2 U' R2 U' R2 U2 R</code></summary>
<img src="/en/assets/cubes/film-pi.svg" alt="R U2 R2 U' R2 U' R2 U2 R — the sequence step by step">
</details>
<details class="film">
<summary>Headlights · <code>R2 D' R U2 R' D R U2 R</code></summary>
<img src="/en/assets/cubes/film-tete.svg" alt="R2 D' R U2 R' D R U2 R — the sequence step by step">
</details>
<details class="film">
<summary>Sock · <code>r U R' U' r' F R F'</code></summary>
<img src="/en/assets/cubes/film-chaussette.svg" alt="r U R' U' r' F R F' — the sequence step by step">
</details>
<details class="film">
<summary>Bowtie · <code>F' r U R' U' r' F R</code></summary>
<img src="/en/assets/cubes/film-noeud-papillon.svg" alt="F' r U R' U' r' F R — the sequence step by step">
</details>

!!! tip "Start with these two"
    **Sune** and **Anti-Sune** are mirrors of each other and between them cover a
    good share of the cases. The other five can in fact all be solved by applying
    Sune twice — slower, but it gets you through while you learn them.

---

## Look 3 — permute the corners

Three cases. Spot the **pairs of identical colours** on the sides (the
"headlights"): the face that has a pair is the one whose corners are already
correctly placed.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/pll-aa.svg" alt="A-perm a"><figcaption><b>A-perm a</b><br><code>x R' U R' D2 R U' R' D2 R2</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/pll-ab.svg" alt="A-perm b"><figcaption><b>A-perm b</b><br><code>x R2 D2 R U R' D2 R U' R</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/pll-e.svg" alt="E-perm"><figcaption><b>E-perm</b><br><code>x' R U' R' D R U R' D' R U R' D R U' R' D'</code></figcaption></figure>
</div>

<details class="film">
<summary>A-perm a · <code>x R' U R' D2 R U' R' D2 R2</code></summary>
<img src="/en/assets/cubes/film-aperm-a.svg" alt="x R' U R' D2 R U' R' D2 R2 — the sequence step by step">
</details>
<details class="film">
<summary>A-perm b · <code>x R2 D2 R U R' D2 R U' R</code></summary>
<img src="/en/assets/cubes/film-aperm-b.svg" alt="x R2 D2 R U R' D2 R U' R — the sequence step by step">
</details>
<details class="film">
<summary>E-perm · <code>x' R U' R' D R U R' D' R U R' D R U' R' D'</code></summary>
<img src="/en/assets/cubes/film-eperm.svg" alt="x' R U' R' D R U R' D' R U R' D R U' R' D' — the sequence step by step">
</details>

!!! info "The A-perms rotate the cube"
    The `x` at the start is a whole-cube rotation: you tip the cube backwards
    before executing, and you finish holding it differently. That is normal.

---

## Look 4 — permute the edges

Four cases, and the best algorithms on the cube: short, fast, and built on the
`M` slice.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/pll-ua.svg" alt="U-perm a"><figcaption><b>U-perm a</b><br><code>M2 U M U2 M' U M2</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/pll-ub.svg" alt="U-perm b"><figcaption><b>U-perm b</b><br><code>M2 U' M U2 M' U' M2</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/pll-h.svg" alt="H-perm"><figcaption><b>H-perm</b><br><code>M2 U M2 U2 M2 U M2</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/pll-z.svg" alt="Z-perm"><figcaption><b>Z-perm</b><br><code>M' U M2 U M2 U M' U2 M2</code></figcaption></figure>
</div>

<details class="film">
<summary>U-perm a · <code>M2 U M U2 M' U M2</code></summary>
<img src="/en/assets/cubes/film-uperm-a.svg" alt="M2 U M U2 M' U M2 — the sequence step by step">
</details>
<details class="film">
<summary>U-perm b · <code>M2 U' M U2 M' U' M2</code></summary>
<img src="/en/assets/cubes/film-uperm-b.svg" alt="M2 U' M U2 M' U' M2 — the sequence step by step">
</details>
<details class="film">
<summary>H-perm · <code>M2 U M2 U2 M2 U M2</code></summary>
<img src="/en/assets/cubes/film-hperm.svg" alt="M2 U M2 U2 M2 U M2 — the sequence step by step">
</details>
<details class="film">
<summary>Z-perm · <code>M' U M2 U M2 U M' U2 M2</code></summary>
<img src="/en/assets/cubes/film-zperm.svg" alt="M' U M2 U M2 U M' U2 M2 — the sequence step by step">
</details>

!!! tip "These four are the ones to learn first"
    They are short, they come up all the time, and they are part of the full 21
    PLL. No effort wasted.

---

## And then

Once the 4LLL is fluent, the logical next step is [full PLL](../advanced/pll.md):
you replace looks 3 and 4 with a single algorithm. You already know 7 out of 21.

[Full OLL](../advanced/oll.md) comes last: it replaces looks 1 and 2, and you
already know 7 out of 57.
