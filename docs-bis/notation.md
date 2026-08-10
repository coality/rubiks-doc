# Ang cube ug ang notation

## Ang tulo ka matang sa piraso

Ang 3×3 walay 26 ka piraso nga puwede magbayloay. Tulo ka pamilya kini, ug **ang
usa ka piraso dili gyud mausab og pamilya**. Mao kini ang labing importante nga
ideya sa tibuok panid.

| | Gidaghanon | Sticker | Ang ilang kalahian |
|---|---|---|---|
| **Center** | 6 | 1 | **Dili gyud** sila mabalhin sa usag usa |
| **Edge** | 12 | 2 | Naa sa taliwala sa duha ka center |
| **Corner** | 8 | 3 | Naa sa walo ka eskina |

!!! tip "Ang center maoy nagtakda sa kolor"
    Ang pagtuyok sa usa ka face dili makabalhin sa iyang center. Busa ang berde
    nga center **mao gyud** ang berde nga face — bisan pa og hilabihan ka gubot
    ang cube. Kung mangita ka asa moadto ang usa ka piraso, tan-awa ang center,
    dili ang ubang piraso.

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/familles-centres.svg" alt="Ang 6 ka center"><figcaption><b>Ang 6 ka center</b></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/familles-aretes.svg" alt="Ang 12 ka edge"><figcaption><b>Ang 12 ka edge</b></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/familles-coins.svg" alt="Ang 8 ka corner"><figcaption><b>Ang 8 ka corner</b></figcaption></figure>
</div>

Ang piraso dili gyud mausab og pamilya: kining tulo ka grupo dili gyud magsagol.

    Mao usab kini ang hinungdan nga ang asul-orange nga edge dili gyud makasulod
    sa taliwala sa berde ug pula nga center: sayop ang iyang kolor.

## Unsaon pagkupot sa cube

Usa ra ka lagda, tinuod sa tibuok site: **ang face nga importante naa sa ibabaw,
ug dili balihon ang cube samtang naa sa tunga sa algorithm.**

Tulo ka axis ang cube:

- **U** (*Up*) sa ibabaw, **D** (*Down*) sa ubos
- **F** (*Front*) atubangan nimo, **B** (*Back*) sa luyo
- **R** (*Right*) sa tuo, **L** (*Left*) sa wala

<div class="objectif" markdown>
![3d-faces](assets/cubes/3d-faces.svg)
<figcaption>Ang tulo ka face nga imong makita: <b>U</b> sa ibabaw, <b>F</b> sa imong atubangan, <b>R</b> sa tuo. Kini nga mga letra nagpasabot og posisyon, dili kolor.</figcaption>
</div>

Kini nga mga letra nagpasabot og **posisyon, dili kolor**. Ang `R` nagpasabot og
"ang face nga naa sa imong tuo karon", bisan unsa pa ang iyang kolor.

## Ang notation

### Ang unom ka batakang lihok

Usa ka letra nga nag-inusara = **usa ka quarter turn niana nga face, clockwise**,
kung imong atubangon mismo kana nga face.

| Notation | Basahon | Epekto |
|---|---|---|
| `R` | *R* | Ang tuo nga face, usa ka quarter turn clockwise |
| `R'` | *R prime* | Ang tuo nga face, usa ka quarter turn **counter-clockwise** |
| `R2` | *R two* | Ang tuo nga face, usa ka **half** turn (bisan asa nga direksyon) |

Ug mao usab sa `U`, `D`, `F`, `B`, `L`.

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/3d-move-r.svg" alt="R"><figcaption><b>R</b><br><code>mosaka ang atubangan sa R</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/3d-move-rp.svg" alt="R'"><figcaption><b>R'</b><br><code>baliktad</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/3d-move-u.svg" alt="U"><figcaption><b>U</b><br><code>ang ibabaw nga face</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/3d-move-f.svg" alt="F"><figcaption><b>F</b><br><code>ang atubangan nga face</code></figcaption></figure>
</div>

!!! warning "Ang lit-ag sa clockwise"
    Ang "clockwise" gisabot **samtang gitan-aw mismo kana nga face**. Busa para
    sa `D` (ang ubos nga face), kinahanglan handurawon nimo nga naa ka sa ilawom
    sa cube ug nagtan-aw pataas. Kung gikan sa ibabaw ka motan-aw, morag
    counter-clockwise ang `D`. Mao kini ang numero unong sayop sa mga
    beginner — ug ang hinungdan nga ang maayong algorithm maglikay sa `D`.

### Ang slice nga lihok

Ang slice mao ang layer sa **tunga**, kadtong walay corner.

| Notation | Basahon | Epekto |
|---|---|---|
| `M` | *M* | Slice sa taliwala sa `L` ug `R`, mosunod sa direksyon sa `L` |
| `E` | *E* | Slice sa taliwala sa `U` ug `D`, mosunod sa direksyon sa `D` |
| `S` | *S* | Slice sa taliwala sa `F` ug `B`, mosunod sa direksyon sa `F` |

Ang `M` mao ang labing gamit (makita siya sa pinakamaayong algorithm sa edge).
Hinumdomi lang: **ang `M` mosunod sa direksyon sa `L`**, buot pasabot paingon
nimo agi sa ibabaw.

### Ang pagtuyok sa tibuok cube

| Notation | Epekto |
|---|---|
| `x` | Ang tibuok cube motikig sa direksyon sa `R` (ang atubangan mosaka) |
| `y` | Ang tibuok cube motuyok sa direksyon sa `U` |
| `z` | Ang tibuok cube moliso sa direksyon sa `F` |

Ang pagtuyok walay masulbad: giusab lang niini kung unsa nga face ang imong
giatubang. **Wala gyud ka magkinahanglan** niini sa beginner nga pamaagi.

### Ang wide nga lihok

Ang **gamay** nga letra = ang face **ug** ang slice sa likod niini, duha ka layer
dungan. `r` = `R` + `M'`. Magamit ra ni gikan sa kompleto nga OLL.

## Pagpraktis sa pagbasa

Kuhaa ang imong nasulbad nga cube, ug hinay-hinay buhata:

```
R U R' U'
```

Buhata kini og **unom ka beses sunod-sunod**. Mobalik ang cube sa nasulbad nga
kahimtang. Kung dili, naay direksyon nga imong nabaligtad — balik sa nasulbad nga
cube, ug hinay-hinaya pa.

!!! success "Nganong molihok kini"
    Kini nga sunod-sunod nga lihok gitawag og *sexy move*, ug mao kini ang labing
    gamit nga sunod-sunod sa tibuok cube. Kini **order 6**: kung balikon og unom
    ka beses, mobalik siya sa iyang gisugdan. Maayo kaayo kini nga pagsulay aron
    masiguro nga husto ang imong pagbasa sa notation.

Kung ang `R U R' U'` × 6 makabalik nimo sa nasulbad nga cube sa unang sulay,
kabalo na ka mobasa sa notation. Puwede na ka mosugod sa
[beginner nga pamaagi](beginner/index.md).


<details class="film">
<summary><code>R U R' U'</code> — ang sequence, matag lihok</summary>
<img src="/bis/assets/cubes/film-sexy.svg" alt="R U R' U' — ang sequence, matag lihok">
</details>