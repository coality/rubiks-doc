# -*- coding: utf-8 -*-
"""Resout des cubes melanges en suivant la methode debutant TELLE QUE LES PAGES
LA DECRIVENT, et verifie que le cube finit resolu.

Pourquoi ce fichier existe. Les controles precedents partaient de
`solved().apply(invert(alg))` et verifiaient qu'appliquer `alg` redonnait un cube
resolu : vrai PAR CONSTRUCTION pour n'importe quelle sequence. Ils ont donc
valide pendant des mois une etape 2 qui detruisait la croix blanche. Ici rien
n'est construit a partir des algorithmes : on part de melanges aleatoires et on
applique les consignes des pages, dans l'ordre, jusqu'au cube resolu ou l'echec.

Chaque etape est une fonction, et chacune verifie son propre objectif avant de
passer la main — un echec dit donc quelle etape ment.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from cube import Cube, solved, COLORS, FACES

# --- les algorithmes, exactement ceux des pages ----------------------------
INSERTION_COIN = "R U R' U'"              # etape 2, repetee 1, 3 ou 5 fois
COURONNE2_DROITE = "U R U' R' U' F' U F"  # etape 3
COURONNE2_GAUCHE = "U' L' U L U F U' F'"
CROIX_JAUNE = "F R U R' U' F'"            # etape 4
ARETES_JAUNES = "R U' R U R U R U' R' U' R2"   # etape 5
COINS_PLACES = "U R U' L' U R' U' L"      # etape 6
COIN_TOURNE = "R' D' R D"                 # etape 7, repetee 2 ou 4 fois

BLANC, JAUNE = COLORS['D'], COLORS['U']
LATERALES = ('F', 'R', 'B', 'L')
NRM = {'U': (0, 1, 0), 'D': (0, -1, 0), 'F': (0, 0, 1),
       'B': (0, 0, -1), 'R': (1, 0, 0), 'L': (-1, 0, 0)}


# --- outils ---------------------------------------------------------------
def pieces(c, n):
    """Positions des pieces a n autocollants (2 = aretes, 3 = coins)."""
    return [p for p in {k[0] for k in c.st} if sum(1 for v in p if v) == n]


def couleurs(c, pos):
    return frozenset(col for (p, _n), col in c.st.items() if p == pos)


def centre(c, face):
    return c.st[(NRM[face], NRM[face])]


def croix_blanche(c):
    fl = c.facelets()
    return (all(fl['D'][i] == BLANC for i in (1, 3, 5, 7))
            and all(fl[f][7] == fl[f][4] for f in LATERALES))


def couronne1(c):
    fl = c.facelets()
    return (all(x == BLANC for x in fl['D'])
            and all(fl[f][i] == fl[f][4] for f in LATERALES for i in (6, 7, 8)))


def couronne2(c):
    fl = c.facelets()
    return couronne1(c) and all(fl[f][i] == fl[f][4] for f in LATERALES for i in (3, 5))


def croix_jaune_faite(c):
    fl = c.facelets()
    return all(fl['U'][i] == JAUNE for i in (1, 3, 5, 7))


def aretes_jaunes_placees(c):
    fl = c.facelets()
    return croix_jaune_faite(c) and all(fl[f][1] == fl[f][4] for f in LATERALES)


def maison_coin(c, couls):
    """La position ou ce coin doit aller."""
    for pos in pieces(c, 3):
        attendu = {centre(c, f) for f in FACES
                   if all(a * b > 0 for a, b in zip(pos, NRM[f]) if b)}
        if attendu == set(couls):
            return pos
    return None


def coins_bas_places(c):
    return all(maison_coin(c, couleurs(c, p)) == p
               for p in pieces(c, 3) if p[1] == -1)


# --- etape 1 : la croix blanche, par la marguerite -------------------------
def petale(c, f):
    """L'arete du haut posee au-dessus de la face f est-elle un petale blanc ?"""
    pos = tuple(a + b for a, b in zip(NRM['U'], NRM[f]))
    return c.st[(pos, NRM['U'])] == BLANC


def petales(c):
    return sum(1 for f in LATERALES if petale(c, f))


def arete_bas_bonne(c, f):
    pos = tuple(a + b for a, b in zip(NRM['D'], NRM[f]))
    return c.st[(pos, NRM['D'])] == BLANC and c.st[(pos, NRM[f])] == centre(c, f)


def aretes_croix_ok(c):
    """Les aretes blanches deja posees, qu'il ne faut plus deranger."""
    return {f for f in LATERALES if arete_bas_bonne(c, f)}


def monte_petale(c, journal):
    """Amene une arete blanche encore mal placee dans la marguerite, sans
    deranger celles qui sont deja descendues. Recherche en profondeur
    croissante : c'est ce que fait le lecteur a tatons, en plus systematique."""
    protege = aretes_croix_ok(c)

    def but(d):
        return (petales(d) > petales(c)
                and aretes_croix_ok(d) >= protege)

    pile = [(c, [])]
    for prof in range(1, 5):
        pile = [(c, [])]
        while pile:
            d, hist = pile.pop()
            if len(hist) == prof:
                if but(d):
                    for m in hist:
                        c.apply(m); journal.append(m)
                    return True
                continue
            for m in GEN:
                if hist and m[0] == hist[-1][0]:
                    continue
                pile.append((d.copy().apply(m), hist + [m]))
    return False


def etape1(c, journal):
    """Marguerite puis descente des petales, comme la page l'explique."""
    for _ in range(12):
        if croix_blanche(c):
            return True
        # un petale aligne sur son centre descend d'un demi-tour
        descendu = False
        for f in LATERALES:
            pos = tuple(a + b for a, b in zip(NRM['U'], NRM[f]))
            if (petale(c, f) and c.st[(pos, NRM[f])] == centre(c, f)
                    and not arete_bas_bonne(c, f)):
                c.apply(f + '2'); journal.append(f + '2')
                descendu = True
                break
        if descendu:
            continue
        # sinon on tourne U pour aligner un petale...
        aligne = False
        for _ in range(4):
            c.apply('U'); journal.append('U')
            if any(petale(c, f) and not arete_bas_bonne(c, f)
                   and c.st[(tuple(a + b for a, b in zip(NRM['U'], NRM[f])), NRM[f])]
                   == centre(c, f) for f in LATERALES):
                aligne = True
                break
        if aligne:
            continue
        # ... ou on va chercher une arete blanche ailleurs
        if not monte_petale(c, journal):
            return False
    return croix_blanche(c)


# --- etape 2 : les coins blancs -------------------------------------------
REPETITIONS = {'R': 1, 'U': 3, 'F': 5}      # ou pointe le blanc -> combien de fois


def etape2(c, journal):
    for _ in range(40):
        if couronne1(c):
            break
        hauts = [p for p in pieces(c, 3) if p[1] == 1 and BLANC in couleurs(c, p)]
        if not hauts:
            # coin blanc coince en bas, mal place : on l'ejecte
            # un coin peut etre dans la bonne fente mais RETOURNE : il faut
            # l'ejecter lui aussi, sinon la couronne ne se termine jamais
            mal = [p for p in pieces(c, 3) if p[1] == -1 and BLANC in couleurs(c, p)
                   and (maison_coin(c, couleurs(c, p)) != p
                        or c.st[(p, NRM['D'])] != BLANC)]
            if not mal:
                break
            couls = couleurs(c, mal[0])
            while [p for p in pieces(c, 3) if couleurs(c, p) == couls][0] != (1, -1, 1):
                c.apply('y'); journal.append('y')
            c.apply(INSERTION_COIN); journal.append(INSERTION_COIN)
            continue
        couls = couleurs(c, hauts[0])
        cible = maison_coin(c, couls)
        ici = lambda: [p for p in pieces(c, 3) if couleurs(c, p) == couls][0]
        for _ in range(4):                       # U pour l'amener au-dessus
            p = ici()
            if (p[0], p[2]) == (cible[0], cible[2]):
                break
            c.apply('U'); journal.append('U')
        for _ in range(4):                       # le cube en main, coin devant-droite
            if ici() == (1, 1, 1):
                break
            c.apply('y'); journal.append('y')
            cible = maison_coin(c, couls)
        face = next(f for f in ('R', 'U', 'F') if c.st[((1, 1, 1), NRM[f])] == BLANC)
        k = REPETITIONS[face]
        c.apply(' '.join([INSERTION_COIN] * k))
        journal.append('(%s) x%d' % (INSERTION_COIN, k))
    return couronne1(c)


# --- etape 3 : la deuxieme couronne ---------------------------------------
def etape3(c, journal):
    for _ in range(40):
        if couronne2(c):
            break
        # une arete du haut sans jaune ?
        cands = [p for p in pieces(c, 2) if p[1] == 1 and JAUNE not in couleurs(c, p)]
        if cands:
            couls = couleurs(c, cands[0])
            ici = lambda: [p for p in pieces(c, 2) if couleurs(c, p) == couls][0]
            place = False
            for _ in range(4):
                p = ici()
                f = next((f for f in LATERALES
                          if p == tuple(a + b for a, b in zip(NRM['U'], NRM[f]))), None)
                if f and c.st[(p, NRM[f])] == centre(c, f):
                    place = True
                    break
                c.apply('U'); journal.append('U')
            if not place:
                c.apply('U'); journal.append('U')
                continue
            while True:                           # amener ce T devant
                p = ici()
                if p == (0, 1, 1):
                    break
                c.apply('y'); journal.append('y')
            dessus = c.st[((0, 1, 1), NRM['U'])]
            alg = COURONNE2_DROITE if dessus == centre(c, 'R') else COURONNE2_GAUCHE
            c.apply(alg); journal.append(alg)
            continue
        # sinon : ejecter une arete etrangere de la deuxieme couronne
        intrus = [p for p in pieces(c, 2) if p[1] == 0
                  and any(c.st[(p, n)] != c.st[(NRM[f], NRM[f])]
                          for f, n in NRM.items() if (p, n) in c.st)]
        if not intrus:
            break
        while (1, 0, 1) not in intrus:
            c.apply('y'); journal.append('y')
            intrus = [p for p in pieces(c, 2) if p[1] == 0
                      and any(c.st[(p, n)] != c.st[(NRM[f], NRM[f])]
                              for f, n in NRM.items() if (p, n) in c.st)]
        c.apply(COURONNE2_DROITE); journal.append(COURONNE2_DROITE)
    return couronne2(c)


# --- etape 4 : la croix jaune ---------------------------------------------
ARETES_HAUT = {'F': (0, 1, 1), 'R': (1, 1, 0), 'B': (0, 1, -1), 'L': (-1, 1, 0)}


def forme_jaune(c):
    """0 point, 1 equerre, 2 barre, 3 croix — la progression de la page."""
    jaunes = [f for f, p in ARETES_HAUT.items() if c.st[(p, NRM['U'])] == JAUNE]
    if len(jaunes) == 4:
        return 3
    if len(jaunes) == 0:
        return 0
    if len(jaunes) != 2:
        return 0
    a, b = (ARETES_HAUT[f] for f in jaunes)
    return 2 if a == tuple(-v for v in b) else 1     # opposees = barre


def etape4(c, journal):
    """Point -> equerre -> barre -> croix. On cherche l'enchainement le plus
    court de « oriente le cube avec U, puis applique la sequence » : c'est
    exactement ce que fait le lecteur qui tourne son cube jusqu'a reconnaitre
    son cas, sans qu'on ait a coder la reconnaissance a la main."""
    if croix_jaune_faite(c):
        return True
    for rondes in range(1, 5):
        pile = [([], c)]
        for _ in range(rondes):
            suite = []
            for hist, d in pile:
                for auf in range(4):
                    e = d.copy()
                    if auf:
                        e.apply(' '.join(['U'] * auf))
                    e.apply(CROIX_JAUNE)
                    suite.append((hist + [auf], e))
            pile = suite
        for hist, d in pile:
            if croix_jaune_faite(d):
                for auf in hist:
                    if auf:
                        c.apply(' '.join(['U'] * auf)); journal.append('U x%d' % auf)
                    c.apply(CROIX_JAUNE); journal.append(CROIX_JAUNE)
                return True
    return False


# --- etape 5 : placer les aretes jaunes ------------------------------------
def etape5(c, journal):
    for _ in range(16):
        if aretes_jaunes_placees(c):
            break
        meilleur, coup = None, None
        for auf in range(4):
            for rot in range(4):
                d = c.copy()
                if auf:
                    d.apply(' '.join(['U'] * auf))
                if rot:
                    d.apply(' '.join(['y'] * rot))
                d.apply(ARETES_JAUNES)
                fl = d.facelets()
                score = sum(1 for f in LATERALES if fl[f][1] == fl[f][4])
                if meilleur is None or score > meilleur:
                    meilleur, coup = score, (auf, rot)
        auf, rot = coup
        if auf:
            c.apply(' '.join(['U'] * auf)); journal.append('U x%d' % auf)
        if rot:
            c.apply(' '.join(['y'] * rot)); journal.append('y x%d' % rot)
        c.apply(ARETES_JAUNES); journal.append(ARETES_JAUNES)
    return aretes_jaunes_placees(c)


# --- etape 6 : placer les coins jaunes -------------------------------------
def coins_hauts_places(c):
    return all(maison_coin(c, couleurs(c, p)) == p for p in pieces(c, 3) if p[1] == 1)


def etape6(c, journal):
    for _ in range(16):
        if coins_hauts_places(c):
            break
        bons = [p for p in pieces(c, 3) if p[1] == 1 and maison_coin(c, couleurs(c, p)) == p]
        if bons:
            couls = couleurs(c, bons[0])
            while [p for p in pieces(c, 3) if couleurs(c, p) == couls][0] != (1, 1, 1):
                c.apply('y'); journal.append('y')
        c.apply(COINS_PLACES); journal.append(COINS_PLACES)
    return coins_hauts_places(c)


# --- etape 7 : orienter les coins jaunes -----------------------------------
def etape7(c, journal):
    for _ in range(4):
        for _ in range(6):
            if c.st[((1, 1, 1), NRM['U'])] == JAUNE:
                break
            c.apply(COIN_TOURNE); journal.append(COIN_TOURNE)
        c.apply('U'); journal.append('U')
    for _ in range(4):
        if c.is_solved():
            break
        c.apply('U'); journal.append('U')
    return c.is_solved()


ETAPES = [('1 croix blanche', etape1), ('2 coins blancs', etape2),
          ('3 deuxieme couronne', etape3), ('4 croix jaune', etape4),
          ('5 aretes jaunes', etape5), ('6 coins places', etape6),
          ('7 coins orientes', etape7)]

GEN = [m + s for m in 'RUFLBD' for s in ('', "'", '2')]


def melange(graine, n=25):
    x, out = graine, []
    for _ in range(n):
        x = (1103515245 * x + 12345) % (1 << 31)
        out.append(GEN[x % len(GEN)])
    return ' '.join(out)


def resout(graine):
    c = solved().apply(melange(graine))
    journal = []
    for nom, fn in ETAPES:
        if not fn(c, journal):
            return False, nom, journal
    return c.is_solved(), None, journal


def main(n=200):
    echecs = []
    longueurs = []
    for g in range(1, n + 1):
        ok, etape, journal = resout(g)
        if ok:
            longueurs.append(sum(len(x.split()) for x in journal))
        else:
            echecs.append((g, etape))
    if echecs:
        print('METHODE : %d ECHEC(S) sur %d melanges' % (len(echecs), n))
        for g, etape in echecs[:10]:
            print('  melange %d : bloque a l\'etape %s' % (g, etape))
        sys.exit(1)
    print('methode debutant : %d melanges aleatoires resolus de bout en bout '
          '(%d mouvements en moyenne)' % (n, sum(longueurs) // len(longueurs)))


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)
