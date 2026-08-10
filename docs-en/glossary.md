# Glossary

## Cube terms

**Algorithm** (or *alg*)
: A memorised sequence of moves that produces a precise effect while leaving the
  rest of the cube intact.

**AUF** (*Adjust Upper Face*)
: The little `U` or `U'` you do before or after an algorithm to line it up. It
  does not count as part of the algorithm.

**Centre**
: A piece with **one** sticker. The six centres never move relative to each
  other: they define the colour of each face.

**Commutator**
: A sequence of the form "do A, do B, undo A, undo B". It disturbs only a very
  small part of the cube. `R' D' R D` is one.

<details class="film">
<summary><code>R' D' R D</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-coin-blanc.svg" alt="R' D' R D — the sequence step by step">
</details>

**Corner**
: A piece with **three** stickers, at a vertex of the cube. There are 8.

**Edge**
: A piece with **two** stickers, between two centres. There are 12.

**Headlights**
: Two corners of the same colour on one face, with a different edge between them.
  Used to recognise PLL cases.

**Orientation**
: The **way round** a piece is placed. A piece can be in the right spot and badly
  oriented.

**Pair**
: A corner and the edge that goes right next to it, handled together. The basis
  of F2L.

**Permutation**
: The **place** of each piece, regardless of which way round it is.

**Slot**
: The home of a corner + edge pair in the first two layers. There are four.

## Methods and steps

**CFOP** (or *Fridrich method*)
: The competition method: **C**ross, **F**2L, **O**LL, **P**LL. 78 algorithms in
  total.

**Cross**
: The first-layer cross. First step of CFOP.

**F2L** (*First Two Layers*)
: The first two layers, solved as corner + edge pairs. 41 cases, but learned
  intuitively.

**4LLL** (*4-Look Last Layer*)
: The last layer in four steps instead of two. **16 algorithms** instead of 78.
  The natural bridge between the beginner method and CFOP.

**Lookahead**
: Hunting for the next piece with your eyes while your fingers execute the
  current sequence. The skill that separates the levels.

**OLL** (*Orientation of the Last Layer*)
: Making the whole top face yellow, without caring about the places. 57 cases.

**PLL** (*Permutation of the Last Layer*)
: Putting every piece of the last layer in its place. 21 cases.

## The algorithms that have names

**Named perms** (A, E, F, G, H, J, N, R, T, U, V, Y, Z)
: The 21 PLL cases, named after the shape drawn by the movement arrows.

**Sexy move**
: `R U R' U'`. The most used sequence on the cube. Repeated six times, it returns
  to the starting point.

<details class="film">
<summary><code>R U R' U'</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-sexy.svg" alt="R U R' U' — the sequence step by step">
</details>

**Sune**
: `R U R' U R U2 R'`. Orients three corners. With its mirror the **anti-Sune**
  (`R U2 R' U' R U' R'`), it is the first real OLL algorithm to learn.

<details class="film">
<summary><code>R U R' U R U2 R'</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-sune.svg" alt="R U R' U R U2 R' — the sequence step by step">
</details>

<details class="film">
<summary><code>R U2 R' U' R U' R'</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-antisune.svg" alt="R U2 R' U' R U' R' — the sequence step by step">
</details>

**T-perm**
: `R U R' U' R' F R2 U' R' U' R U R' F'`. The best-known PLL: it swaps two
  corners and two edges.

<details class="film">
<summary><code>R U R' U' R' F R2 U' R' U' R U R' F'</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-tperm.svg" alt="R U R' U' R' F R2 U' R' U' R U R' F' — the sequence step by step">
</details>

## Measurements

**Ao5, Ao12** (*average of 5 / of 12*)
: The average over 5 or 12 solves, **dropping the best and the worst time**. It
  is the official measure in competition, far more reliable than an isolated
  record.

**HTM** (*Half Turn Metric*)
: A way of counting moves: a half turn (`R2`) counts as **one** move.

**Inspection**
: The 15 seconds allowed before the timer starts, to plan the cross.
