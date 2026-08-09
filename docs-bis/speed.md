# Aron mas paspas

Kini nga panid **walay algorithm**. Ang sulod niini mao ang naghimo sa kalainan
kung nahibaloan na nimo ang mga algorithm — ug kung nagsugod ka pa lang, mao kini
ang makadaginot nimo og pinakadaghang segundo.

## Unsay tinuod nga nagpahinay nimo

Timing-i ang imong kaugalingon kausa, ug tan-awa **asa maadto ang oras**. Halos
kanunay, makurat ka sa tubag:

| Unsay imong gituohan | Unsay tinuod nga nahitabo |
|---|---|
| "Hinay kaayo ko motuyok" | Paspas ka motuyok, apan **mohunong** ka tali sa mga lakang |
| "Kulang pa akong algorithm" | 40% sa oras imong gigahin sa **pagpangita** sa sunod nga piraso |
| "Kinahanglan ko mas magpraktis" | Mas paspas lang nimong gibalik-balik ang imong sayop |

Ang mga paghunong mas bug-at kay sa kapaspas sa tudlo. Ang solve nga 60 ka
segundo kasagaran adunay **20 ka segundo nga walay lihok ang kamot**.

## Ang lookahead

Mao kini ang sentro nga abilidad, ug mabansay kini.

Ang ideya: samtang ang imong tudlo naghimo sa sunod-sunod nga nahibaloan na nimo,
**ang imong mata nangita na sa sunod nga piraso**. Dili nimo kinahanglan tan-awon
ang imong kamot, kabalo na sila.

### Ang ehersisyo

Sulbara **hinay kaayo**, sa usa ka tulo ka bahin sa imong normal nga kapaspas, ug
dili gyud ka mohunong. Kinahanglan padayon nga motuyok ang cube, hinay apan walay
hunong.

Makapaglagot kini ug makahatag og ngil-ad nga oras sulod sa usa ka semana. Dayon
mawala ang mga paghunong, ug mas paspas ka pa kay sa una.

!!! tip "Ang lagda sa 3 ka segundo"
    Kung molapas ka og 3 ka segundo nga wala molihok ang cube, nangita ka —
    ug didto ang imong daog, dili sa bag-ong algorithm.

## Ang fingertrick

Ang usa ka lihok kinahanglan buhaton **sa usa ka tudlo**, dili sa pulso.

| Lihok | Tudlo | Timaan |
|---|---|---|
| `U` | index sa wala | itulod ang ibabaw paingon sa tuo |
| `U'` | index sa tuo | ang labing kanunay nga lihok sa cube |
| `R` | palasingsingan sa tuo | itulod paibabaw |
| `R'` | index sa tuo | ibira paubos |
| `F` | index sa tuo + kumagko sa wala | |
| `M` | palasingsingan sa wala | ibira ang slice paingon nimo |

!!! tip "Ang pagsulay sa sexy move"
    Ang `R U R' U'` kinahanglan buhaton **nga dili molihok ang imong palad**,
    tudlo ra ang mogamit. Kung usbon nimo ang imong pagkupot tali sa duha ka
    lihok, wala pa nimo makab-ot ang fingertrick. Balika hinay-hinay hangtod nga
    dili na molihok ang imong pagkupot.

## Ang gamit

!!! warning "Ang orihinal nga cube usa gyud ka babag"
    Ang branded nga Rubik's gikan sa tindahan **maghunong**: dili kini motuyok
    kung dili hingpit nga naglinya ang mga face. Ang bisan unsang moderno nga
    "speedcube" nga 15 € mas nindot gyud kaayo ug makawagtang sa katunga sa imong
    pagduha-duha.

    Mao ra kini ang paliton nga naghatag og tinuod nga kalainan. Ang uban kay
    kahayahay lang.

Pipila ka giya:

- **Tension**: kinahanglan motuyok ang cube nga dili pugson, apan dili mabungkag
  kung uyogon nimo. Kadaghanan sa bag-ong cube ma-adjust nga walay gamit.
- **Lubricant**: usa ka tulo, kaduha sa usa ka tuig. Daghan ang sobra og butang.
- **Magnet**: maghimo sila og "klik" kung maglinya ang face. Nindot kaayo, apan
  dili gyud kinahanglan.

## Usa ka plano sa pagbansay nga makayanan

Baynte minutos, tulo ka beses sa usa ka semana, mas maayo kay sa tulo ka oras sa
Domingo.

1. **5 min — pag-init.** Napulo ka normal nga solve, walay timer.
2. **5 min — cross lamang.** Baynte ka cross nga gi-timing, lakip ang inspection.
3. **5 min — usa ka kahuyangan.** Usa ka case sa F2L, o tulo ka algorithm sa PLL.
4. **5 min — hinay nga solve.** Walay bisan usa ka paghunong, sama sa gihisgutan
   sa ibabaw.

!!! success "Unsaon pagkahibalo kung nag-uswag ka"
    Ayaw tan-awa ang imong pinakamaayong oras: nagdepende kana sa suwerte sa
    scramble. Tan-awa ang imong **aberids sa 12 ka solve**, nga kuhaan sa
    pinakamaayo ug pinakangil-ad. Mao kini ang sukod nga gigamit sa kompetisyon,
    ug mao ra kini ang mabasa nga tin-aw.
