# Troubleshooting

## "My cube is impossible to solve"

Nine times out of ten that is true — and it is not your fault.

A cube taken apart and reassembled at random has an **11 in 12** chance of being
in an impossible state. No method will solve it, because no sequence of moves can
get there.

Here are the three signatures of a tampered cube. All of them show up **right at
the end**, when everything else is solved.

### A single flipped edge

Everything is solved except one edge, in its place but flipped.

**That is impossible on an intact cube.** Edges necessarily flip in pairs.

### A single twisted corner

Everything is solved except one corner, in its place but rotated a third of a
turn.

**Equally impossible.** The sum of the corner twists is always a multiple of
three.

### Two pieces swapped

Everything is solved except two edges — or two corners — that need swapping.

**Also impossible**: a single swap changes the parity, which no 3×3 move can
alter.

### The fix

Take it apart and reassemble it properly.

1. Turn the top face 45°, and lever out an **edge** with a flat screwdriver or
   your fingernail. It comes out without breaking.
2. Take the rest apart, piece by piece.
3. Reassemble it **directly in the solved state**, colour by colour. Corners
   last.

!!! warning "Never reassemble a cube at random"
    That is exactly how the problem is created. Always reassemble it solved.

!!! tip "Another possible cause: the stickers"
    On old sticker cubes, somebody may have peeled one off. Check that you have
    **9 stickers of each colour**, and that the opposite-colour pairs are
    consistent (white↔yellow, green↔blue, red↔orange).

## "I break everything on the last step"

This is by far the most frequent problem, and it has a single cause: **you turned
the whole cube** during [step 7](beginner/7-corners-oriented.md).

While orienting the corners you must only do `U` moves between the repetitions of
`R' D' R D`. The cube must stay rigorously still in your hands.

<details class="film">
<summary><code>R' D' R D</code> — the sequence step by step</summary>
<img src="/en/assets/cubes/film-coin-blanc.svg" alt="R' D' R D — the sequence step by step">
</details>

If it is already broken: start the cube again from
[step 1](beginner/1-white-cross.md). It will be quick, you know the way.

## "The cube looks destroyed in the middle of an algorithm"

That is normal and intended. Most algorithms **pull out pieces that were already
solved**, manipulate them, then put them back.

The rule: **never stop in the middle of an algorithm**. Always go to the last
move. If you are unsure where you are, it is better to restart the algorithm from
the beginning than to carry on guessing.

## "I can't find the piece you are talking about"

Two landmarks unblock nearly everything:

- **The centres never move** relative to each other. The green centre is the
  green face, definitively. Always search relative to the centres.
- **A piece never changes family.** A corner has three colours and stays a
  corner; an edge has two and stays an edge. If you are looking for a
  green-orange piece, it is an **edge**: do not look for it among the corners.

## "I have two identical colours next to each other"

Impossible on an intact cube: every piece is unique. If you see two green-orange
edges, your cube has stickers in the wrong place, or it is a counterfeit with an
incorrect sticker set.
