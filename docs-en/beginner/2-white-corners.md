# 2 · The white corners

<div class="objectif" markdown>
![Finished first layer](../assets/cubes/but-couronne1.svg)
<figcaption>The goal: the whole bottom layer, plus a complete band of the right
colour on each side face.</figcaption>
</div>

Four corners are left to place: the ones containing white. You are going to
insert them one by one, always the same way.

## How to hold the cube

Yellow is **on top**, and the white cross you have just built is **underneath**.
You do not turn the cube over during this whole step.

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/3d-tenue-dessus.svg" alt="What you see"><figcaption><b>What you see</b><br><code>yellow on top</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-tenue-dessous.svg" alt="What is underneath"><figcaption><b>What is underneath</b><br><code>the white cross</code></figcaption></figure>
</div>

So the diagrams on this page that show the cube **from underneath** read like
the picture on the right: you are looking at your cube from below, without
turning it over.

## The principle

A corner goes **between three centres**. The white-green-orange corner therefore
goes at the intersection of the white, green and orange faces — there is no
other possible spot.

<div class="objectif" markdown>
![corner between three centres](../assets/cubes/3d-coin-trois-centres.svg)
<figcaption>Seen <b>from below</b>, on a solved cube: the white-green-orange
corner touches exactly the white, green and orange centres. That is its only
possible destination — everything else is greyed out.</figcaption>
</div>

## The manoeuvre

Every diagram in this section shows the state **before** you turn anything:
look at them, identify your case, and only then execute.

<div class="objectif" markdown>
![the target slot](../assets/cubes/3d-coin-fente.svg)
<figcaption>The starting point, again <b>from below</b>: the white corner is
waiting on top, and the arrow shows the hole it has to drop into. Whatever is
sitting in that hole right now does not matter — it will be pushed out.</figcaption>
</div>

1. **Find a white corner** in the top layer.
2. **Turn `U`** to bring it **directly above the hole it belongs in**. The corner
   must be exactly above its place, one storey up.
3. Hold the cube so that this corner is **top right, in front of you**.
4. **Look at where its white sticker points.** That, and only that, decides how
   many repetitions you need — always an **odd** number:

<div class="algs">
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-droite.svg" alt="White on the right"><figcaption><b>White on the right</b><br><code>1 time</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-haut.svg" alt="White on top"><figcaption><b>White on top</b><br><code>3 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-avant.svg" alt="White at the front"><figcaption><b>White at the front</b><br><code>5 times</code></figcaption></figure>
</div>

The arrow shows the real path of the white sticker: it leaves the top layer
and ends up underneath the cube, in its place.

**Then run the sequence that many times:**

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">R U R' U'</span>
<p>The corner leaves the slot, turns around, and finally settles in the right way up. The white cross is <b>intact after every repetition</b>: you may pause between two.</p>
</div>
</div>

The sequence is shown **step by step** below: every frame is the cube before
the turn, and the arrow is the move to make.

<figure class="film">
<img src="/en/assets/cubes/film-sexy.svg" alt="R U R' U'">
<figcaption><code>R U R' U'</code> — the simplest case: white points to <b>the right</b>, one repetition is enough. If your white points elsewhere it is the same sequence, repeated 3 or 5 times.</figcaption>
</figure>

!!! warning "Do not stop in the middle of a repetition"
    A complete repetition never breaks the cross: it takes a piece out and puts
    it back. Stopping between two moves does — always finish the four.

    Between repetitions, however, you may stop as long as you like.

!!! tip "You don't have to count"
    Just repeat until the corner is seated, white underneath. The diagrams above
    are only there to reassure you when it feels long: five repetitions is
    normal, it is not a mistake.

    What never works here is **2 or 4**: an even number brings the corner back
    to exactly where it started.

## The corner is stuck at the bottom but wrong

This happens often: a white corner is already in the bottom layer, but in the
wrong place or facing the wrong way.

Put it bottom right in front of you and do `R U R' U'` **once**. The corner goes
up into the top layer. You can now treat it normally.

!!! success "Check"
    The white face is entirely white, and the four side faces have a bottom band
    of a single colour. One third of the cube is done.

## Why this sequence works

`R U R' U'` is a **commutator**: it does something, does something else, then
undoes the first. As a result it only disturbs one corner and puts everything else
back at each repetition. It is the most used sequence on the cube — you will meet
it everywhere under the name **sexy move**.
