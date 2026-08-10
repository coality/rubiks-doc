# 2 · Ang puti nga corner

<div class="objectif" markdown>
![Nahuman nga unang layer](../assets/cubes/but-couronne1.svg)
<figcaption>Ang tumong: ang tibuok ubos nga layer, ug usa ka kompleto nga bandang
husto og kolor sa matag kilid nga face.</figcaption>
</div>

Upat ka corner pa ang ibutang: kadtong adunay puti. Isulod nimo sila usa-usa,
kanunay sa parehong paagi.

## Ang prinsipyo

Ang corner mosulod **sa taliwala sa tulo ka center**. Busa ang
puti-berde-orange nga corner moadto sa nagsangang dapit sa puti, berde ug orange
nga face — wala nay laing lugar nga posible.

<div class="objectif" markdown>
![corner taliwala sa tulo ka center](../assets/cubes/3d-coin-trois-centres.svg)
<figcaption>Tan-aw <b>gikan sa ilawom</b>, sa nahuman nga cube: ang
puti-berde-orange nga corner naghikap gyud sa puti, berde ug orange nga center.
Mao ra kana ang iyang posible nga adtoan — gray ang tanan nga uban.</figcaption>
</div>

## Ang paagi

Ang tanan nga hulagway niini nga seksyon nagpakita sa kahimtang **sa dili pa**
ka motuyok: tan-awa sila, ilha ang imong case, ug ugma-damlag pa buhata.

<div class="objectif" markdown>
![ang slot nga adtoan](../assets/cubes/3d-coin-fente.svg)
<figcaption>Ang sinugdanan, tan-aw gihapon <b>gikan sa ilawom</b>: ang puti nga
corner naghulat sa ibabaw, ug ang arrow nagpakita sa lungag nga iyang adtoan.
Ang bisan unsa nga naa karon niana nga lungag walay bili — ipagawas ra
siya.</figcaption>
</div>

1. **Pangitaa ang puti nga corner** sa ibabaw nga layer.
2. **Tuyoka ang `U`** aron dad-on kini **mismo sa ibabaw sa lungag nga iyang
   adtoan**. Kinahanglan naa gyud ang corner sa ibabaw sa iyang lugar, usa ka
   andana ang gilay-on.
3. Kupti ang cube aron kana nga corner maanaa **sa ibabaw-tuo, atubangan nimo**.
4. **Tan-awa asa nag-atubang ang iyang puti nga sticker.** Kana ra ang
   magtakda sa gidaghanon sa balik — kanunay **kulang** (odd):

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/3d-coin-blanc-avant.svg" alt="Puti sa atubangan"><figcaption><b>Puti sa atubangan</b><br><code>1 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/3d-coin-blanc-haut.svg" alt="Puti sa ibabaw"><figcaption><b>Puti sa ibabaw</b><br><code>3 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/3d-coin-blanc-droite.svg" alt="Puti sa tuo"><figcaption><b>Puti sa tuo</b><br><code>5 ka beses</code></figcaption></figure>
</div>

Ang arrow nagpakita sa tinuod nga agianan sa puti: mobiya siya sa ibabaw nga
layer ug moabot sa ilawom sa cube, sa iyang lugar.

**Buhata dayon ang sunod-sunod nga lihok sumala niana nga gidaghanon:**

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">R' D' R D</span>
<p>Manaog ang corner sa slot, moliso, mosaka pag-usab, ug sa kadugayan mahiluna
sa husto nga direksyon. <b>Ayaw gyud hunong sa tunga.</b></p>
</div>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-coin-blanc.svg" alt="R' D' R D — ang sequence, matag lihok">
<figcaption>Ang sequence matag lihok: ang matag hulagway nagpakita sa cube <b>sa wala pa</b> moliso, ug ang arrow nagpakita sa move nga buhaton.</figcaption>
</figure>

!!! tip "Dili nimo kinahanglan mag-ihap"
    Balika lang hangtod nga mahiluna ang corner, ang puti naa sa ubos. Ang mga
    hulagway sa ibabaw naa ra aron dili ka mabalaka kung morag dugay na: normal
    ra ang lima ka balik, dili kana sayop.

    Ang **2 ug 4 dili gyud molihok** dinhi: ang parehas nga numero magbalik sa
    corner sa iyang gigikanan gyud.

!!! warning "Ayaw hunong sa tunga"
    Sa taliwala sa duha ka balik, morag guba ang ubos nga bahin sa cube. Normal
    ra kana: ang sunod-sunod nga lihok maggawas og piraso ug mobalik niini. Kung
    mohunong ka sa tunga, maguba ang cross. **Padayon kanunay hangtod nga
    mahiluna ang corner.**

## Naipit ang corner sa ubos apan sayop ang dapit

Kanunay ni mahitabo: naa na ang puti nga corner sa ubos nga layer, apan sayop ang
lugar o sayop ang atubangan.

Ibutang siya sa ubos-tuo atubangan nimo, ug buhata ang `R' D' R D` og **kausa**.
Mosaka ang corner ngadto sa ibabaw nga layer. Mahimo na nimo kining atubangon sa
normal nga paagi.

!!! success "Pagsusi"
    Puro na puti ang puti nga face, ug ang upat ka kilid nga face adunay banda sa
    ubos nga usa ra ka kolor. Usa ka tulo ka bahin sa cube nahuman na.

## Nganong molihok kini nga sunod-sunod

Ang `R' D' R D` usa ka **commutator**: magbuhat siya og usa ka butang, magbuhat
og lain, dayon iyang bawion ang una. Ang resulta: usa ra ka corner ang iyang
matandog, ug ibalik niya kini nga lahi ang pagkaliso. Makita nimo pag-usab kini
gyud nga sunod-sunod sa [lakang 7](7-corners-oriented.md) — mao ra kini ang
algorithm nga gigamit makaduha.
