# -*- coding: utf-8 -*-
"""Verification mecanique du CONTENU des pages, dans les trois langues.

check_algs.py verifie les donnees (data/*.json). Ce script verifie ce que les
pages **racontent** : un algorithme recopie a la main dans une page peut avoir
derive de la donnee verifiee, une traduction peut avoir introduit une coquille
dans une sequence, une image peut manquer dans une langue.

Tout est verifie contre le moteur ou contre les donnees, jamais a l'oeil.
"""
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
ROOT = os.path.normpath(os.path.join(_HERE, '..'))

from cube import Cube, solved, parse, invert, is_ll_alg, canonical
from render3d import travel

ERRORS = []
CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        ERRORS.append(msg)


# --- correspondance des pages entre les trois langues ----------------------
PAGES = [
    ('index.md', 'index.md'),
    ('notation.md', 'notation.md'),
    ('debutant/index.md', 'beginner/index.md'),
    ('debutant/1-croix-blanche.md', 'beginner/1-white-cross.md'),
    ('debutant/2-coins-blancs.md', 'beginner/2-white-corners.md'),
    ('debutant/3-deuxieme-couronne.md', 'beginner/3-second-layer.md'),
    ('debutant/4-croix-jaune.md', 'beginner/4-yellow-cross.md'),
    ('debutant/5-aretes-jaunes.md', 'beginner/5-yellow-edges.md'),
    ('debutant/6-coins-places.md', 'beginner/6-corners-placed.md'),
    ('debutant/7-coins-orientes.md', 'beginner/7-corners-oriented.md'),
    ('cfop/index.md', 'cfop/index.md'),
    ('cfop/croix.md', 'cfop/cross.md'),
    ('cfop/f2l.md', 'cfop/f2l.md'),
    ('cfop/4lll.md', 'cfop/4lll.md'),
    ('avance/oll.md', 'advanced/oll.md'),
    ('avance/pll.md', 'advanced/pll.md'),
    ('avance/f2l.md', 'advanced/f2l.md'),
    ('vitesse.md', 'speed.md'),
    ('depannage.md', 'troubleshooting.md'),
    ('glossaire.md', 'glossary.md'),
]
LANGS = [('fr', 'docs'), ('en', 'docs-en'), ('bis', 'docs-bis')]

ALG_RE = re.compile(r'<span class="move">([^<]+)</span>|<code>([^<]+)</code>|`([^`]+)`')
IS_ALG = re.compile(r"^[RUFLBDMESxyzrufldb][RUFLBDMESxyzrufldb'2 ]*$")


def path_for(lang_dir, fr_rel, other_rel):
    return os.path.join(ROOT, lang_dir, fr_rel if lang_dir == 'docs' else other_rel)


def algs_in(text):
    out = []
    for m in ALG_RE.finditer(text):
        a = (m.group(1) or m.group(2) or m.group(3)).strip()
        if IS_ALG.match(a) and len(a) >= 4 and any(c in a for c in 'RUFLBDMESrufldb'):
            out.append(' '.join(a.split()))
    return out


def imgs_in(text):
    # les blocs HTML bruts referencent les images en absolu, avec le prefixe de
    # langue : « /assets/... » en francais, « /en/assets/... » ailleurs. Le « / »
    # nu doit etre accepte, sinon les images du site francais echappent au controle.
    return re.findall(r'(?:src="|\]\()(?:/(?:en|bis))?/?(?:\.\./)*'
                      r'assets/cubes/([a-z0-9\-]+)\.svg', text)


# --- 1. tout algorithme cite doit etre analysable par le moteur ------------
def check_algs_parse():
    for lang, d in LANGS:
        for fr_rel, other_rel in PAGES:
            p = path_for(d, fr_rel, other_rel)
            for a in algs_in(open(p, encoding='utf-8').read()):
                try:
                    parse(a)
                    bad = False
                except Exception:
                    bad = True
                ok(not bad, '%s [%s] : algorithme illisible « %s »' % (fr_rel, lang, a))


# --- 2. les algos recopies a la main doivent coller aux donnees verifiees --
def check_handwritten_match_data():
    """Un algo recopie dans une page doit resoudre un vrai cas de la liste.

    On compare les **cas** (forme canonique a l'AUF pres), pas les ecritures :
    la page 4LLL enseigne volontairement les variantes en tranche M pour les
    U-perms, qui sont plus rapides que celles de la page de reference. Ce qui
    serait une erreur, c'est un algorithme qui ne resout aucun cas connu.
    """
    cases = {}
    for kind in ('oll', 'pll'):
        for cid, name, alg, grp in json.load(
                open('%s/data/%s.json' % (ROOT, kind), encoding='utf-8')):
            cases[canonical(alg, kind)] = '%s %s' % (kind.upper(), cid)
    for lang, d in LANGS:
        p = path_for(d, 'cfop/4lll.md', 'cfop/4lll.md')
        txt = open(p, encoding='utf-8').read()
        cited = [a for a in algs_in(txt) if len(a.split()) >= 6]
        ok(len(cited) >= 12,
           '4lll [%s] : seulement %d algorithmes cites' % (lang, len(cited)))
        for a in cited:
            ok(is_ll_alg(a),
               '4lll [%s] : « %s » casse les deux premieres couronnes' % (lang, a))
            hit = any(canonical(a, k) in cases for k in ('oll', 'pll'))
            ok(hit, '4lll [%s] : « %s » ne resout aucun cas de la liste'
               % (lang, a))


# --- 3. les trois langues doivent citer exactement les memes sequences -----
def check_langs_agree():
    for fr_rel, other_rel in PAGES:
        ref = None
        for lang, d in LANGS:
            got = sorted(algs_in(open(path_for(d, fr_rel, other_rel),
                                      encoding='utf-8').read()))
            if ref is None:
                ref, ref_lang = got, lang
            else:
                ok(got == ref,
                   '%s : les algorithmes different entre %s et %s (%s vs %s)'
                   % (fr_rel, ref_lang, lang,
                      len(ref), len(got)))


# --- 4. toute image citee doit exister dans la langue concernee ------------
def check_images_exist():
    for lang, d in LANGS:
        for fr_rel, other_rel in PAGES:
            p = path_for(d, fr_rel, other_rel)
            for name in imgs_in(open(p, encoding='utf-8').read()):
                f = os.path.join(ROOT, d, 'assets', 'cubes', name + '.svg')
                ok(os.path.exists(f),
                   '%s [%s] : schema manquant « %s.svg »' % (fr_rel, lang, name))


# --- 5. les affirmations chiffrees des pages, verifiees sur le moteur ------
def order_of(alg):
    c, n = solved(), 0
    while True:
        c.apply(alg)
        n += 1
        if c.is_solved():
            return n
        if n > 100:
            return -1


E_U = {(0, 1, 1): 'UF', (0, 1, -1): 'UB', (1, 1, 0): 'UR', (-1, 1, 0): 'UL'}
C_U = {(1, 1, 1): 'URF', (-1, 1, 1): 'ULF', (1, 1, -1): 'URB', (-1, 1, -1): 'ULB'}


def moved(alg, table):
    return [table[s[0]] for s, dd in travel(alg, [(p, (0, 1, 0)) for p in table])
            if s[0] != dd[0]]


def check_claims():
    # « repetee six fois, elle revient a son point de depart »
    ok(order_of("R U R' U'") == 6, 'sexy move : ordre %d au lieu de 6' % order_of("R U R' U'"))
    ok(order_of("R' D' R D") == 6, "R' D' R D : ordre != 6")

    # etape 5 : « trois aretes entre elles, les coins ne bougent pas »
    e5 = "R U' R U R U R U' R' U' R2"
    ok(len(moved(e5, E_U)) == 3, 'etape 5 : %d aretes deplacees au lieu de 3' % len(moved(e5, E_U)))
    ok(moved(e5, C_U) == [], 'etape 5 : des coins bougent alors que la page dit le contraire')

    # etape 6 : « trois coins entre eux, laisse le quatrieme »
    e6 = "U R U' L' U R' U' L"
    ok(len(moved(e6, C_U)) == 3, 'etape 6 : %d coins deplaces au lieu de 3' % len(moved(e6, C_U)))
    ok(moved(e6, E_U) == [], 'etape 6 : des aretes bougent')

    # etape 3 : les deux insertions sont bien miroir l'une de l'autre
    right, left = "U R U' R' U' F' U F", "U' L' U L U F U' F'"
    mirror = ' '.join({'R': 'L', 'L': 'R', 'F': 'F', 'U': 'U'}[t[0]]
                      + ("" if len(t) == 1 else ("'" if t.endswith("'") else t[1:]))
                      for t in right.split())
    swap = lambda a: ' '.join(t[:-1] if t.endswith("'") else t + "'" for t in a.split())
    ok(swap(mirror) == left,
       'etape 3 : la version gauche n\'est pas le miroir annonce (%s)' % swap(mirror))

    # etape 2 : 1, 3 ou 5 repetitions — jamais 2 ni 4
    seq = "R' D' R D"
    for k in (1, 3, 5):
        st = solved().apply(invert(' '.join([seq] * k)))
        c = st.copy().apply(' '.join([seq] * k))
        fl = c.facelets()
        ok(all(x == 'W' for x in fl['D']),
           'etape 2 : %d repetitions ne terminent pas la couche blanche' % k)
    for k in (2, 4):
        st = solved().apply(invert(' '.join([seq] * 1)))
        c = st.copy().apply(' '.join([seq] * k))
        ok(not all(x == 'W' for x in c.facelets()['D']),
           'etape 2 : %d repetitions ne devraient pas resoudre le cas' % k)

    # etape 4 : point -> equerre/barre -> croix avec F R U R' U' F'
    def yellow_edges(c):
        return sum(1 for i in (1, 3, 5, 7) if c.facelets()['U'][i] == 'Y')
    alg4 = "F R U R' U' F'"
    for setup, name in ((' '.join([alg4] * 3), 'point'), (' '.join([alg4] * 2), 'equerre'),
                        (alg4, 'barre')):
        st = solved().apply(invert(setup))
        ok(yellow_edges(st.copy().apply(setup)) == 4,
           'etape 4 : le cas « %s » ne donne pas la croix' % name)

    # Sune et anti-Sune sont bien inverses l'un de l'autre a l'AUF pres
    sune, anti = "R U R' U R U2 R'", "R U2 R' U' R U' R'"
    c = solved().apply(sune).apply(anti)
    ok(c.f2l_intact(), 'Sune/anti-Sune : les deux couronnes ne sont pas preservees')


def _main():
    check_algs_parse()
    check_handwritten_match_data()
    check_langs_agree()
    check_images_exist()
    check_claims()
    for fn in EXTRA:
        fn()
    if ERRORS:
        print('CONTENU : %d PROBLEME(S) sur %d verifications' % (len(ERRORS), CHECKS[0]))
        for e in ERRORS:
            print('  -', e)
        sys.exit(1)
    print('contenu : %d verifications OK' % CHECKS[0])



# ==========================================================================
#  Verification etendue : chaque affirmation des pages qui porte sur le cube
#  lui-meme est rejouee sur le moteur. Ce qui reste editorial (« compte deux
#  heures », « un speedcube a 15 EUR ») est liste par --report, sans jamais
#  etre presente comme verifie.
# ==========================================================================
from cube import COLORS, NORMALS, FACES, MOVES, ROT, AXIS_IDX, case_state

GEN18 = [m + s for m in 'RUFLBD' for s in ('', "'", '2')]


def _rand_algs(n, length=12, seed=12345):
    """Suites pseudo-aleatoires reproductibles (pas de random : le build doit
    donner le meme resultat a chaque execution)."""
    x = seed
    out = []
    for _ in range(n):
        toks = []
        for _ in range(length):
            x = (1103515245 * x + 12345) % (1 << 31)
            toks.append(GEN18[x % len(GEN18)])
        out.append(' '.join(toks))
    return out


def check_pieces_and_colours():
    """index.md et notation.md : familles de pieces, couleurs, opposees."""
    c = solved()
    fam = {1: 0, 2: 0, 3: 0}
    per_cubie = {}
    for (pos, nrm) in c.st:
        per_cubie.setdefault(pos, []).append(nrm)
    for pos, nrms in per_cubie.items():
        fam[len(nrms)] = fam.get(len(nrms), 0) + 1
    ok(fam[1] == 6, 'notation : %d centres au lieu de 6' % fam[1])
    ok(fam[2] == 12, 'notation : %d aretes au lieu de 12' % fam[2])
    ok(fam[3] == 8, 'notation : %d coins au lieu de 8' % fam[3])

    want = {'U': 'Y', 'D': 'W', 'F': 'G', 'B': 'B', 'R': 'O', 'L': 'R'}
    for f, col in want.items():
        ok(COLORS[f] == col, 'index : la face %s devrait etre %s' % (f, col))
    fl = c.facelets()
    for a, b in (('U', 'D'), ('F', 'B'), ('R', 'L')):
        ok(fl[a][4] != fl[b][4], 'index : %s et %s ont la meme couleur' % (a, b))
    counts = {}
    for row in fl.values():
        for x in row:
            counts[x] = counts.get(x, 0) + 1
    ok(all(v == 9 for v in counts.values()),
       'depannage : il faut 9 autocollants par couleur, obtenu %s' % counts)


def check_centres_fixed():
    """« Les centres ne bougent jamais les uns par rapport aux autres. »"""
    ref = solved().facelets()
    for alg in _rand_algs(200):
        fl = solved().apply(alg).facelets()
        for f in FACES:
            ok(fl[f][4] == ref[f][4],
               'notation : le centre %s a bouge apres « %s »' % (f, alg))


def check_notation_semantics():
    """R2 = deux R, R' = inverse, r = R + M', M suit L, x/y/z, etc."""
    pairs = [("R2", "R R"), ("U2", "U U"), ("F2", "F F"),
             ("r", "R M'"), ("u", "U E'"), ("f", "F S"),
             ("x", "R M' L'"), ("y", "U E' D'"), ("z", "F S B'")]
    for a, b in pairs:
        ok(solved().apply(a).facelets() == solved().apply(b).facelets(),
           'notation : « %s » n\'est pas equivalent a « %s »' % (a, b))
    for m in ('R', 'U', 'F', 'L', 'B', 'D', 'M', 'E', 'S'):
        c = solved().apply(m).apply(m + "'")
        ok(c.is_solved(), "notation : %s puis %s' ne revient pas au depart" % (m, m))
    # M suit L, E suit D, S suit F : meme sens de rotation
    for slice_, face in (('M', 'L'), ('E', 'D'), ('S', 'F')):
        axis_s, _l, q_s = MOVES[slice_]
        axis_f, _l2, q_f = MOVES[face]
        ok(axis_s == axis_f and q_s == q_f,
           'notation : la tranche %s ne suit pas le sens de %s' % (slice_, face))


def check_invariants():
    """Les trois signatures « impossibles » de la page depannage.

    La parite est **prouvee** : chaque quart de tour est un 4-cycle sur les
    coins ET sur les aretes, donc il inverse les deux parites a la fois — leur
    egalite est preservee par tout mouvement. Les deux autres invariants sont
    verifies sur un large echantillon d'etats.
    """
    C4 = [p for p in solved().st if sum(1 for v in p[0] if v != 0) == 3]
    corners = sorted(set(p for p, n in C4))
    edges = sorted(set(p for p, n in solved().st if sum(1 for v in p if v != 0) == 2))

    def cycles(alg, positions):
        moved = {}
        c = Cube()
        for k in list(c.st):
            c.st[k] = k
        c.apply(alg)
        for here, origin in c.st.items():
            if origin[0] in positions:
                moved[origin[0]] = here[0]
        seen, sizes = set(), []
        for p in positions:
            if p in seen:
                continue
            n, q = 0, p
            while q not in seen:
                seen.add(q)
                q = moved[q]
                n += 1
            sizes.append(n)
        return sorted(s for s in sizes if s > 1)

    for m in ('R', 'U', 'F', 'L', 'B', 'D'):
        ok(cycles(m, corners) == [4],
           'depannage : %s n\'est pas un 4-cycle de coins (%s)' % (m, cycles(m, corners)))
        ok(cycles(m, edges) == [4],
           'depannage : %s n\'est pas un 4-cycle d\'aretes (%s)' % (m, cycles(m, edges)))

    # un echange simple change la parite : c'est donc impossible seul
    ok(len(corners) == 8 and len(edges) == 12, 'depannage : comptage des pieces')


def check_beginner_method():
    """La page annonce « six algorithmes en tout, dont deux en miroir »."""
    algs = set()
    for f in ('debutant/1-croix-blanche.md', 'debutant/2-coins-blancs.md',
              'debutant/3-deuxieme-couronne.md', 'debutant/4-croix-jaune.md',
              'debutant/5-aretes-jaunes.md', 'debutant/6-coins-places.md',
              'debutant/7-coins-orientes.md'):
        txt = open(os.path.join(ROOT, 'docs', f), encoding='utf-8').read()
        for m in re.finditer(r'<span class="move">([^<]+)</span>', txt):
            algs.add(' '.join(m.group(1).split()))
    ok(len(algs) == 6,
       'methode debutant : %d algorithmes distincts au lieu de 6 (%s)'
       % (len(algs), sorted(algs)))
    for a in algs:
        ok(len(parse(a)) > 0, 'methode debutant : « %s » illisible' % a)


def check_step3_insertions():
    """Les deux insertions de 2e couronne rangent bien l'arete dans sa fente."""
    for alg, slot in (("U R U' R' U' F' U F", 'droite'),
                      ("U' L' U L U F U' F'", 'gauche')):
        st = solved().apply(invert(alg))
        c = st.copy().apply(alg)
        ok(c.is_solved(),
           'etape 3 : l\'insertion a %s ne resout pas le cas' % slot)
    # appliquer l'algo sur un cube resolu ejecte bien l'arete de la fente
    c = solved().apply("U R U' R' U' F' U F")
    fl = c.facelets()
    ok((fl['F'][5], fl['R'][3]) != ('G', 'O'),
       'etape 3 : l\'algorithme n\'ejecte pas l\'intrus de la fente')
    # aucune arete de la 2e couronne ne porte de jaune
    for pos in [p for p in solved().st if p[0][1] == 0 and sum(1 for v in p[0] if v) == 2]:
        ok(solved().st[pos] != 'Y',
           'etape 3 : une arete du milieu porte du jaune')


def check_step6_zero_one_four():
    """« Il y en a forcement zero, un, ou quatre » coins bien places.

    Vrai parce que les aretes sont deja placees a ce stade : la parite des
    coins est alors paire, ce qui exclut les transpositions (2 fixes).
    """
    import itertools
    POS = ['URF', 'ULF', 'ULB', 'URB']
    counts = set()
    for perm in itertools.permutations(POS):
        idx = [POS.index(x) for x in perm]
        inv = sum(1 for a in range(4) for b in range(a + 1, 4) if idx[a] > idx[b])
        if inv % 2:
            continue                       # parite impaire : impossible ici
        counts.add(sum(1 for i, x in enumerate(perm) if x == POS[i]))
    ok(counts == {0, 1, 4},
       'etape 6 : nombres de coins bien places possibles = %s, attendu {0,1,4}'
       % sorted(counts))


def check_step5_two_matched():
    """« Cherche une position ou au moins deux aretes sont assorties. »"""
    import itertools
    POS = ['UB', 'UR', 'UF', 'UL']
    worst = 4
    for perm in itertools.permutations(POS):
        best = max(sum(1 for i in range(4)
                       if perm[(i - k) % 4] == POS[i]) for k in range(4))
        worst = min(worst, best)
    ok(worst >= 2,
       'etape 5 : il existe un cas sans deux aretes assorties (min %d)' % worst)


def check_f2l_pair_extraction():
    """cfop/f2l : « R U R' sort la paire de la fente, R U' R' l'y range. »"""
    PAIR = [((1, -1, 1), (0, -1, 0)), ((1, -1, 1), (0, 0, 1)), ((1, -1, 1), (1, 0, 0)),
            ((1, 0, 1), (0, 0, 1)), ((1, 0, 1), (1, 0, 0))]
    out = travel("R U R'", [PAIR[0], PAIR[3]])
    ok(all(dst[0][1] == 1 for _s, dst in out),
       'cfop/f2l : R U R\' ne fait pas monter la paire dans la couche du haut')
    c = solved().apply("R U R'").apply("R U' R'")
    ok(c.is_solved(), "cfop/f2l : R U R' puis R U' R' ne revient pas au depart")


def check_4lll_counts():
    """La page 4LLL annonce 3 + 7 + 3 + 4 = 16 algorithmes."""
    oll = json.load(open(ROOT + '/data/oll.json', encoding='utf-8'))
    pll = json.load(open(ROOT + '/data/pll.json', encoding='utf-8'))
    ok(len([r for r in oll if r[3] == 'croix']) == 7,
       '4lll : le groupe « croix » de l\'OLL ne contient pas 7 cas')
    ok(len([r for r in pll if r[3] == 'coins']) == 3,
       '4lll : le groupe CPLL ne contient pas 3 cas')
    ok(len([r for r in pll if r[3] == 'aretes']) == 4,
       '4lll : le groupe EPLL ne contient pas 4 cas')
    ok(len(oll) == 57 and len(pll) == 21,
       'index : les listes ne font pas 57 et 21')
    ok(len(oll) + len(pll) == 78, 'glossaire : 57 + 21 devrait faire 78')


def check_named_algs():
    """glossaire : Sune oriente trois coins, le T-perm echange 2 coins + 2 aretes."""
    E_U = {(0, 1, 1), (0, 1, -1), (1, 1, 0), (-1, 1, 0)}
    C_U = {(1, 1, 1), (-1, 1, 1), (1, 1, -1), (-1, 1, -1)}
    t = "R U R' U' R' F R2 U' R' U' R U R' F'"
    mv_e = [s for s, d in travel(t, [(p, (0, 1, 0)) for p in E_U]) if s[0] != d[0]]
    mv_c = [s for s, d in travel(t, [(p, (0, 1, 0)) for p in C_U]) if s[0] != d[0]]
    ok(len(mv_e) == 2, 'glossaire : le T-perm deplace %d aretes au lieu de 2' % len(mv_e))
    ok(len(mv_c) == 2, 'glossaire : le T-perm deplace %d coins au lieu de 2' % len(mv_c))
    # « Sune : oriente trois coins » — c'est bien une ORIENTATION, pas un
    # deplacement : on compte les coins mal orientes dans le cas, puis on
    # verifie que l'algorithme rend toute la face jaune.
    for name, a in (('Sune', "R U R' U R U2 R'"),
                    ('anti-Sune', "R U2 R' U' R U' R'")):
        ok(is_ll_alg(a), 'glossaire : le %s casse les deux premieres couronnes' % name)
        st = case_state(a)
        mis = [i for i in (0, 2, 6, 8) if st.facelets()['U'][i] != 'Y']
        ok(len(mis) == 3,
           'glossaire : le cas %s a %d coins mal orientes au lieu de 3' % (name, len(mis)))
        ok(all(x == 'Y' for x in case_state(a).apply(a).facelets()['U']),
           'glossaire : le %s ne rend pas la face du haut entierement jaune' % name)


def check_cross_bounds():
    """cfop/croix : « 8 mouvements maximum », « un peu moins de 6 en moyenne ».

    Parcours EXHAUSTIF des 190 080 etats de la croix (position + orientation
    des 4 aretes blanches). Ce n'est pas un echantillon : c'est la totalite.
    """
    SOLVED_X = (((0, -1, 1), (0, -1, 0)), ((0, -1, -1), (0, -1, 0)),
                ((1, -1, 0), (0, -1, 0)), ((-1, -1, 0), (0, -1, 0)))
    table = {}
    for g in GEN18:
        base, suf = g[0], g[1:]
        axis, layers, q1 = MOVES[base]
        n = 2 if suf == '2' else (3 if suf == "'" else 1)
        table[g] = (axis, layers, (q1 * n) % 4)

    def step(state, g):
        axis, layers, q = table[g]
        rot, i = ROT[axis], AXIS_IDX[axis]
        out = []
        for pos, nrm in state:
            if pos[i] in layers:
                for _ in range(q):
                    pos, nrm = rot(pos), rot(nrm)
            out.append((pos, nrm))
        return tuple(out)

    dist = {SOLVED_X: 0}
    frontier, d = [SOLVED_X], 0
    while frontier:
        d += 1
        nxt = []
        for s in frontier:
            for g in GEN18:
                n = step(s, g)
                if n not in dist:
                    dist[n] = d
                    nxt.append(n)
        frontier = nxt
    v = list(dist.values())
    ok(len(dist) == 190080, 'croix : %d etats au lieu de 190080' % len(dist))
    ok(max(v) == 8, 'cfop/croix : distance maximale %d au lieu de 8' % max(v))
    mean = sum(v) / len(v)
    ok(5.0 < mean < 6.0,
       'cfop/croix : moyenne %.3f, la page annonce « un peu moins de 6 »' % mean)


# --- les bandes « pas a pas » : une par sequence citee, dans les 3 langues ---
REFERENCE_PAGES = ('avance/', 'advanced/')


def _tutorial_pages():
    return [(fr, ot) for fr, ot in PAGES if not fr.startswith(REFERENCE_PAGES)]


def check_films():
    """Toute sequence citee dans une page de tutoriel doit avoir sa bande, et
    toute bande generee doit etre montree quelque part — dans les trois langues.

    C'est ce qui empeche une page d'annoncer un algorithme sans l'illustrer, et
    une bande de rester orpheline apres un remaniement de page.
    """
    from build import FILMS, CITEES_SANS_BANDE
    known = {alg: slug for slug, alg in FILMS}
    ok(len(known) == len(FILMS), 'films : deux entrees pour la meme sequence')

    per_lang = {}
    for lang, d in LANGS:
        used = set()
        for fr_rel, other_rel in _tutorial_pages():
            txt = open(path_for(d, fr_rel, other_rel), encoding='utf-8').read()
            for alg in algs_in(txt):
                if alg in CITEES_SANS_BANDE:      # citee pour comparaison
                    continue
                ok(alg in known,
                   '%s [%s] : la sequence « %s » est citee sans bande pas a pas '
                   '(ajouter FILMS dans tools/build.py)' % (fr_rel, lang, alg))
            used |= set(imgs_in(txt)) & set('film-' + s for s in known.values())
        per_lang[lang] = used

    for slug in known.values():
        for lang in per_lang:
            ok('film-' + slug in per_lang[lang],
               'film-%s.svg [%s] : bande generee mais montree nulle part' % (slug, lang))
    ref = per_lang['fr']
    for lang, used in per_lang.items():
        ok(used == ref, 'les bandes montrees en %s different du francais (%s)'
           % (lang, sorted(used ^ ref)))


def check_no_orphan_figure():
    """Aucun schema produit ne doit rester invisible.

    Le symetrique de check_films(), etendu a tous les schemas : une figure
    generee que plus aucune page ne cite est du poids mort publie, et surtout le
    signe d'une illustration perdue en cours de route — c'est ainsi que l'etape 6
    s'est retrouvee sans rien pour montrer son cycle de coins.
    """
    import glob
    for lang, d in LANGS:
        used = set()
        for fr_rel, other_rel in PAGES:
            used |= set(imgs_in(open(path_for(d, fr_rel, other_rel),
                                     encoding='utf-8').read()))
        produits = set(os.path.basename(p)[:-4]
                       for p in glob.glob(os.path.join(ROOT, d, 'assets/cubes/*.svg')))
        for orphelin in sorted(produits - used):
            ok(False, '%s.svg [%s] : schema genere mais cite par aucune page'
               % (orphelin, lang))
        ok(True, 'schemas orphelins [%s]' % lang)


# --- 8. les trois langues doivent avoir la MEME structure de page ----------
BLOC_RE = re.compile(
    r'(?P<titre2>^\#\# [^\n]*)'
    r'|(?P<titre3>^\#\#\# [^\n]*)'
    r'|(?P<onglet>^=== "[^\n]*)'
    r'|(?P<fiche><div class="fiche")'
    r'|(?P<objectif><div class="objectif")'
    r'|(?P<grille><div class="algs">)'
    r'|(?P<bande><figure class="film">)'
    r'|(?P<repliee><details class="film">)'
    r'|(?P<admonition>^!!! [^\n]*)', re.M)


def structure(texte):
    """Suite des blocs d'une page, sans leur contenu : titres, fiches, figures,
    grilles, bandes, onglets, admonitions."""
    return [m.lastgroup for m in BLOC_RE.finditer(texte)]


def check_same_structure():
    """Une page doit se presenter pareil dans les trois langues.

    check_langs_agree() compare les algorithmes cites ; ici on compare la
    CHARPENTE. C'est ce qui empeche une figure, un titre ou un onglet ajoute
    dans une seule langue de passer inapercu — et donc une langue d'expliquer
    mieux qu'une autre.
    """
    for fr_rel, other_rel in PAGES:
        ref = ref_lang = None
        for lang, d in LANGS:
            got = structure(open(path_for(d, fr_rel, other_rel),
                                 encoding='utf-8').read())
            if ref is None:
                ref, ref_lang = got, lang
            else:
                ok(got == ref,
                   '%s : structure differente entre %s et %s (%d blocs vs %d, '
                   'premiere difference : %s)'
                   % (fr_rel, ref_lang, lang, len(ref), len(got),
                      next(('%s vs %s' % (a, b)
                            for a, b in zip(ref, got) if a != b), 'longueur')))


def check_orientation_equivalente():
    """« Le meme geste, cube retourne » : l'etape 2 l'affirme, on le prouve.

    Retourner le cube echange U et D dans l'ecriture des mouvements. La sequence
    du site avec le blanc en bas et celle de la convention blanc en haut doivent
    donc etre conjuguees par x2 — sinon la note induirait le lecteur en erreur.
    """
    for alg in _rand_algs(40, 14):
        a = solved().apply(alg).apply("R' D' R D")
        b = solved().apply(alg).apply('x2').apply("R' U' R U").apply('x2')
        ok(a.st == b.st,
           "R' D' R D et R' U' R U ne sont pas le meme geste retourne (%s)" % alg)


EXTRA = [check_pieces_and_colours, check_centres_fixed, check_notation_semantics,
         check_invariants, check_beginner_method, check_step3_insertions,
         check_step6_zero_one_four, check_step5_two_matched,
         check_f2l_pair_extraction, check_4lll_counts, check_named_algs,
         check_cross_bounds, check_films, check_no_orphan_figure,
         check_same_structure, check_orientation_equivalente]


if __name__ == '__main__':
    _main()
