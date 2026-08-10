# F2L — ang unang duha ka layer

Mao **kini** ang kausaban nga labing makadaginot sa oras, ug walay algorithm nga
kinahanglan tun-an. Hatagi kini nga panid sa panahon nga kinahanglan niini.

## Ang ideya

Sa beginner nga pamaagi, ibutang nimo ang puti nga corner, dayon, unya na, ang
edge nga naa ra gyud sa tapad niini. Busa makaduha ka moagi sa parehong dapit.

Ang F2L magbutang **kanilang duha dungan**. Ang puti-berde-orange nga corner ug
ang berde-orange nga edge maghimo og usa ka **pares**: tapoon nimo sila sa
ibabaw nga layer, dayon isulod ang pares sa usa lang ka lihok.

Upat ka pares, upat ka slot, ug human na ang duha ka tulo ka bahin sa cube.

!!! success "Ang daog, sa numero"
    Beginner nga pamaagi: mga 8 ka lihok matag corner + 8 matag edge, sa ato pa
    **64 ka lihok** para sa duha ka layer.
    F2L: mga **7 ka lihok matag pares**, sa ato pa **28 ka lihok**. Pareho ra ang
    resulta.

## Ang bugtong lihok nga kinahanglan masabtan

Ang tibuok F2L nagsukad sa usa ka obserbasyon: ang tulo ka lihok nga `R U R'`
**maggawas sa pares gikan sa slot**, ug ang `R U' R'` **magbalik niini**.

<figure class="film">
<img src="/bis/assets/cubes/film-trigger-droit.svg" alt="R U R' — ang sequence, matag lihok">
<figcaption><code>R U R'</code> — ang sequence, matag lihok</figcaption>
</figure>

<figure class="film">
<img src="/bis/assets/cubes/film-trigger-droit-inverse.svg" alt="R U' R' — ang sequence, matag lihok">
<figcaption><code>R U' R'</code> — ang sequence, matag lihok</figcaption>
</figure>

Kuhaa ang nasulbad nga cube ug buhata ang `R U R'`. Tan-awa ang front-right nga
slot: ang corner ug ang edge nanggawas, dungan, ngadto sa ibabaw nga layer.
Buhata ang `R U' R'` aron ibalik sila.

Mao ra kana ang tibuok F2L. Ang uban kay ang pagdala sa pares sa husto nga
kahimtang sa dili pa isulod.

## Ang pamaagi sa tulo ka pangutana

Kung naa kay pares, pangutan-a ang imong kaugalingon niining tulo, sunod-sunod.

### 1. Asa ang corner?

- **Sa ibabaw nga layer** → maayo, mahimo na ka magtrabaho.
- **Naipit sa slot** → ipagawas gamit ang `R U R'` (o ang katumbas niini sa
  maong kilid), dayon balik sa pangutana 1.

### 2. Asa ang edge?

- **Sa ibabaw nga layer** → maayo.
- **Naipit sa slot** → ipagawas, pareho sa corner.

### 3. Unsaon nako pagtapo kanila?

Ang duha ka piraso naa na sa ibabaw. Kinahanglan itapad sila, sa husto nga
direksyon, dayon isulod ang pares. Dinhi naa ang tanang intuitive nga trabaho:

- **Ablihi ang slot** gamit ang `R U R'` o `F' U' F` — maghimo kini og lugar.
- **Dad-a ang laing piraso** sa ibabaw niini gamit ang `U`, `U'` o `U2`.
- **Siradohi** pinaagi sa pagbalik sa lihok nga imong giablihan.

!!! tip "Ang reflex nga makasulbad sa 90% sa mga case"
    Kung dili nimo makita unsay buhaton: **ablihi ang slot** (`R U R'`), tan-awa
    unsay nahitabo, `U` aron ibalhin, dayon **siradohi**. Sa kadaghanan sa mga
    case, matapo ang pares o mas maduol gyud siya.

## Ang tulo ka batakang case

Kini ra ang kinahanglan nimong mahibaloan aron makasugod. Ang tanan nga uban
mahulog niini sulod sa usa o duha ka lihok.

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/f2l-01.svg" alt="Batakang case 1"><figcaption><b>Natapo na ang pares</b><br>Diretso nga pagsulod</figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/f2l-02.svg" alt="Batakang case 2"><figcaption><b>Nagbulag ang piraso</b><br>Ablihi, ipahiluna, siradohi</figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/f2l-03.svg" alt="Batakang case 3"><figcaption><b>Baliktad ang pares</b><br>Bungkaga dayon tapoa pag-usab</figcaption></figure>
</div>

## Upat ka tambag nga makausab sa tanan

!!! tip "Trabahoa ang upat ka slot, dili lang ang tuo"
    Daghan ang motuyok sa cube aron kanunay magtrabaho sa front-right. Usa kana
    ka nausik nga rotation matag pares. Tun-i usab ang pagsulod sa **front-left**
    gamit ang `F' U' F` ug `F' U F`, nga mao ang mirror niini.

<figure class="film">
<img src="/bis/assets/cubes/film-trigger-gauche.svg" alt="F' U' F — ang sequence, matag lihok">
<figcaption><code>F' U' F</code> — ang sequence, matag lihok</figcaption>
</figure>

<figure class="film">
<img src="/bis/assets/cubes/film-trigger-gauche-inverse.svg" alt="F' U F — ang sequence, matag lihok">
<figcaption><code>F' U F</code> — ang sequence, matag lihok</figcaption>
</figure>

!!! tip "Pilia ang imong pares, ayaw pagpaagi-agi"
    Human sa cross, tan-awa ang upat ka pares ug sugdi sa **labing sayon** —
    kadtong ang duha ka piraso makita na sa ibabaw. Samtang gisulod nimo kini,
    naa kay panahon sa pagpangita sa sunod.

!!! tip "Paghinay aron mopaspas"
    Ang F2L nga gibuhat sa tibuok kakusog apan gisundan og tulo ka segundo nga
    pagpangita sa sunod nga pares kay **mas hinay** kay sa kalma nga F2L diin
    mangita ka samtang nagtuyok ka. Mao kana ang lookahead, ug mao kana ang tinuod
    nga hisgutanan.

!!! warning "Ayaw dayon tan-awa ang 41 ka case"
    Ang [kompleto nga lista](../advanced/f2l.md) naa, ug mapuslanon kini — unya
    na. Ang F2L nga gisag-ulo nga wala masabti makapugong nimo sa dugay nga
    panahon, kay dili nimo mahibaloan unsay buhaton sa mga case nga wala nimo
    masag-uloi.

    Gamita kini nga diksyonaryo: kung naay usa ka case nga kanunay makahurot sa
    imong oras, adto tan-awa unsaon kini pagbuhat sa husto.
