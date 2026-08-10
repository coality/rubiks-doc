# 3 · Ang ikaduhang layer

<div class="objectif" markdown>
![Nahuman nga duha ka layer](../assets/cubes/but-couronne2.svg)
<figcaption>Ang tumong: duha ka tulo ka bahin sa cube. Ang ibabaw nga layer na
lang ang gubot.</figcaption>
</div>

Upat ka edge pa ang ibutang, kadtong naa sa tunga. **Walay bisan usa niini nga
adunay dalag** — mao kini ang timailhan aron mailhan sila sa ibabaw nga layer.

<div class="objectif" markdown>
![arete/centres](../assets/cubes/arete-deux-centres.svg)
<figcaption>Ang berde-orange nga edge mosulod sa taliwala sa berde ug orange nga center — ug wala nay lain.</figcaption>
</div>

## Pag-ila sa husto nga edge

Tan-awa ang ibabaw nga layer ug pangitaa ang edge nga **walay dalag**.
Pananglitan, usa ka berde-orange nga edge.

Tuyoka ang `U` hangtod nga **ang kolor sa iyang atubangan** motakdo sa center
niana nga face: kung berde ang gipakita sa kilid, dad-a siya sa berde nga face.
Makita nimo dayon ang **baliktad nga T** nga usa ra ka kolor sa atubangan nga
face.

Ang laing kolor sa edge (ang orange, naa sa ibabaw) mao ang magsulti kanimo
**asa nga kilid** siya manaog: paingon sa orange nga face.

## Ang duha ka case

Duha ra gyud, ug ang ikaduha mao ang eksakto nga mirror sa una.

Sa ilawom sa matag card, gipakita ang sequence **matag lihok**: ang matag
hulagway mao ang cube sa wala pa moliso, ug ang arrow mao ang move nga buhaton.

### Kaso 1 — ang edge moadto sa tuo

<div class="fiche" markdown>
![Pagsulod sa tuo](../assets/cubes/couronne2-droite.svg)
<div class="corps" markdown>
<span class="move">U R U' R' U' F' U F</span>
<p><b>Ang edge kinahanglan moadto sa tuo.</b> Ang T naa sa imong atubangan, ug
ang kolor sa ibabaw motakdo sa center sa tuo nga face.</p>
</div>
</div>

<div class="objectif" markdown>
![Ang edge mobiya sa ibabaw ug manaog sa front-right nga slot](../assets/cubes/3d-arete-insere-droite.svg)
<figcaption>Ang edge mobiya sa ibabaw nga layer ug manaog sa front-right nga slot. Mao ra kana ang gibuhat sa algorithm.</figcaption>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-couronne2-droite.svg" alt="U R U' R' U' F' U F — ang sequence, matag lihok">
<figcaption><code>U R U' R' U' F' U F</code> — ang sequence, matag lihok</figcaption>
</figure>

### Kaso 2 — ang edge moadto sa wala

<div class="fiche" markdown>
![Pagsulod sa wala](../assets/cubes/couronne2-gauche.svg)
<div class="corps" markdown>
<span class="move">U' L' U L U F U' F'</span>
<p><b>Ang edge kinahanglan moadto sa wala.</b> Pareho ra gyud nga sunod-sunod,
gi-mirror lang: ang matag <code>R</code> mahimong <code>L</code>, ug ang matag
direksyon mabaliktad.</p>
</div>
</div>

<div class="objectif" markdown>
![Ang edge mobiya sa ibabaw ug manaog sa front-left nga slot](../assets/cubes/3d-arete-insere-gauche.svg)
<figcaption>Ang eksaktong mirror: karon manaog ang edge sa <b>front-left</b> nga slot.</figcaption>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-couronne2-gauche.svg" alt="U' L' U L U F U' F' — ang sequence, matag lihok">
<figcaption><code>U' L' U L U F U' F'</code> — ang sequence, matag lihok</figcaption>
</figure>

!!! tip "Unsaon pagsag-ulo sa duha ka algorithm dungan"
    Ayaw sila tun-i nga bulag. Sag-uloha ang bersyon sa tuo, dayon hinumdomi ang
    lagda: **ilisan ang `R` og `L`, ang `U` og `U'`, ug ang `F` og `F'`**.
    Itapad ang duha ka linya ug makita dayon nimo ang simetriya.

## Walay magamit nga edge sa ibabaw?

Usahay ang upat ka edge sa ibabaw adunay tanan og dalag, apan wala pa mahuman ang
ikaduhang layer. Nagpasabot kini nga naay edge nga **naa na sa layer, apan sayop
ang lugar o baliktad**.

<div class="objectif" markdown>
![intrus](../assets/cubes/couronne2-intrus.svg)
<figcaption>Naay <b>langyaw</b> nga edge nga naipit sa front-right nga slot (makita ang dalag sa kilid). Kinahanglan kini ipagawas gamit ang algorithm sa tuo.</figcaption>
</div>

Kinahanglan siya ipagawas: ibutang siya sa front-right nga slot, ug buhata ang
algorithm **sa tuo** nga daw naay imong gisulod. Mosaka ang dili angay ngadto sa
ibabaw nga layer, ug mahimo na nimo siyang atubangon sa normal nga paagi.

!!! success "Pagsusi"
    Human na ang ubos nga duha ka tulo ka bahin sa cube: ang matag kilid nga
    face nagpakita og duha ka kompleto nga banda sa iyang kolor. Ang dalag nga
    layer na lang ang nahibilin.

Gikan dinhi, **dili na gyud ta mobali sa cube**: ang dalag magpabilin sa ibabaw
hangtod sa katapusan.
