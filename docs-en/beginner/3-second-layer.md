# 3 · The second layer

<div class="objectif" markdown>
![Two layers finished](../assets/cubes/but-couronne2.svg)
<figcaption>The goal: two thirds of the cube. Only the top layer is still
scrambled.</figcaption>
</div>

Four edges are left to place, the middle ones. **None of them contains yellow** —
that is how you recognise them in the top layer.

<div class="objectif" markdown>
![arete/centres](../assets/cubes/arete-deux-centres.svg)
<figcaption>The green-orange edge goes between the green centre and the orange centre — and nowhere else.</figcaption>
</div>

## Spotting the right edge

Look at the top layer and find an edge **with no yellow**. A green-orange edge,
say.

Turn `U` until **its front colour** matches the centre of that face: if the edge
shows green on the side, bring it onto the green face. You then see an
**upside-down T** in a single colour on the front face.

The edge's other colour (the orange, on top) tells you **which way** it must go
down: towards the orange face.

## The two cases

There are only two, and the second is the exact mirror of the first.

<div class="objectif" markdown>
![3d-arete-insere](../assets/cubes/3d-arete-insere.svg)
<figcaption>The edge leaves the top layer and drops into the front-right slot. That is all the algorithm does.</figcaption>
</div>

<div class="fiche" markdown>
![Insertion on the right](../assets/cubes/couronne2-droite.svg)
<div class="corps" markdown>
<span class="move">U R U' R' U' F' U F</span>
<p><b>The edge must go to the right.</b> The T is in front of you, and the
colour on top matches the centre of the right face.</p>
</div>
</div>

<div class="fiche" markdown>
![Insertion on the left](../assets/cubes/couronne2-gauche.svg)
<div class="corps" markdown>
<span class="move">U' L' U L U F U' F'</span>
<p><b>The edge must go to the left.</b> Exactly the same sequence, mirrored:
every <code>R</code> becomes <code>L</code>, and every direction is reversed.</p>
</div>
</div>

!!! tip "How to learn two algorithms at once"
    Do not learn them separately. Remember the right-hand version, then remember
    the rule: **replace `R` with `L`, `U` with `U'` and `F` with `F'`**. Put the
    two lines side by side and the symmetry jumps out.

## No usable edge on top?

Sometimes all four top edges contain yellow while the second layer is not
finished. That means an edge is **already in the layer, but misplaced or
flipped**.

<div class="objectif" markdown>
![intrus](../assets/cubes/couronne2-intrus.svg)
<figcaption>A <b>foreign</b> edge is stuck in the front-right slot (you can see yellow on the side). It has to be ejected with the right-hand algorithm.</figcaption>
</div>

You have to eject it: put it in the front-right slot and apply the **right-hand**
algorithm as if you were inserting something. The intruder comes up into the top
layer, and you can treat it normally.

!!! success "Check"
    The bottom two thirds of the cube are done: each side face shows two
    complete bands of its colour. Only the yellow layer is left.

From here on, **you never turn the cube over again**: yellow stays on top until
the end.
