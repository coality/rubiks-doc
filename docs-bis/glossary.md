# Glossary

## Ang mga termino sa cube

**Algorithm** (o *alg*)
: Usa ka sinag-ulo nga sunod-sunod nga lihok nga naghatag og eksaktong epekto,
  samtang wala matandog ang uban nga bahin sa cube.

**AUF** (*Adjust Upper Face*)
: Ang gamay nga `U` o `U'` nga buhaton sa dili pa o human sa algorithm aron
  ipahiluna kini. Dili kini apil sa algorithm.

**Center**
: Piraso nga adunay **usa** ka sticker. Ang unom ka center dili gyud molihok sa
  usag usa: sila ang nagtakda sa kolor sa matag face.

**Commutator**
: Sunod-sunod nga lihok nga sama sa "buhata ang A, buhata ang B, bawia ang A,
  bawia ang B". Gamay ra kaayo ang bahin sa cube nga iyang matandog. Ang
  `R' D' R D` usa niini.

<details class="film">
<summary><code>R' D' R D</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-commutateur.svg" alt="R' D' R D — ang sequence, matag lihok">
</details>

**Corner**
: Piraso nga adunay **tulo** ka sticker, naa sa eskina sa cube. Naay 8.

**Edge**
: Piraso nga adunay **duha** ka sticker, taliwala sa duha ka center. Naay 12.

**Headlights**
: Duha ka corner nga managsama og kolor sa usa ka face, ug lahi ang edge sa
  ilang taliwala. Gamiton aron mailhan ang case sa PLL.

**Orientation**
: Ang **direksyon** sa pagkabutang sa piraso. Mahimong husto ang lugar sa piraso
  apan sayop ang orientation.

**Pares** (*pair*)
: Ang corner ug ang edge nga naa ra gyud sa tapad niini, giatubang nga dungan.
  Pundasyon sa F2L.

**Permutation**
: Ang **lugar** sa matag piraso, bisan unsa pa ang iyang direksyon.

**Slot**
: Ang puy-anan sa pares nga corner + edge sulod sa unang duha ka layer. Naay
  upat.

## Ang mga pamaagi ug lakang

**CFOP** (o *Fridrich nga pamaagi*)
: Ang pamaagi sa kompetisyon: **C**ross, **F**2L, **O**LL, **P**LL. 78 ka
  algorithm tanan.

**Cross**
: Ang cross sa unang layer. Unang lakang sa CFOP.

**F2L** (*First Two Layers*)
: Ang unang duha ka layer, gisulbad pinaagi sa pares nga corner + edge. 41 ka
  case, apan tun-an kini sa intuitive nga paagi.

**4LLL** (*4-Look Last Layer*)
: Ang last layer sa upat ka lakang imbes duha. **16 ka algorithm** imbes 78. Ang
  natural nga tulay tali sa beginner nga pamaagi ug sa CFOP.

**Lookahead**
: Ang pagpangita sa sunod nga piraso pinaagi sa mata samtang ang tudlo naghimo pa
  sa kasamtangan nga sunod-sunod. Ang abilidad nga nagbulag sa mga ang-ang.

**OLL** (*Orientation of the Last Layer*)
: Ang paghimo sa tibuok top face nga dalag, nga walay pagtagad sa lugar. 57 ka
  case.

**PLL** (*Permutation of the Last Layer*)
: Ang pagbutang sa matag piraso sa last layer sa iyang lugar. 21 ka case.

## Ang mga algorithm nga adunay ngalan

**Named perms** (A, E, F, G, H, J, N, R, T, U, V, Y, Z)
: Ang 21 ka case sa PLL, ginganlan sunod sa porma nga gidrowing sa mga arrow sa
  paglihok.

**Sexy move**
: `R U R' U'`. Ang labing gamit nga sunod-sunod sa cube. Kung balikon og unom ka
  beses, mobalik kini sa gisugdan.

<details class="film">
<summary><code>R U R' U'</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-sexy.svg" alt="R U R' U' — ang sequence, matag lihok">
</details>

**Sune**
: `R U R' U R U2 R'`. Mag-orient og tulo ka corner. Uban sa iyang mirror nga
  **anti-Sune** (`R U2 R' U' R U' R'`), mao kini ang unang tinuod nga algorithm
  sa OLL nga tun-an.

<details class="film">
<summary><code>R U R' U R U2 R'</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-sune.svg" alt="R U R' U R U2 R' — ang sequence, matag lihok">
</details>

<details class="film">
<summary><code>R U2 R' U' R U' R'</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-antisune.svg" alt="R U2 R' U' R U' R' — ang sequence, matag lihok">
</details>

**T-perm**
: `R U R' U' R' F R2 U' R' U' R U R' F'`. Ang labing ilado nga PLL: magbayloay
  siya og duha ka corner ug duha ka edge.

<details class="film">
<summary><code>R U R' U' R' F R2 U' R' U' R U R' F'</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-tperm.svg" alt="R U R' U' R' F R2 U' R' U' R U R' F' — ang sequence, matag lihok">
</details>

## Ang mga sukod

**Ao5, Ao12** (*average of 5 / of 12*)
: Ang aberids sa 5 o 12 ka solve, **nga kuhaan sa pinakamaayo ug pinakangil-ad
  nga oras**. Mao kini ang opisyal nga sukod sa kompetisyon, mas kasaligan kay sa
  usa ka bulag nga rekord.

**HTM** (*Half Turn Metric*)
: Paagi sa pag-ihap sa lihok: ang half turn (`R2`) mag-ihap og **usa** ra ka
  lihok.

**Inspection**
: Ang 15 ka segundo nga gihatag sa dili pa magsugod ang timer, aron planohon ang
  cross.
