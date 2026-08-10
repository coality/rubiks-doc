# F2L — the first two layers

This is **the** change that saves the most time, and it requires no algorithm to
learn. Take as long as you need on this page.

## The idea

In the beginner method you place a white corner, then, later, the edge that goes
right next to it. So you visit the same spot twice.

F2L places **both together**. The white-green-orange corner and the green-orange
edge form a **pair**: you join them in the top layer, then put the pair away in
one motion.

Four pairs, four slots, and two thirds of the cube is done.

!!! success "The gain, in numbers"
    Beginner method: about 8 moves per corner + 8 per edge, that is **64 moves**
    for the two layers.
    F2L: about **7 moves per pair**, that is **28 moves**. For the same result.

## The only move you need to understand

The whole of F2L rests on one observation: the trio `R U R'` **pulls the pair out
of the slot**, and `R U' R'` **puts it back in**.

<figure class="film">
<img src="/en/assets/cubes/film-trigger-droit.svg" alt="R U R' — the sequence step by step">
<figcaption>The sequence step by step: each frame shows the cube <b>before</b> the turn, and the arrow shows the move to make.</figcaption>
</figure>

<figure class="film">
<img src="/en/assets/cubes/film-trigger-droit-inverse.svg" alt="R U' R' — the sequence step by step">
</figure>

Take a solved cube and do `R U R'`. Look at the front-right slot: the corner and
the edge have come out of it, together, into the top layer. Do `R U' R'` to put
them back.

That is all of F2L. The rest consists of bringing the pair into the right
configuration before putting it away.

## The method, in three questions

Faced with a pair, ask yourself these three questions in order.

### 1. Where is the corner?

- **In the top layer** → perfect, you can work.
- **Stuck in a slot** → pull it out with `R U R'` (or its equivalent on the
  relevant side), then go back to question 1.

### 2. Where is the edge?

- **In the top layer** → perfect.
- **Stuck in a slot** → pull it out, same as for the corner.

### 3. How do I join them?

Both pieces are on top. You have to put them side by side, the right way round,
then put the pair away. This is where all the intuitive work lies:

- **Open the slot** with `R U R'` or `F' U' F` — that makes the room.
- **Bring the other piece** above it with `U`, `U'` or `U2`.
- **Close it up** by undoing the opening move.

!!! tip "The reflex that unblocks 90% of cases"
    If you cannot see what to do: **open the slot** (`R U R'`), look at what
    happens, `U` to reposition, **close it up**. In the vast majority of cases
    the pair forms, or gets much closer to forming.

## The three basic cases

These are the only ones you need to get going. All the others reduce to them in
one or two moves.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/f2l-01.svg" alt="Basic case 1"><figcaption><b>Pair already formed</b><br>Direct insertion</figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/f2l-02.svg" alt="Basic case 2"><figcaption><b>Pieces separated</b><br>Open, align, close</figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/f2l-03.svg" alt="Basic case 3"><figcaption><b>Pair the wrong way round</b><br>Undo then re-form</figcaption></figure>
</div>

## Four pieces of advice that change everything

!!! tip "Work all four slots, not just the right one"
    Many people rotate the cube so as to always work front-right. That is a
    wasted rotation on every pair. Learn to insert **front-left** too, with
    `F' U' F` and `F' U F`, which is its mirror.

<figure class="film">
<img src="/en/assets/cubes/film-trigger-gauche.svg" alt="F' U' F — the sequence step by step">
</figure>

<figure class="film">
<img src="/en/assets/cubes/film-trigger-gauche-inverse.svg" alt="F' U F — the sequence step by step">
</figure>

!!! tip "Choose your pair, don't just take what comes"
    After the cross, look at all four pairs and start with the **easiest** — the
    one whose two pieces are already visible on top. While you insert it, you
    have time to spot the next one.

!!! tip "Slow down to go faster"
    An F2L executed at full speed but followed by three seconds hunting for the
    next pair is **slower** than a calm F2L where you search at the same time as
    you turn. That is lookahead, and it is the real subject.

!!! warning "Do not go and look at the 41 cases straight away"
    The [full list](../advanced/f2l.md) exists, and it is useful — later. F2L
    learned by heart without being understood blocks you for a long time,
    because you will not know what to do with the cases you have not memorised.

    Use it as a dictionary: when one particular case keeps costing you time, go
    and see how it is done properly.
