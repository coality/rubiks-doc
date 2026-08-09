# 6 · Placing the yellow corners

We put each corner **in the right spot**, without caring about its orientation.
A corner can therefore be in its place while showing yellow on the side: that is
correct at this step.

## Recognising a correctly placed corner

A corner is **in the right spot** if its three colours match the three faces it
touches, **in any order**.

Example: the yellow-green-orange corner is correctly placed if it sits at the
intersection of the yellow, green and orange faces. It does not matter whether
the yellow is on top or on the side.

!!! tip "The reliable way to check"
    Take a corner, note its three colours, and look at the three centres around
    it. If the two trios are the same, it is correctly placed.

Now count how many corners are correctly placed. There are necessarily **zero,
one, or four**.

## The algorithm

<div class="fiche" markdown>
![Three-corner cycle](../assets/cubes/coins-placer.svg)
<div class="corps" markdown>
<span class="move">U R U' L' U R' U' L</span>
<p>It cycles <b>three corners</b> among themselves and leaves the fourth alone.
It twists the corners along the way: that is normal, step 7 deals with it.</p>
</div>
</div>

## How to position it

=== "One corner is correct"

    Hold the cube so that this corner is **top right, in front of you**. That is
    the one the algorithm will spare.

    Apply the algorithm. If the four corners are not all correct yet, apply it a
    second time from the same position.

=== "No corner is correct"

    Apply the algorithm from any position. You then get one correct corner. Go
    back to the case above.

=== "All four are correct"

    The step is done. Move on to the [last one](7-corners-oriented.md).

!!! success "Check"
    The four corners are in the right spots. The cube looks **more scrambled
    than before** on top, because the corners are twisted every which way. That
    is the sign everything is fine: only one step is left.
