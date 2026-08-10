# The cube and the notation

## The three kinds of piece

A 3×3 does not have 26 interchangeable pieces. It has three families, and **a
piece never changes family**. This is the most important idea on the whole page.

| | Count | Stickers | What makes them special |
|---|---|---|---|
| **Centres** | 6 | 1 | They **never** move relative to each other |
| **Edges** | 12 | 2 | Between two centres |
| **Corners** | 8 | 3 | At the eight vertices |

!!! tip "The centres define the colours"
    Turning a face does not move its centre. So the green centre **is** the
    green face, by definition — even on a completely scrambled cube. When you
    are looking for where a piece goes, look at the centres, never at the other
    pieces.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/familles-centres.svg" alt="The 6 centres"><figcaption><b>The 6 centres</b></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/familles-aretes.svg" alt="The 12 edges"><figcaption><b>The 12 edges</b></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/familles-coins.svg" alt="The 8 corners"><figcaption><b>The 8 corners</b></figcaption></figure>
</div>

A piece never changes family: these three sets never mix.

    It is also why a blue-orange edge can never go between the green centre and
    the red centre: it does not have the right colours.

## Holding the cube

One rule, valid across the whole site: **the face that matters is on top, and
you do not turn the cube over in the middle of an algorithm.**

The cube has three reading axes:

- **U** (*Up*) on top, **D** (*Down*) underneath
- **F** (*Front*) facing you, **B** (*Back*) behind
- **R** (*Right*) on the right, **L** (*Left*) on the left

<div class="objectif" markdown>
![3d-faces](assets/cubes/3d-faces.svg)
<figcaption>The three faces you can see: <b>U</b> on top, <b>F</b> in front of you, <b>R</b> on the right. These letters name positions, not colours.</figcaption>
</div>

These letters name **a position, not a colour**. `R` means "the face that is on
your right right now", whatever colour it happens to be.

## The notation

### The six basic moves

A letter on its own = **a quarter turn of that face, clockwise**, looking
straight at that face.

| Notation | Read as | Effect |
|---|---|---|
| `R` | *R* | The right face, a quarter turn clockwise |
| `R'` | *R prime* | The right face, a quarter turn **anticlockwise** |
| `R2` | *R two* | The right face, a **half** turn (direction does not matter) |

And the same for `U`, `D`, `F`, `B`, `L`.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/3d-move-r.svg" alt="R"><figcaption><b>R</b><br><code>the front of R goes up</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-move-rp.svg" alt="R'"><figcaption><b>R'</b><br><code>the reverse</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-move-u.svg" alt="U"><figcaption><b>U</b><br><code>the top face</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-move-f.svg" alt="F"><figcaption><b>F</b><br><code>the front face</code></figcaption></figure>
</div>

!!! warning "The clockwise trap"
    "Clockwise" is understood **looking at the face in question**. For `D` (the
    bottom face) you therefore have to imagine yourself under the cube looking
    up at it. Seen from above, a `D` looks anticlockwise. This is the number one
    beginner mistake — and the reason good algorithms avoid `D`.

### The slice moves

The slice is the **middle** layer, the one that contains no corner.

| Notation | Read as | Effect |
|---|---|---|
| `M` | *M* | Slice between `L` and `R`, it follows the direction of `L` |
| `E` | *E* | Slice between `U` and `D`, it follows the direction of `D` |
| `S` | *S* | Slice between `F` and `B`, it follows the direction of `F` |

`M` is by far the most used (it appears in the best edge algorithms). Just
remember: **`M` goes the same way as `L`**, that is, towards you over the top.

### Whole-cube rotations

| Notation | Effect |
|---|---|
| `x` | The whole cube tips in the direction of `R` (the front goes up) |
| `y` | The whole cube turns in the direction of `U` |
| `z` | The whole cube pivots in the direction of `F` |

A rotation solves nothing: it only changes which face is in front of you. You
need **none of them** for the beginner method.

### Wide moves

A **lowercase** letter = the face **and** the slice behind it, two layers at
once. `r` = `R` + `M'`. You only need them from full OLL onwards.

## Practising your reading

Take your solved cube and slowly execute:

```
R U R' U'
```

Do it **six times in a row**. The cube comes back exactly to the solved state.
If it does not, you reversed a direction somewhere — start again from a solved
cube, more slowly.

!!! success "Why it works"
    This sequence is called the *sexy move*, and it is the most used sequence on
    the whole cube. It has the property of being **of order 6**: repeated six
    times, it returns to its starting point. That makes it an excellent test
    that you are reading the notation correctly.

Once `R U R' U'` × 6 brings you back to a solved cube first try, you can read the
notation. You are ready for the [beginner method](beginner/index.md).


<details class="film">
<summary><code>R U R' U'</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-sexy.svg" alt="R U R' U' — the sequence step by step">
</details>