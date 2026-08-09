# 1 · The white cross

<div class="objectif" markdown>
![Finished white cross](../assets/cubes/but-croix.svg)
<figcaption>The goal: a white cross underneath, with each arm matched to the
centre of its face. The rest does not matter at all.</figcaption>
</div>

Look carefully at the diagram: on the side faces there is **a coloured sticker
under each arm**, and it is the same colour as the centre of its face. That is
what counts. A white cross whose sides are not matched is useless.

<div class="objectif" markdown>
![croix ratee](../assets/cubes/croix-mauvaise.svg)
<figcaption>A <b>failed</b> white cross: the arms are white all right, but no side matches its centre. It has to be redone.</figcaption>
</div>

## The daisy method

This is the simplest route, and it avoids turning the cube over entirely.

### Stage A — build the daisy

Hold the cube **yellow on top**. Bring the **four edges that contain white**
around the yellow centre, white facing up. You get a flower: a yellow heart,
four white petals.

There is no algorithm here: you find a white edge and you bring it up.

<div class="objectif" markdown>
![marguerite](../assets/cubes/marguerite.svg)
<figcaption>The daisy: four white edges around the yellow centre, white facing up. The corners are greyed out: they do not count yet.</figcaption>
</div>

- **White edge in the bottom layer?** Turn that face twice (`F2` for example) to
  send it straight up.
- **White edge in the middle layer?** A quarter turn of the right or left face
  brings it up. If that would knock out a petal already in place, turn `U` first
  to move the petal out of harm's way.
- **White edge already on top but white facing sideways?** Leave it, stage B
  fixes it.

!!! tip "The reflex that unblocks everything"
    If a move breaks a petal you already placed, it does not matter: turn `U` a
    quarter, make your move, put `U` back. This idea — *move it out of the way,
    act, put it back* — is the foundation of the entire cube.

### Stage B — bring each petal down

<div class="objectif" markdown>
![3d-petale-descend](../assets/cubes/3d-petale-descend.svg)
<figcaption>The red petal is lined up above the red centre: a half turn of that face drops it exactly into place.</figcaption>
</div>

Take a petal. Look at its **second colour**, the one on the side.

1. Turn `U` until that colour is **directly above the centre of the same
   colour**. The red petal must end up on the face whose centre is red.
2. Turn that face a **half turn**. The edge comes down into place.


Repeat for all four petals. Careful: never bring a petal down without first
lining up its colour — that is the only mistake possible at this step.

!!! success "Check"
    Turn the cube over to look at the white face: you should see a white cross.
    Then look at the four side faces: under each arm, a sticker matching its
    centre. If so, the step is done.

## How long it takes

This step is the only completely free one. At first, take your time. Later it
takes eight moves and a few seconds — see [The efficient cross](../cfop/cross.md).
