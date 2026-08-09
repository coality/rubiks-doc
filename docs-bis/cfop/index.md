# Pagbalhin sa CFOP — nganong ug unsang han-ay

Ang **CFOP** mao ang pamaagi nga gigamit sa halos tanan nga kompetidor. Ang
ngalan niini gikan sa upat ka lakang: **C**ross, **F**2L, **O**LL, **P**LL.

## Unsay tinuod nga nausab

Ang imong beginner nga pamaagi adunay pito ka lakang. Ang CFOP upat ra:

| Beginner nga pamaagi | CFOP | Daog |
|---|---|---|
| 1 · puti nga cross | **Cross** — pareho ra, apan mas maayo | mga lihok |
| 2 · puti nga corner<br>3 · ikaduhang layer | **F2L** — silang duha dungan | **dako kaayo** |
| 4 · dalag nga cross<br>5 · pagbutang sa edge | **OLL** — i-orient ang tibuok face | algorithm |
| 6 · pagbutang sa corner<br>7 · pag-orient sa corner | **PLL** — i-permute ang tanan | algorithm |

!!! success "Ang usa ka kausaban nga tinuod nga importante"
    Ang **F2L** naghiusa sa lakang 2 ug 3: imbes ibutang ang corner dayon ang
    edge nga bulag, imong tapoon sila nga pares ug isulod nga dungan.

    Mao kini ang makapaubos sa imong oras og katunga — ug **walay algorithm nga
    kinahanglan sag-ulohon**. Kung usa ra ka butang ang imong buhaton gikan
    niini nga seksyon, kana na.

## Ang han-ay sa pagtuon

Daghan ang napakyas tungod kay ilang giatubang ang 57 OLL una. Mao kini ang
pinakadautan nga agianan: dako ang paningkamot, gamay ra ang segundo nga
madaog. Ania ang han-ay nga tinuod nga mapuslanon.

<div class="grid cards" markdown>

- **Lakang 1 — intuitive nga F2L**

    [Pagsabot sa F2L](f2l.md). Walay algorithm. Dinhi ang kadaghanan sa daog, ug
    mahimong pipila ka semana ayha kini mahimong natural. Ayaw ni laktawi.

- **Lakang 2 — ang last layer sa 4 ka lakang**

    Ang [4LLL](4lll.md): **16 ka algorithm** imbes 78, para sa kompleto nga last
    layer. Mao kini ang tulay nga halos tanan moagi.

- **Lakang 3 — kompleto nga PLL**

    Ang [21 PLL](../advanced/pll.md). Ang PLL una sa OLL: mas gamay ang case, mas
    daghan ang segundo nga madaog matag algorithm nga tun-an.

- **Lakang 4 — kompleto nga OLL**

    Ang [57 OLL](../advanced/oll.md). Tun-an kini sa gagmay nga hugpong, sulod sa
    pipila ka bulan. Kini ang katapusang buhaton, dili ang una.

</div>

## Unsay paabuton

| Ang-ang | Aberids nga oras | Unsay imong nabatasan |
|---|---|---|
| Beginner nga pamaagi | 2 hangtod 3 min | ang 7 ka lakang |
| Hanas nga beginner | 1 min 30 | parehong lakang, dili na maghunahuna |
| Intuitive nga F2L | 45 hangtod 60 s | Cross + F2L + 4LLL |
| Kompleto nga CFOP | 20 hangtod 30 s | 78 ka algorithm, lookahead |

!!! tip "Ang ang-ang diin tanan mahunong"
    Sa taliwala sa 45 ug 30 ka segundo, dili na ang algorithm ang nagpugong,
    kondili ang **lookahead**: ang pagtan-aw sa sunod nga piraso samtang ang
    imong tudlo naghimo pa sa nauna. Tan-awa ang [Aron mas paspas](../speed.md).
