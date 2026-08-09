# 4 · Ang dalag nga cross

<div class="objectif" markdown>
![Dalag nga cross](../assets/cubes/but-croix-jaune.svg)
<figcaption>Ang tumong: dalag nga cross sa ibabaw. Ang edge ra ang gi-ihap — ang
corner puwede bisan unsa nga kolor.</figcaption>
</div>

!!! info "Ang edge ra atong tan-awon"
    Niini nga lakang, **ayaw gyud tagda ang upat ka corner**. Tan-awa lang ang
    dalag nga center ug ang upat ka edge sa palibot. Ang corner atubangon sa
    lakang 6 ug 7.

## Usa ra ka algorithm

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>Iyang balihon ang mga edge sa ibabaw. Depende sa imong nakuha, buhaton kini
kausa, kaduha o katulo — mao ra kana ang sulod niini nga lakang.</p>
</div>
</div>

## Ang tulo ka case

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/eo-point.svg" alt="Ang dot"><figcaption><b>Ang dot</b><br>Walay dalag nga edge.<br><code>3 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/eo-equerre.svg" alt="Ang L"><figcaption><b>Ang L</b><br>Duha ka edge nga nag-eskina.<br><code>2 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/eo-barre.svg" alt="Ang bar"><figcaption><b>Ang bar</b><br>Duha ka edge nga naglinya.<br><code>1 ka beses</code></figcaption></figure>
</div>

### Unsaon pagkupot sa cube

Mao ra kini ang lisod nga bahin sa lakang, ug sayon ra kini kung masabtan na.

=== "Ang dot"

    Walay espesyal nga posisyon. Buhata ang algorithm: makuha nimo ang L o ang
    bar. Padayon sa case nga imong nakuha.

=== "Ang L"

    Tuyoka ang `U` aron ibutang ang L **sa ibabaw-wala**, sama sa hulagway: ang
    duha ka bukton nagtudlo **paibabaw** ug **pawala**.

    Buhata ang algorithm: makuha nimo ang bar. Buhata pag-usab kausa.

=== "Ang bar"

    Tuyoka ang `U` aron ang bar mahimong **pahigda**, gikan sa wala paingon sa
    tuo.

    Buhata ang algorithm kausa: motungha ang cross.

!!! tip "Ang shortcut"
    Dot → L → bar → cross. Ang matag pagbuhat magpauswag nimo og usa ka ang-ang
    niini nga kadena. Kung sayop ang imong posisyon, mobalik ka og usa ka ang-ang
    sa kadena apan walay laing maguba — walay peligro.

!!! success "Pagsusi"
    Klaro nga dalag nga cross sa ibabaw. Ang dalag nga corner, sa laing bahin,
    nagkatag-katag: normal ug gipaabot kana.
