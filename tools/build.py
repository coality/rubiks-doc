# -*- coding: utf-8 -*-
"""Genere les SVG et les pages d'algorithmes du site depuis les donnees verifiees.

Multilingue : tout est produit une fois par langue declaree dans LANGS. Les
textes traduits vivent dans data/i18n.json, data/names.<lang>.json et
data/intros/<lang>/. Les schemas sont recalcules pour chaque langue afin que
le <title> / aria-label du SVG soit dans la bonne langue.
"""
import json, os, sys, shutil
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from cube import (Cube, solved, invert, derotate, case_state, is_ll_alg,
                  orient_std, face_index, FACES)
from render import render_net, render_ll, pll_arrows, PAINT, _svg, _body, _sticker, S, G, T, P
from render3d import render3d, filmstrip, travel, CAM_BAS

ROOT = os.path.normpath(os.path.join(_HERE, '..'))

# (code, dossier docs, prefixe d'URL absolue du site, dossier des pages de reference)
LANGS = [('fr', 'docs', '', 'avance'),
         ('en', 'docs-en', '/en', 'advanced'),
         ('bis', 'docs-bis', '/bis', 'advanced')]

I18N = json.load(open(ROOT + '/data/i18n.json', encoding='utf-8'))

# etat courant de la generation (fixe par run_lang)
LANG, DOCS, BASE, REFDIR, STR, NAMES = None, None, None, None, None, None
WRITTEN = set()          # schemas produits par la langue en cours


def set_lang(code, docsdir, base, refdir):
    global LANG, DOCS, BASE, REFDIR, STR, NAMES
    LANG, DOCS, BASE, REFDIR = code, ROOT + '/' + docsdir, base, refdir
    STR = I18N[code]
    path = ROOT + '/data/names.%s.json' % code
    NAMES = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else None
    os.makedirs(DOCS + '/assets/cubes', exist_ok=True)
    WRITTEN.clear()


def name_of(kind, cid, default):
    """Nom traduit d'un cas OLL/PLL ; le francais est la source dans data/<kind>.json."""
    if NAMES is None:
        return default
    return NAMES[kind].get(cid, default)


CORNERS = [(('U', 0), ('L', 0), ('B', 2)), (('U', 2), ('B', 0), ('R', 2)),
           (('U', 6), ('F', 0), ('L', 2)), (('U', 8), ('R', 0), ('F', 2)),
           (('D', 0), ('L', 8), ('F', 6)), (('D', 2), ('F', 8), ('R', 6)),
           (('D', 6), ('B', 8), ('L', 6)), (('D', 8), ('R', 8), ('B', 6))]
EDGES = [(('U', 1), ('B', 1)), (('U', 3), ('L', 1)), (('U', 5), ('R', 1)), (('U', 7), ('F', 1)),
         (('F', 3), ('L', 5)), (('F', 5), ('R', 3)), (('B', 3), ('R', 5)), (('B', 5), ('L', 3)),
         (('D', 1), ('F', 7)), (('D', 3), ('L', 7)), (('D', 5), ('R', 7)), (('D', 7), ('B', 7))]


def labeled(alg):
    """Etat du cas, chaque facette portant sa position d'origine."""
    c = Cube()
    for k in list(c.st):
        c.st[k] = face_index(*k)
    c.apply(invert(derotate(alg)))
    return c.facelets()


def write(name, svg):
    with open('%s/assets/cubes/%s.svg' % (DOCS, name), 'w', encoding='utf-8') as fh:
        fh.write(svg)
    WRITTEN.add(name)
    return 'assets/cubes/%s.svg' % name


def prune():
    """Supprime les schemas qu'on ne produit plus.

    Sans ca, renommer une figure laisse l'ancien fichier sur le disque : MkDocs
    le copie dans site/ et le publie, alors que plus aucune page ne le cite.
    """
    d = DOCS + '/assets/cubes'
    old = [f for f in os.listdir(d)
           if f.endswith('.svg') and f[:-4] not in WRITTEN]
    for f in old:
        os.remove(os.path.join(d, f))
    return old


def fig_title(name):
    """Titre traduit d'un schema fixe, repere par son nom de fichier.

    Echoue si la traduction manque : un `.get(name, name)` silencieux laisserait
    passer un `<title>` / `aria-label` en francais dans le site anglais ou
    bisaya, et rien ne le signalerait.
    """
    try:
        return STR['figures'][name]
    except KeyError:
        raise KeyError('titre de figure « %s » absent de data/i18n.json pour %s'
                       % (name, LANG))


# ---------------------------------------------------------------- OLL / PLL
def gen_ll(kind):
    rows = json.load(open('%s/data/%s.json' % (ROOT, kind), encoding='utf-8'))
    out = []
    for cid, name, alg, grp in rows:
        st = case_state(alg)
        arr = pll_arrows(alg) if kind == 'pll' else None
        svg = render_ll(st, mode=kind, arrows=arr, title='%s %s' % (kind.upper(), cid))
        out.append(dict(id=cid, name=name_of(kind, cid, name), alg=alg, grp=grp,
                        img=write('%s-%s' % (kind, cid.lower()), svg)))
    return out


# ---------------------------------------------------------------------- F2L
PAIR_HOME = [('D', 2), ('F', 8), ('R', 6), ('F', 5), ('R', 3)]
CTX = ([('D', i) for i in range(9)] +
       [(f, i) for f in ('F', 'R', 'B', 'L') for i in range(3, 9)])


def gen_f2l():
    algs = [a for a in json.load(open(ROOT + '/data/f2l_raw.json', encoding='utf-8')) if a.strip()]
    out = []
    for n, alg in enumerate(algs, 1):
        fl = labeled(alg)
        here = [(f, i) for f in FACES for i in range(9) if fl[f][i] in PAIR_HOME]
        keep = set(CTX) | set(here)
        st = solved().apply(invert(derotate(alg)))
        svg = render_net(st, keep=keep, title=STR['f2l_case_title'] % n)
        # ou sont le coin et l'arete ?
        cpos = next(k for k, sl in enumerate(CORNERS)
                    if set(sl) & set(here) and len(set(sl) & set(here)) == 3)
        epos = next(k for k, sl in enumerate(EDGES)
                    if len(set(sl) & set(here)) == 2)
        c_up = cpos < 4
        e_up = epos < 4
        if c_up and e_up:
            grp = 'a-deux-en-haut'
        elif c_up and not e_up:
            grp = 'b-arete-casee'
        elif e_up and not c_up:
            grp = 'c-coin-case'
        else:
            grp = 'd-les-deux-cases'
        out.append(dict(id=str(n), name=STR['f2l_case_name'] % n, alg=alg, grp=grp,
                        moves=len(alg.split()), img=write('f2l-%02d' % n, svg)))
    out.sort(key=lambda r: (r['grp'], r['moves'], r['alg']))
    for n, r in enumerate(out, 1):
        r['name'] = STR['f2l_case_name'] % n
    return out


# ------------------------------------------------------------ figures fixes
def u_pattern(bits, name):
    """Diagramme d'orientation des aretes du haut (etape croix jaune)."""
    blk = 3 * S + 2 * G
    w = h = blk + 2 * P
    parts = [_body(0, 0, w, h)]
    for i in range(9):
        on = bits[i] if i < len(bits) else False
        parts.append(_sticker(P + (i % 3) * (S + G), P + (i // 3) * (S + G), 'Y' if on else '.'))
    return write(name, _svg(w, h, parts, fig_title(name)))


def net_fig(name, keep=None):
    return write(name, render_net(solved(), keep=keep, title=fig_title(name)))


def gen_figures():
    f = {}
    croix = set([('D', i) for i in (1, 3, 4, 5, 7)] +
                [(x, 7) for x in ('F', 'R', 'B', 'L')])
    couronne1 = set([('D', i) for i in range(9)] +
                    [(x, i) for x in ('F', 'R', 'B', 'L') for i in (6, 7, 8)])
    couronne2 = set(CTX)
    f['resolu'] = net_fig('but-resolu')
    f['croix'] = net_fig('but-croix', croix)
    f['couronne1'] = net_fig('but-couronne1', couronne1)
    f['couronne2'] = net_fig('but-couronne2', couronne2)
    f['croixjaune'] = u_pattern([0, 1, 0, 1, 1, 1, 0, 1, 0], 'but-croix-jaune')
    f['facejaune'] = u_pattern([1] * 9, 'but-face-jaune')
    f['eo_point'] = u_pattern([0, 0, 0, 0, 1, 0, 0, 0, 0], 'eo-point')
    f['eo_barre'] = u_pattern([0, 0, 0, 1, 1, 1, 0, 0, 0], 'eo-barre')
    f['eo_equerre'] = u_pattern([0, 1, 0, 1, 1, 0, 0, 0, 0], 'eo-equerre')
    return f


def gen_beginner():
    """Cas illustres de la methode debutant, rendus depuis les algos verifies."""
    specs = [
        ('couronne2-droite', "U R U' R' U' F' U F"),
        ('couronne2-gauche', "U' L' U L U F U' F'"),
        ('coins-placer', "U R U' L' U R' U' L"),
    ]
    out = {}
    for name, alg in specs:
        assert is_ll_alg(alg) or name.startswith('couronne2'), name
        st = solved().apply(invert(derotate(alg)))
        title = fig_title(name)
        out[name] = dict(alg=alg, img=write(name, render_net(st, title=title)), title=title)
    return out


# ------------------------------------------- figures pedagogiques (debutant)
# Chaque etat est produit par le moteur puis verifie : aucune figure n'est
# dessinee a la main, et une figure fausse fait echouer le build.
FACE_CENTER = {'U': 4, 'D': 4, 'F': 4, 'R': 4, 'B': 4, 'L': 4}


def _keep(*specs):
    out = set()
    for face, idx in specs:
        for i in idx:
            out.add((face, i))
    return out


def gen_teaching():
    """Schemas ajoutes pour la methode debutant : familles de pieces, marguerite,
    croix mal assortie, reperes coin/arete, intrus en 2e couronne, cube 'casse'."""
    out = {}

    def emit(name, cube, keep=None, check=None):
        fl = cube.facelets()
        if check is not None:
            assert check(fl), 'figure %s : etat inattendu' % name
        out[name] = write(name, render_net(cube, keep=keep, title=fig_title(name)))

    sides = ('F', 'R', 'B', 'L')

    # --- les trois familles de pieces (page notation)
    centres = _keep(*[(f, (4,)) for f in FACES])
    aretes = _keep(*[(f, (1, 3, 5, 7)) for f in FACES])
    coins = _keep(*[(f, (0, 2, 6, 8)) for f in FACES])
    emit('familles-centres', solved(), centres)
    emit('familles-aretes', solved(), aretes)
    emit('familles-coins', solved(), coins)

    # --- etape 1 : la marguerite (4 aretes blanches autour du centre jaune)
    daisy = solved().apply('F2 R2 B2 L2')
    emit('marguerite', daisy,
         _keep(('U', (1, 3, 4, 5, 7)), *[(f, (1, 4)) for f in sides]),
         lambda fl: all(fl['U'][i] == 'W' for i in (1, 3, 5, 7)) and fl['U'][4] == 'Y')

    # --- etape 1 : croix faite mais cotes non assortis (l'erreur classique)
    bad = solved().apply('D')
    emit('croix-mauvaise', bad,
         _keep(('D', (1, 3, 4, 5, 7)), *[(f, (4, 7)) for f in sides]),
         lambda fl: all(fl['D'][i] == 'W' for i in (1, 3, 4, 5, 7))
         and fl['F'][7] != 'G')

    # (les deux figures a plat de l'etape 2 — le coin entre trois centres et le
    # coin blanc en attente — ont ete remplacees par leurs versions 3D, qui
    # montrent en plus la fente d'arrivee. Voir gen_3d().)

    # --- etape 3 : une arete vit entre deux centres
    emit('arete-deux-centres', solved(),
         _keep(('F', (4, 5)), ('R', (3, 4))))

    # --- etape 3 : une arete etrangere coincee dans la fente avant-droite
    intru = solved().apply("U R U' R' U' F' U F")
    emit('couronne2-intrus', intru,
         _keep(('F', (3, 4, 5, 6, 7, 8)), ('R', (3, 4, 5, 6, 7, 8)),
               ('D', tuple(range(9)))),
         lambda fl: (fl['F'][5], fl['R'][3]) != ('G', 'O')
         and all(fl['D'][i] == 'W' for i in (1, 3, 4, 5, 7)))

    # --- objectif de l'etape 5 : les quatre aretes jaunes assorties.
    # Etat reel de fin d'etape — donc l'etat de depart de l'etape 6 — et non un
    # cube resolu masque : a ce stade les coins ne sont NI places NI tournes,
    # un cube resolu le ferait croire.
    apres5 = solved().apply(invert("U R U' L' U R' U' L"))
    emit('but-aretes-jaunes', apres5,
         _keep(('U', (1, 3, 4, 5, 7)), *[(f, (1, 4)) for f in sides]),
         lambda fl: (all(fl['U'][i] == 'Y' for i in (1, 3, 5, 7))
                     and all(fl[f][1] == fl[f][4] for f in sides)))

    # --- objectif de l'etape 6 : les quatre coins a leur place, mais tournes.
    # Le cas OLL 21 : tout est permute, seule l'orientation des coins reste.
    apres6 = solved().apply(invert(derotate("R U2 R' U' R U R' U' R U' R'")))
    coins_hauts = _keep(('U', (0, 2, 4, 6, 8)), *[(f, (0, 2, 4)) for f in sides])

    def _coins_places(fl):
        # les trois couleurs de chaque coin sont celles des trois faces qu'il
        # touche — l'ordre, lui, est faux : c'est tout le propos de la figure
        trios = [(('U', 0), ('L', 0), ('B', 2)), (('U', 2), ('B', 0), ('R', 2)),
                 (('U', 6), ('F', 0), ('L', 2)), (('U', 8), ('R', 0), ('F', 2))]
        for coin in trios:
            if set(fl[f][i] for f, i in coin) != set(fl[f][4] for f, _i in coin):
                return False
        return sum(1 for i in (0, 2, 6, 8) if fl['U'][i] != 'Y') == 4

    emit('but-coins-places', apres6, coins_hauts, _coins_places)

    # --- etape 7 : le cube a l'air detruit au milieu de l'orientation des coins
    mid = solved().apply("R' D' R D R' D' R D")
    emit('cube-casse', mid, None,
         lambda fl: not all(c == 'W' for c in fl['D']))

    return out

# ------------------------------------------------- schemas 3D (isometriques)
SEQ_COIN = "R' D' R D"

# Ou est le blanc quand le coin attend en haut, et combien de repetitions il
# faut alors. Ce ne sont PAS 2 ou 4 : ces deux-la ramenent le coin d'ou il
# vient. Les valeurs sont reverifiees ci-dessous a chaque build.
COIN_CASES = [('3d-coin-blanc-avant', 1, (0, 0, 1)),
              ('3d-coin-blanc-haut', 3, (0, 1, 0)),
              ('3d-coin-blanc-droite', 5, (1, 0, 0))]


def _first_layer_done(cube):
    """La premiere couronne est-elle vraiment finie ?

    Comparer la rangee du bas a elle-meme ne suffit pas : apres `R' D' R`, elle
    est unie ET la face blanche est complete, mais l'ensemble est decale d'un
    quart de tour par rapport aux centres. On compare donc au CENTRE de chaque
    face, sinon une couronne hors de phase passerait pour terminee.
    """
    fl = cube.facelets()
    return (all(x == 'W' for x in fl['D'])
            and all(fl[f][i] == fl[f][4] for f in 'FRBL' for i in (6, 7, 8)))


def gen_3d():
    """Vues isometriques : trajets de pieces et sens des mouvements.

    Les fleches viennent de travel(), donc du moteur : elles ne peuvent pas
    contredire l'algorithme annonce. Les auto-tests de tools/test_render3d.py
    verifient en plus le sens de rotation face par face.
    """
    out = {}

    def emit(name, cube, **kw):
        out[name] = write(name, render3d(cube, title=fig_title(name), **kw))

    # --- notation : reperes et sens des mouvements
    emit('3d-faces', solved(), labels=[('U', 'U'), ('F', 'F'), ('R', 'R')])
    # D est le mouvement que la page signale comme l'erreur numero un : c'est
    # justement celui qui manquait. Son arc passe SOUS le cube, donc il se lit
    # tres bien — contrairement a B, dont l'arc passe derriere et semble
    # appartenir a la face droite. Pas de figure pour B, donc.
    for name, face, cw in (('3d-move-r', 'R', True), ('3d-move-rp', 'R', False),
                           ('3d-move-u', 'U', True), ('3d-move-f', 'F', True),
                           ('3d-move-d', 'D', True)):
        emit(name, solved(), turns=[(face, cw)])

    # --- etape 1 : le petale descend a sa place avec F2
    daisy = solved().apply('F2 R2 B2 L2')
    arr = travel('F2', [((0, 1, 1), (0, 0, 1))])
    assert arr[0][1] == ((0, -1, 1), (0, 0, 1)), 'F2 : trajet du petale inattendu'
    emit('3d-petale-descend', daisy, arrows=arr)

    # --- CFOP : le F2L insere le coin ET l'arete d'un seul geste. C'est
    # l'argument central de la page ; les deux fleches viennent du moteur.
    pair = "R U' R'"
    depart = [((-1, 1, 1), (0, 1, 0)), ((0, 1, 1), (0, 1, 0))]
    arr = travel(pair, depart)
    fente = {((1, -1, 1), (0, 0, 1)), ((1, 0, 1), (0, 0, 1))}
    assert set(b for _a, b in arr) == fente, \
        'F2L : la paire devrait arriver dans la fente avant-droite, pas %r' % (arr,)
    emit('3d-paire-f2l', solved().apply(invert(pair)), arrows=arr)

    # --- CFOP : la croix telle qu'on doit apprendre a la lire, par en dessous.
    # La page demande de la construire sans retourner le cube ; une vue de
    # dessus ne montrerait justement pas ce qu'on doit apprendre a voir.
    emit('3d-croix-dessous', solved(), cam=CAM_BAS,
         keep=set(face_index(pos, nrm) for pos, nrm in
                  [((0, -1, 0), (0, -1, 0)), ((0, -1, 1), (0, -1, 0)),
                   ((0, -1, -1), (0, -1, 0)), ((1, -1, 0), (0, -1, 0)),
                   ((-1, -1, 0), (0, -1, 0)),
                   ((0, -1, 1), (0, 0, 1)), ((1, -1, 0), (1, 0, 0)),
                   ((0, 0, 1), (0, 0, 1)), ((1, 0, 0), (1, 0, 0))]))

    # --- etape 2 : ce qu'il faut avoir vu AVANT de tourner quoi que ce soit.
    # Toute l'action se passe en bas : on regarde donc le cube par en dessous,
    # sinon la fente d'arrivee est cachee.
    URF, DRF = (1, 1, 1), (1, -1, 1)
    N_U, N_D, N_F, N_R = (0, 1, 0), (0, -1, 0), (0, 0, 1), (1, 0, 0)

    def fx(*specs):
        return set(face_index(pos, nrm) for pos, nrm in specs)

    centres = fx(((0, -1, 0), N_D), ((0, 0, 1), N_F), ((1, 0, 0), N_R))
    # un coin vit entre trois centres : ici blanc + vert + orange
    emit('3d-coin-trois-centres', solved(), cam=CAM_BAS,
         keep=fx((DRF, N_D), (DRF, N_F), (DRF, N_R)) | centres)

    # ou le coin doit arriver : la fente, vue par en dessous
    alg1 = SEQ_COIN
    st1 = solved().apply(invert(alg1))
    arr1 = travel(alg1, [(URF, N_F)])
    assert arr1[0][1] == (DRF, N_D), 'fente : le blanc devrait arriver sous le cube'
    # la piece qui squatte la fente est grisee : le lecteur n'a pas a s'en
    # soucier, la fleche pointe alors vers "le trou" et non vers une couleur.
    emit('3d-coin-fente', st1, cam=CAM_BAS, arrows=arr1,
         keep=fx((URF, N_F), (URF, N_R)) | centres)

    # --- etape 2 : les trois positions du blanc, et le nombre de repetitions
    for name, k, white_normal in COIN_CASES:
        alg = ' '.join([SEQ_COIN] * k)
        st = solved().apply(invert(alg))
        # le coin blanc attend bien en haut, blanc sur la face annoncee
        assert st.st[((1, 1, 1), white_normal)] == 'W', \
            '%s : le blanc n\'est pas sur la face attendue' % name
        assert _first_layer_done(st.copy().apply(alg)), \
            '%s : %d repetitions ne terminent pas la premiere couronne' % (name, k)
        for bad in (k - 1, k + 1):       # les comptes pairs encadrants echouent
            if bad > 0:
                assert not _first_layer_done(
                    st.copy().apply(' '.join([SEQ_COIN] * bad))), \
                    '%s : %d repetitions ne devraient pas suffire' % (name, bad)
        # « ne t'arrete jamais en cours de route » : aucun arret intermediaire
        # ne finit la couronne. Le piege est a l'avant-dernier mouvement, ou
        # tout a l'air fini alors que le bas est decale d'un quart de tour.
        partiel = st.copy()
        for i, coup in enumerate(alg.split()[:-1], 1):
            partiel.apply(coup)
            assert not _first_layer_done(partiel), \
                '%s : s\'arreter au mouvement %d finirait la couronne' % (name, i)
        arr = travel(alg, [((1, 1, 1), white_normal)])
        assert arr[0][1][1] == (0, -1, 0), '%s : le blanc devrait finir en bas' % name
        emit(name, st, arrows=arr)

    # --- etape 3 : l'arete descend dans sa fente, a droite ou a gauche.
    # Les deux cas sont miroirs : ils mentent le meme droit a une figure.
    UF = ((0, 1, 1), (0, 0, 1))
    for cote, ins, cible in (('droite', "U R U' R' U' F' U F", ((1, 0, 1), (0, 0, 1))),
                             ('gauche', "U' L' U L U F U' F'", ((-1, 0, 1), (0, 0, 1)))):
        arr = travel(ins, [UF])
        assert arr[0][1] == cible, \
            'insertion %s : l\'arete arrive en %r, %r attendu' % (cote, arr[0][1], cible)
        emit('3d-arete-insere-' + cote, solved().apply(invert(ins)), arrows=arr)

    # --- etape 6 : trois coins tournent entre eux, le quatrieme ne bouge pas.
    # Le schema a plat ne peut pas le montrer : l'algo retourne les coins en les
    # deplacant, donc l'autocollant du haut ne vient pas du haut et pll_arrows()
    # n'a rien a tracer. Le trajet 3D, lui, suit la piece quoi qu'il arrive.
    cyc = "U R U' L' U R' U' L"
    hauts = [(1, 1, 1), (-1, 1, 1), (1, 1, -1), (-1, 1, -1)]
    N_HAUT = (0, 1, 0)
    arr = travel(cyc, [(p, N_HAUT) for p in hauts])
    bouge = [(a, b) for a, b in arr if a[0] != b[0]]
    assert len(bouge) == 3, \
        'etape 6 : %d coins deplaces, la page en annonce 3' % len(bouge)
    assert len([a for a, b in arr if a[0] == b[0]]) == 1, \
        'etape 6 : le coin epargne devrait etre unique'
    # On relie le dessus au dessus, pas l'autocollant a son arrivee reelle :
    # l'algo retourne les coins en les deplacant, et une fleche qui plongerait
    # vers une face laterale ferait croire a un changement d'etage. L'etape ne
    # parle que de PLACEMENT — l'orientation est le sujet de l'etape 7.
    emit('3d-coins-cycle', solved().apply(invert(cyc)),
         arrows=[(a, (b[0], N_HAUT)) for a, b in bouge])

    # --- etape 7 : le coin est a sa place, il ne reste qu'a le tourner
    tw = ' '.join([SEQ_COIN] * 2)
    st = solved().apply(invert(tw))
    arr = travel(tw, [((1, 1, 1), (0, 1, 0))])
    assert arr[0][1][0] == (1, 1, 1), 'etape 7 : le coin ne doit pas changer de place'
    emit('3d-coin-tourne', st, arrows=arr)

    return out


# ------------------------------------------------- sequences pas a pas (3D)
# Toute sequence citee dans une page de tutoriel a sa bande. La liste est
# verrouillee par tools/check_content.py : citer une sequence dans une page
# sans l'ajouter ici fait echouer le build.
FILMS = [
    # methode debutant
    ('coin-blanc',              "R' D' R D"),
    ('couronne2-droite',        "U R U' R' U' F' U F"),
    ('couronne2-gauche',        "U' L' U L U F U' F'"),
    ('croix-jaune',             "F R U R' U' F'"),
    ('aretes-jaunes',           "R U' R U R U R U' R' U' R2"),
    ('coins-places',            "U R U' L' U R' U' L"),
    # 4LLL — orientation des coins
    ('sune',                    "R U R' U R U2 R'"),
    ('antisune',                "R U2 R' U' R U' R'"),
    ('double-sune',             "R U2 R' U' R U R' U' R U' R'"),
    ('pi',                      "R U2 R2 U' R2 U' R2 U2 R"),
    ('tete',                    "R2 D' R U2 R' D R U2 R"),
    ('chaussette',              "r U R' U' r' F R F'"),
    ('noeud-papillon',          "F' r U R' U' r' F R"),
    # 4LLL — permutation des coins, puis des aretes
    ('aperm-a',                 "x R' U R' D2 R U' R' D2 R2"),
    ('aperm-b',                 "x R2 D2 R U R' D2 R U' R"),
    ('eperm',                   "x' R U' R' D R U R' D' R U R' D R U' R' D'"),
    ('uperm-a',                 "M2 U M U2 M' U M2"),
    ('uperm-b',                 "M2 U' M U2 M' U' M2"),
    ('hperm',                   "M2 U M2 U2 M2 U M2"),
    ('zperm',                   "M' U M2 U M2 U M' U2 M2"),
    # declencheurs de F2L, sexy move, T-perm (glossaire)
    ('trigger-droit',           "R U R'"),
    ('trigger-droit-inverse',   "R U' R'"),
    ('trigger-gauche',          "F' U' F"),
    ('trigger-gauche-inverse',  "F' U F"),
    ('sexy',                    "R U R' U'"),
    ('tperm',                   "R U R' U' R' F R2 U' R' U' R U R' F'"),
]


def gen_films():
    """Une bande de vignettes par sequence : l'etat avant chaque mouvement, la
    fleche de ce mouvement et son nom.

    L'etat de depart est le cas que la sequence resout — la meme convention que
    les schemas a plat, donc la bande et la fiche ne peuvent pas diverger. Les
    vignettes sont deroulees par le moteur dans filmstrip() : elles disent donc
    exactement ce que fait l'algorithme, et l'assertion ci-dessous verifie que
    la derniere montre bien un cube resolu.
    """
    out = {}
    for slug, alg in FILMS:
        start = case_state(alg)
        assert orient_std(start.copy().apply(alg)).is_solved(), \
            '%s : « %s » ne resout pas l\'etat de depart de sa bande' % (slug, alg)
        svg = filmstrip(alg, start, title=STR['film_title'] % alg,
                        last=STR['film_result'])
        out['film-' + slug] = write('film-' + slug, svg)
    return out


# ------------------------------------------------------------------- pages
def cards(rows):
    out = ['<div class="algs">']
    for r in rows:
        out.append(
            '<figure class="alg">'
            '<img src="%s/%s" alt="%s" loading="lazy">'
            '<figcaption><b>%s</b><br><code>%s</code></figcaption>'
            '</figure>' % (BASE, r['img'], r['name'], r['name'], r['alg']))
    out.append('</div>')
    return '\n'.join(out)


def page(path, kind, rows, group_key):
    title = STR['page_titles'][kind]
    intro = open('%s/data/intros/%s/%s.md' % (ROOT, LANG, kind), encoding='utf-8').read().strip()
    labels = STR[group_key]
    body = ['# %s\n' % title, intro, '']
    for key in ORDER[group_key]:
        sel = [r for r in rows if r['grp'] == key]
        if not sel:
            continue
        body.append('## %s\n' % labels[key])
        body.append(cards(sel))
        body.append('')
    with open(DOCS + '/' + path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(body))
    return len(rows)


# ordre d'affichage des sections (les libelles, eux, sont traduits dans i18n.json)
ORDER = {
    'oll_groups': ['croix', 'points', 'bandeaux', 'poissons', 'eclairs', 'petits-l',
                   'carres', 'chevilles', 'formes-c', 'formes-p', 'formes-t', 'formes-w',
                   'formes-l', 'reveils', 'awkward', 'chaussures', 'coins-orientes'],
    'pll_groups': ['aretes', 'coins', 'mixtes'],
    'f2l_groups': ['a-deux-en-haut', 'b-arete-casee', 'c-coin-case', 'd-les-deux-cases'],
}


def emit_pages(oll, pll, f2l):
    os.makedirs(DOCS + '/' + REFDIR, exist_ok=True)
    page(REFDIR + '/oll.md', 'oll', oll, 'oll_groups')
    page(REFDIR + '/pll.md', 'pll', pll, 'pll_groups')
    page(REFDIR + '/f2l.md', 'f2l', f2l, 'f2l_groups')
    seen = set(r['grp'] for r in oll)
    missing = seen - set(ORDER['oll_groups'])
    assert not missing, 'groupes OLL non declares : %s' % missing
    # tout libelle declare doit exister dans les trois langues
    for key in ('oll_groups', 'pll_groups', 'f2l_groups'):
        absent = [k for k in ORDER[key] if k not in STR[key]]
        assert not absent, 'libelles %s manquants en %s : %s' % (key, LANG, absent)


def copy_static():
    """Les fichiers statiques non generes vivent une seule fois, dans docs/assets."""
    if DOCS.endswith('/docs'):
        return
    for f in ('extra.css', 'favicon.svg'):
        shutil.copyfile(ROOT + '/docs/assets/' + f, DOCS + '/assets/' + f)


def run_lang(code, docsdir, base, refdir):
    set_lang(code, docsdir, base, refdir)
    figs = gen_figures()
    beg = gen_beginner()
    figs.update(gen_teaching())
    figs.update(gen_3d())
    figs.update(gen_films())
    oll, pll, f2l = gen_ll('oll'), gen_ll('pll'), gen_f2l()
    emit_pages(oll, pll, f2l)
    perimes = prune()
    if perimes:
        print('       %d schema(s) perime(s) supprime(s) : %s'
              % (len(perimes), ', '.join(sorted(perimes))))
    copy_static()
    if code == 'fr':   # artefacts de debug, une seule langue suffit
        json.dump({'figures': figs, 'beginner': beg},
                  open(ROOT + '/data/figures.json', 'w'), indent=1, ensure_ascii=False)
        json.dump({'oll': oll, 'pll': pll, 'f2l': f2l},
                  open(ROOT + '/data/generated.json', 'w'), indent=1, ensure_ascii=False)
    return len(figs) + len(beg), len(oll), len(pll), len(f2l)


if __name__ == '__main__':
    for code, docsdir, base, refdir in LANGS:
        nf, no, np_, nf2 = run_lang(code, docsdir, base, refdir)
        print('[%-3s] %d figures fixes | OLL %d | PLL %d | F2L %d | pages de reference generees'
              % (code, nf, no, np_, nf2))
