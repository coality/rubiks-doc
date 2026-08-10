# 5 · Pagbutang sa dalag nga edge

<div class="objectif" markdown>
![Ang upat ka dalag nga edge nga pareho sa ilang face](../assets/cubes/but-aretes-jaunes.svg)
<figcaption>Ang tumong: ang upat ka dalag nga edge pareho na sa centre sa ilang face. Ang
mga corner wala pa mabutang ug wala pa maliso — normal ra kana.</figcaption>
</div>

Naa na kay dalag nga cross, apan lagmit ang iyang mga bukton wala pa sa husto nga
face. Ibutang nato sila **nga walay laing matandog**.

## Susiha unsay imong naa

Tuyoka ang `U` hinay-hinay ug tan-awa ang kilid sa upat ka edge sa cross. Pangitaa
ang posisyon diin **labing menos duha ka edge** ang motakdo sa center sa ilang
face.

- **Duha ka edge ang husto** → mao kini ang normal nga case, padayon sa ubos.
- **Ang upat husto tanan** → human na kini nga lakang, adto na sa
  [sunod](6-corners-placed.md).

## Ang algorithm

<div class="fiche" markdown>
![Pag-cycle sa tulo ka edge](../assets/cubes/pll-ua.svg)
<div class="corps" markdown>
<span class="move">R U' R U R U R U' R' U' R2</span>
<p>Iyang i-cycle ang <b>tulo ka edge</b> sa ilang kaugalingon ug pasagdan ang
ikaupat. Ang corner dili molihok.</p>
</div>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-aretes-jaunes.svg" alt="R U' R U R U R U' R' U' R2 — ang sequence, matag lihok">
<figcaption><code>R U' R U R U R U' R' U' R2</code> — ang sequence, matag lihok</figcaption>
</figure>

## Unsaon pagposisyon

1. Pangitaa ang **duha ka edge nga husto na**.
2. Kung **magtapad** sila: tuyoka ang cube aron sila maanaa sa **likod** ug sa
   **tuo**. Buhata ang algorithm kausa.
3. Kung **magtapad ang ilang atubangan** (nag-atbang): buhata ang algorithm gikan
   sa bisan unsang posisyon. Mahulog ka sa case nga "magtapad". Balik sa numero 2.

!!! tip "Tuyoka ang cube, dili ang ibabaw nga face"
    Niini nga lakang mahimo nimong tuyokon ang tibuok cube palibot sa tindog nga
    axis (ang dalag magpabilin sa ibabaw) — walay maguba niana. Ang makaguba sa
    tanan kay ang pagbali sa cube aron ibutang ang dalag sa laing dapit.

!!! success "Pagsusi"
    Ang upat ka edge sa ibabaw motakdo sa center sa ilang face. Makita nimo ang
    gamay nga **T nga usa ra ka kolor** sa matag usa sa upat ka kilid nga face.
    Ang corner na lang ang nahibilin.
