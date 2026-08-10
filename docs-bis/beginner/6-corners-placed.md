# 6 · Pagbutang sa dalag nga corner

<div class="objectif" markdown>
![Ang upat ka corner naa na sa lugar, apan sayop pa ang pagkaliso](../assets/cubes/but-coins-places.svg)
<figcaption>Ang tumong: ang matag corner naa na sa iyang lugar — ang tulo ka kolor niini
mao ang tulo ka face nga iyang gitandog. Wala pa sila sa hustong kilid; ang
step 7 ang mag-atiman niana.</figcaption>
</div>

Ibutang nato ang matag corner **sa husto nga lugar**, nga dili tagdon ang iyang
orientation. Busa mahimong naa na ang corner sa iyang lugar apan ang dalag naa sa
kilid: husto ra kana niini nga lakang.

## Pag-ila sa corner nga husto ang lugar

Ang corner **husto ang lugar** kung ang iyang tulo ka kolor motakdo sa tulo ka
face nga iyang gihikap, **bisan unsa pa ang han-ay**.

Pananglitan: ang dalag-berde-orange nga corner husto ang lugar kung siya naa sa
nagsangang dapit sa dalag, berde ug orange nga face. Wala kay labot kung ang
dalag naa sa ibabaw o sa kilid.

!!! tip "Ang siguradong paagi sa pagsusi"
    Kuhaa ang usa ka corner, hinumdomi ang iyang tulo ka kolor, ug tan-awa ang
    tulo ka center sa palibot niini. Kung pareho ang duha ka trio, husto ang
    iyang lugar.

Karon ihapa pila ka corner ang husto ang lugar. Kanunay kini **wala, usa, o
upat**.

## Ang algorithm

<div class="fiche" markdown>
![Pag-cycle sa tulo ka corner](../assets/cubes/coins-placer.svg)
<div class="corps" markdown>
<span class="move">U R U' L' U R' U' L</span>
<p>Iyang i-cycle ang <b>tulo ka corner</b> sa ilang kaugalingon ug pasagdan ang
ikaupat. Malisohan niya ang corner samtang naglihok: normal ra kana, ang lakang 7
maoy moatubang niini.</p>
</div>
</div>

<div class="objectif" markdown>
![Tulo ka corner ang magtinabangay ug ilis; ang ikaupat dili molihok](../assets/cubes/3d-coins-cycle.svg)
<figcaption>Tulo ka corner ang mag-ilisay; ang ikaupat magpabilin. Ang <b>placement</b>
ra ang importante dinhi — ang orientation mao ang step 7.</figcaption>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-coins-places.svg" alt="U R U' L' U R' U' L — ang sequence, matag lihok">
<figcaption>Ang sequence matag lihok: ang matag hulagway nagpakita sa cube <b>sa wala pa</b> moliso, ug ang arrow nagpakita sa move nga buhaton.</figcaption>
</figure>

## Unsaon pagposisyon

=== "Naay usa ka corner nga husto"

    Kupti ang cube aron kana nga corner maanaa **sa ibabaw-tuo, atubangan
    nimo**. Siya ang dili hilabtan sa algorithm.

    Buhata ang algorithm. Kung wala pa mahusto ang upat ka corner, buhata
    pag-usab gikan sa parehong posisyon.

=== "Walay corner nga husto"

    Buhata ang algorithm gikan sa bisan unsang posisyon. Makakuha ka dayon og usa
    ka corner nga husto. Balik sa case sa ibabaw.

=== "Husto na ang upat"

    Human na ang lakang. Adto sa [katapusan](7-corners-oriented.md).

!!! success "Pagsusi"
    Husto na ang lugar sa upat ka corner. Morag **mas gubot pa kay sa una** ang
    cube sa ibabaw, tungod kay nagkatag-katag ang pagkaliso sa corner. Timailhan
    kana nga maayo ang tanan: usa na lang ka lakang ang nahibilin.
