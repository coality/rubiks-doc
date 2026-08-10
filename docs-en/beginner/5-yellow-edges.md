# 5 · Placing the yellow edges

<div class="objectif" markdown>
![The four yellow edges matched to their face](../assets/cubes/but-aretes-jaunes.svg)
<figcaption>The goal: the four yellow edges matched to the centre of their face. The
corners are neither placed nor turned yet — that is normal.</figcaption>
</div>

You have a yellow cross, but its arms are probably not in front of the right
faces. We are going to place them **without touching anything else**.

## Check what you have

Turn `U` slowly and watch the sides of the four cross edges. Look for a position
where **at least two edges** match the centre of their face.

- **Two edges correctly placed** → that is the normal case, carry on below.
- **All four correctly placed** → this step is already done, go to the
  [next one](6-corners-placed.md).

## The algorithm

<div class="fiche" markdown>
![Three-edge cycle](../assets/cubes/pll-ua.svg)
<div class="corps" markdown>
<span class="move">R U' R U R U R U' R' U' R2</span>
<p>It cycles <b>three edges</b> among themselves and leaves the fourth alone.
The corners do not move.</p>
</div>
</div>

<figure class="film">
<img src="/en/assets/cubes/film-aretes-jaunes.svg" alt="R U' R U R U R U' R' U' R2 — the sequence step by step">
<figcaption><code>R U' R U R U R U' R' U' R2</code> — the sequence step by step</figcaption>
</figure>

## How to position it

Find the **two edges that are already correct**, then look at how they sit
relative to each other.

=== "They are next to each other"

    Turn the cube so they are at the **back** and on the **right**. Apply the
    algorithm once.

=== "They are opposite"

    Apply the algorithm from any position. You land on the "next to each other"
    case, handled alongside.

!!! tip "Turn the cube, not the top face"
    At this step you may rotate the whole cube around the vertical axis (yellow
    stays on top) — that breaks nothing. What breaks everything is turning the
    cube over so yellow ends up somewhere else.

!!! success "Check"
    The four top edges match the centres of their faces. You see a small
    **single-colour T** on each of the four side faces. Only the corners are
    left.
