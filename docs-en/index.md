# Start here

This site teaches you to solve a 3×3 Rubik's Cube, **starting from nothing** and
going all the way to competition methods. It is one single progression: you never
learn the same thing twice, and every step reuses the previous one.

## Pick your starting point

<div class="grid cards" markdown>

- :material-numeric-1-circle: **I have never solved a cube**

    Go straight to the [beginner method](beginner/index.md). Seven steps,
    **six algorithms** to remember in total. Expect two hours for your first
    solved cube, and a few days before you can do it without looking.

- :material-numeric-2-circle: **I can solve it, I want to go faster**

    Read [Moving on to CFOP](cfop/index.md). You keep your current method
    during the transition. The first real gain is not learning algorithms,
    it is [F2L](cfop/f2l.md).

- :material-numeric-3-circle: **I already do CFOP**

    The reference pages: [57 OLL](advanced/oll.md), [21 PLL](advanced/pll.md),
    [41 F2L cases](advanced/f2l.md). All of it readable on a phone, cube in hand.

</div>

## How to read the diagrams

Two views come back everywhere on this site.

<div class="objectif" markdown>
![Solved cube, unfolded net](assets/cubes/but-resolu.svg)
<figcaption>The <b>unfolded net</b>: the top face is above, the four side faces
are in the middle (left, front, right, back), the bottom face is below. It is the
cube "opened out flat".</figcaption>
</div>

<div class="objectif" markdown>
![Top view of the last layer](assets/cubes/oll-27.svg)
<figcaption>The <b>top view</b>: the big square is the top face, the small tabs
around it are the stickers visible on the sides. This is the standard view for
the last layer.</figcaption>
</div>

!!! info "Grey is not a colour"
    A grey square means **"it doesn't matter"**. It is not there out of
    laziness: it tells you that this piece does not count for the step you are
    working on.

## The colours used here

The whole site assumes the standard colour scheme, cube held **white on the
bottom, green in front**:

| Face | Colour | | Face | Colour |
|---|---|---|---|---|
| Up (U) | 🟡 yellow | | Down (D) | ⬜ white |
| Front (F) | 🟩 green | | Back (B) | 🟦 blue |
| Right (R) | 🟧 orange | | Left (L) | 🟥 red |

If your cube has other colours, nothing changes: just replace "white" with the
colour you start on, and "yellow" with the one opposite it.

!!! question "Why start with white **on the bottom**?"
    Many old tutorials build the white cross on top, then flip the cube over.
    That is a wasted step, and worse, it forces you to relearn your landmarks
    later. Here we build **from the bottom up** from beginning to end: that is
    what every fast method does.

## A guarantee about the content

The diagrams on this site are not images taken from somewhere else: they are
**computed** from the algorithms themselves by a cube simulator. A diagram
therefore cannot disagree with the algorithm it illustrates.

Every algorithm has been checked by that simulator: that it does what it claims,
and that it breaks nothing that was already solved. The lists of 57 OLL, 21 PLL
and 41 F2L have been verified **complete and free of duplicates**.
