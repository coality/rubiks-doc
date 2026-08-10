# 4 · The yellow cross

<div class="objectif" markdown>
![Yellow cross](../assets/cubes/but-croix-jaune.svg)
<figcaption>The goal: a yellow cross on top. Only the edges count — the corners
can be any colour.</figcaption>
</div>

!!! info "We only look at the edges"
    At this step, **ignore the four corners completely**. Look only at the
    yellow centre and the four edges around it. The corners are dealt with in
    steps 6 and 7.

## A single algorithm

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>It flips edges on the top face. Depending on what you have, you apply it
once, twice or three times — that is the whole of this step.</p>
</div>
</div>

<figure class="film">
<img src="/en/assets/cubes/film-croix-jaune.svg" alt="F R U R' U' F' — the sequence step by step">
<figcaption><code>F R U R' U' F'</code> — the sequence step by step</figcaption>
</figure>

## The three cases

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/eo-point.svg" alt="The dot"><figcaption><b>The dot</b><br>No yellow edge.<br><code>3 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/eo-equerre.svg" alt="The L"><figcaption><b>The L</b><br>Two edges at a right angle.<br><code>2 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/eo-barre.svg" alt="The bar"><figcaption><b>The bar</b><br>Two edges in a line.<br><code>1 time</code></figcaption></figure>
</div>

### How to hold the cube

This is the only delicate point of the step, and it is simple once understood.

=== "The dot"

    No particular orientation. Apply the algorithm: you get the L or the bar.
    Carry on with whichever case you got.

=== "The L"

    Turn `U` to put the L **at the top left**, as in the diagram: the two arms
    point **up** and **left**.

    Apply the algorithm: you get the bar. Apply it once more.

=== "The bar"

    Turn `U` so that the bar is **horizontal**, left to right.

    Apply the algorithm once: the cross appears.

!!! tip "The shortcut"
    Dot → L → bar → cross. Each application moves you one notch along that
    chain. If you get the orientation wrong you move backwards along the chain
    without ever breaking anything else — it is risk-free.

!!! success "Check"
    A clean yellow cross on top. The yellow corners are pointing every which
    way: that is normal and expected.
