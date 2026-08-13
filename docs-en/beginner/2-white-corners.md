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

!!! info "Learned it elsewhere with white on top?"
    That is another convention, just as valid, and it is **the same gesture seen
    from the other side**: with white on top it is written `R' U' R U`, with
    white on the bottom `R' D' R D`. Turning the cube over swaps the two — and
    `R' D' R D` does nothing useful if your white face is up. On this site white
    stays on the bottom from start to finish.

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
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-avant.svg" alt="White in front"><figcaption><b>White in front</b><br><code>once</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-haut.svg" alt="White on top"><figcaption><b>White on top</b><br><code>3 times</code></figcaption></figure>
<figure class="alg"><img src="/en/assets/cubes/3d-coin-blanc-droite.svg" alt="White on the right"><figcaption><b>White on the right</b><br><code>5 times</code></figcaption></figure>
</div>

The arrow shows the real path of the white sticker: it leaves the top layer
and ends up underneath the cube, in its place.

**Then run the sequence that many times:**

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">R' D' R D</span>
<p>The corner drops into the slot, turns, comes back up, and eventually settles
the right way round. <b>Never stop part way through.</b></p>
</div>
</div>

The sequence is shown **step by step** below: every frame is the cube before
the turn, and the arrow is the move to make.

<figure class="film">
<img src="/en/assets/cubes/film-coin-blanc.svg" alt="R' D' R D — the sequence step by step">
<figcaption><code>R' D' R D</code> — the sequence step by step</figcaption>
</figure>

!!! warning "Never stop in the middle"
    During the manoeuvre the bottom of the cube looks wrecked: that is normal, the
    sequence takes a piece out and puts it back.

    One move from the end it is the opposite: everything looks finished, the
    white face is complete. It is in fact a quarter turn out of place, and the
    last move puts it right. Always go to the end.

!!! tip "You don't have to count"
    Just repeat until the corner is seated, white underneath. The diagrams above
    are only there to reassure you when it feels long: five repetitions is
    normal, it is not a mistake.

    What never works here is **2 or 4**: an even number brings the corner back
    to exactly where it started.

## The corner is stuck at the bottom but wrong

This happens often: a white corner is already in the bottom layer, but in the
wrong place or facing the wrong way.

Put it bottom right in front of you and do `R' D' R D` **once**. The corner goes
up into the top layer. You can now treat it normally.

!!! success "Check"
    The white face is entirely white, and the four side faces have a bottom band
    of a single colour. One third of the cube is done.

## Why this sequence works

`R' D' R D` is a **commutator**: it does one thing, does another, then undoes
the first move. The result is that it disturbs only one corner and puts it back
turned differently. You will meet exactly the same sequence again at
[step 7](7-corners-oriented.md) — it is the only algorithm used twice.
