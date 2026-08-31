# Ang last layer sa 4 ka lakang

Ang kompleto nga CFOP nagkinahanglan og 78 ka algorithm. Ang **4LLL** (*4-Look
Last Layer*) maghimo sa parehong trabaho gamit ang **16**, pinaagi sa pagbahin sa
matag lakang sa duha.

Mao kini ang tulay nga halos tanan nga cuber moagi, ug daghan ang dugay kaayo nga
nagpabilin dinhi: kung maayo ang pagbuhat, igo na kini aron mapaubos sa usa ka
minuto.

| Lakang | Unsay buhaton | Case |
|---|---|---|
| 1 | I-orient ang edge → ang dalag nga cross | 3 |
| 2 | I-orient ang corner → ang dalag nga face | 7 |
| 3 | I-permute ang corner | 3 |
| 4 | I-permute ang edge | 4 |

Kabalo na ka sa lakang 1: mao ni ang [lakang 4](../beginner/4-yellow-cross.md) sa
beginner nga pamaagi, wala mausab.

---

## Lakang 1 — i-orient ang edge

<div class="fiche" markdown>
<div class="corps" markdown>
<span class="move">F R U R' U' F'</span>
<p>Dot → L → bar → cross. Tan-awa ang
<a href="../../beginner/4-yellow-cross/">lakang 4</a> para sa posisyon sa cube sa
matag case.</p>
</div>
</div>

<figure class="film">
<img src="/bis/assets/cubes/film-croix-jaune.svg" alt="F R U R' U' F' — ang sequence, matag lihok">
<figcaption><code>F R U R' U' F'</code> — ang sequence, matag lihok</figcaption>
</figure>

<div class="algs">
<figure class="alg"><img src="/bis/assets/cubes/eo-point.svg" alt="Ang dot"><figcaption><b>Ang dot</b><br><code>3 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/eo-equerre.svg" alt="Ang L"><figcaption><b>Ang L</b><br><code>2 ka beses</code></figcaption></figure>
<figure class="alg"><img src="/bis/assets/cubes/eo-barre.svg" alt="Ang bar"><figcaption><b>Ang bar</b><br><code>1 ka beses</code></figcaption></figure>
</div>

---

## Lakang 2 — i-orient ang corner

Pito ka case. Mao gyud kini ang pito ka OLL diin human na ang cross, busa
**walay tun-an pag-usab** sa adlaw nga mobalhin ka sa kompleto nga OLL.

<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-27.svg" alt="Sune" loading="lazy">
<div class="titre"><b>Sune</b><br><code>R U R' U R U2 R'</code></div>
<img class="film" src="/bis/assets/cubes/film-sune.svg" alt="R U R' U R U2 R' — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-26.svg" alt="Anti-Sune" loading="lazy">
<div class="titre"><b>Anti-Sune</b><br><code>R U2 R' U' R U' R'</code></div>
<img class="film" src="/bis/assets/cubes/film-antisune.svg" alt="R U2 R' U' R U' R' — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-21.svg" alt="Double Sune" loading="lazy">
<div class="titre"><b>Double Sune</b><br><code>R U2 R' U' R U R' U' R U' R'</code></div>
<img class="film" src="/bis/assets/cubes/film-double-sune.svg" alt="R U2 R' U' R U R' U' R U' R' — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-22.svg" alt="Pi" loading="lazy">
<div class="titre"><b>Pi</b><br><code>R U2 R2 U' R2 U' R2 U2 R</code></div>
<img class="film" src="/bis/assets/cubes/film-pi.svg" alt="R U2 R2 U' R2 U' R2 U2 R — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-23.svg" alt="Headlights" loading="lazy">
<div class="titre"><b>Headlights</b><br><code>R2 D' R U2 R' D R U2 R</code></div>
<img class="film" src="/bis/assets/cubes/film-tete.svg" alt="R2 D' R U2 R' D R U2 R — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-24.svg" alt="Sock" loading="lazy">
<div class="titre"><b>Sock</b><br><code>r U R' U' r' F R F'</code></div>
<img class="film" src="/bis/assets/cubes/film-chaussette.svg" alt="r U R' U' r' F R F' — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/oll-25.svg" alt="Bowtie" loading="lazy">
<div class="titre"><b>Bowtie</b><br><code>F' r U R' U' r' F R</code></div>
<img class="film" src="/bis/assets/cubes/film-noeud-papillon.svg" alt="F' r U R' U' r' F R — ang sequence, matag lihok" loading="lazy">
</div>

!!! tip "Sugdi niining duha"
    Ang **Sune** ug ang **Anti-Sune** mirror sa usag usa, ug silang duha ra
    naglangkob sa dako nga bahin sa mga case. Ang laing lima mahimo usab tanan
    masulbad pinaagi sa pagbuhat sa Sune og kaduha — mas hinay, apan makatabang
    samtang gitun-an pa nimo sila.

---

## Lakang 3 — i-permute ang corner

Tulo ka case. Ilha ang **pares nga managsamang kolor** sa kilid (ang
"headlights"): ang face nga adunay pares mao ang face nga husto na ang lugar sa
iyang corner.

<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-aa.svg" alt="A-perm a" loading="lazy">
<div class="titre"><b>A-perm a</b><br><code>x R' U R' D2 R U' R' D2 R2</code></div>
<img class="film" src="/bis/assets/cubes/film-aperm-a.svg" alt="x R' U R' D2 R U' R' D2 R2 — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-ab.svg" alt="A-perm b" loading="lazy">
<div class="titre"><b>A-perm b</b><br><code>x R2 D2 R U R' D2 R U' R</code></div>
<img class="film" src="/bis/assets/cubes/film-aperm-b.svg" alt="x R2 D2 R U R' D2 R U' R — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-e.svg" alt="E-perm" loading="lazy">
<div class="titre"><b>E-perm</b><br><code>x' R U' R' D R U R' D' R U R' D R U' R' D'</code></div>
<img class="film" src="/bis/assets/cubes/film-eperm.svg" alt="x' R U' R' D R U R' D' R U R' D R U' R' D' — ang sequence, matag lihok" loading="lazy">
</div>

!!! info "Ang A-perm magtuyok sa cube"
    Ang `x` sa sinugdanan usa ka rotation sa tibuok cube: itikig nimo ang cube
    paluyo sa dili pa magbuhat, ug lahi ang imong pagkupot sa katapusan. Normal
    ra kana.

---

## Lakang 4 — i-permute ang edge

Upat ka case, ug kini ang pinakamaayong algorithm sa cube: mubo, paspas, ug
nagsukad sa `M` nga slice.

<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-ua.svg" alt="U-perm a" loading="lazy">
<div class="titre"><b>U-perm a</b><br><code>M2 U M U2 M' U M2</code></div>
<img class="film" src="/bis/assets/cubes/film-uperm-a.svg" alt="M2 U M U2 M' U M2 — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-ub.svg" alt="U-perm b" loading="lazy">
<div class="titre"><b>U-perm b</b><br><code>M2 U' M U2 M' U' M2</code></div>
<img class="film" src="/bis/assets/cubes/film-uperm-b.svg" alt="M2 U' M U2 M' U' M2 — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-h.svg" alt="H-perm" loading="lazy">
<div class="titre"><b>H-perm</b><br><code>M2 U M2 U2 M2 U M2</code></div>
<img class="film" src="/bis/assets/cubes/film-hperm.svg" alt="M2 U M2 U2 M2 U M2 — ang sequence, matag lihok" loading="lazy">
</div>
<div class="cas">
<img class="etat" src="/bis/assets/cubes/pll-z.svg" alt="Z-perm" loading="lazy">
<div class="titre"><b>Z-perm</b><br><code>M' U M2 U M2 U M' U2 M2</code></div>
<img class="film" src="/bis/assets/cubes/film-zperm.svg" alt="M' U M2 U M2 U M' U2 M2 — ang sequence, matag lihok" loading="lazy">
</div>

!!! tip "Kining upat ang una nga tun-an"
    Mubo sila, kanunay sila motungha, ug apil sila sa kompleto nga 21 PLL. Walay
    nausik nga paningkamot.

---

## Ug unya

Kung hanas na ka sa 4LLL, ang lohikal nga sunod mao ang
[kompleto nga PLL](../advanced/pll.md): ilisan nimo ang lakang 3 ug 4 og usa ra
ka algorithm. Kabalo na ka sa 7 sa 21.

Ang [kompleto nga OLL](../advanced/oll.md) mao ang katapusan: iyang ilisan ang
lakang 1 ug 2, ug kabalo na ka sa 7 sa 57.
