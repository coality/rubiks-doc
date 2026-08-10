# -*- coding: utf-8 -*-
"""Rendu 3D (isometrique) du cube en SVG pur. Zero dependance, zero ressource.

Complementaire de render.py (patron deplie / vue de dessus) : ici on voit trois
faces d'un coup, ce qui permet de montrer **le trajet d'une piece** — d'ou elle
part, ou elle arrive — et **le sens d'un mouvement**.

Le moteur de cube repere chaque autocollant par (position, normale) dans
{-1,0,1}^3 : on a donc directement sa geometrie, et les fleches sont calculees
depuis les algorithmes eux-memes (cf. travel()), jamais placees a la main.

Reperes du moteur : x droite, y haut, z vers l'observateur.
"""
import math

from cube import Cube, NORMALS, NORMAL_TO_FACE, MOVES, face_index, parse
from render import PAINT, BODY, EDGE

# --- camera ----------------------------------------------------------------
CAM = (1.0, 0.85, 1.35)       # defaut : on regarde le coin haut-avant-droit
CAM_BAS = (1.0, -0.85, 1.35)  # vue de dessous : on voit D, F et R
SCALE = 44                   # pixels par unite de cubie
PAD = 16

STICKER = 0.42               # demi-cote d'un autocollant (cubie = 1)
RADIUS = 0.10                # arrondi des coins d'autocollant

INK = '#15171b'              # contour sombre des fleches
CHALK = '#f7f8fa'            # coeur clair des fleches : lisible sur tout


def _norm(v):
    n = math.sqrt(sum(c * c for c in v))
    return tuple(c / n for c in v)


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _mul(a, k):
    return tuple(x * k for x in a)


_D = _RIGHT = _UP = None


def set_camera(cam=CAM):
    """Fixe le point de vue. Les faces visibles en decoulent.

    Etat global assume : toutes les primitives (projection, visibilite, arcs)
    partagent la meme camera pendant le rendu d'une figure. render3d() la pose
    puis la restaure, donc l'appelant n'a rien a gerer.
    """
    global _D, _RIGHT, _UP
    _D = _norm(cam)                                   # cube -> camera
    up_world = (0, 1, 0) if abs(_D[1]) < 0.99 else (0, 0, 1)
    _RIGHT = _norm(_cross(up_world, _D))
    _UP = _cross(_D, _RIGHT)


set_camera()


def project(p):
    """Point 3D -> (x, y) ecran, en unites de cubie."""
    return (_dot(p, _RIGHT), -_dot(p, _UP))


def basis(n):
    """Base (u, v) du plan de normale n, telle que u x v = n."""
    ref = (0, 1, 0) if abs(n[1]) < 0.9 else (0, 0, 1)
    u = _norm(_cross(ref, n))
    v = _cross(n, u)
    return u, v


def visible(n):
    return _dot(n, _D) > 0.01


# --- primitives SVG --------------------------------------------------------
def _poly(pts, fill, stroke=EDGE, w=1.2, extra=''):
    d = ' '.join('%.2f,%.2f' % p for p in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%.1f" '
            'stroke-linejoin="round"%s/>' % (d, fill, stroke, w, extra))


def _path(d, stroke, w, extra=''):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" '
            'stroke-linecap="round" stroke-linejoin="round"%s/>'
            % (d, stroke, w, extra))


def _hull(points):
    """Enveloppe convexe (monotone chain) — la silhouette du cube est un hexagone."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2:
                (x1, y1), (x2, y2) = out[-2], out[-1]
                if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) > 0:
                    break
                out.pop()
            out.append(p)
        return out

    return half(pts)[:-1] + half(reversed(pts))[:-1]


# --- geometrie des autocollants -------------------------------------------
def sticker_center(pos, nrm):
    return _add(pos, _mul(nrm, 0.5))


def sticker_quad(pos, nrm):
    c = sticker_center(pos, nrm)
    u, v = basis(nrm)
    h = STICKER
    return [_add(c, _add(_mul(u, sx * h), _mul(v, sy * h)))
            for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]


# --- fleches ---------------------------------------------------------------
def travel(alg, want):
    """Trajets reels des autocollants, calcules en appliquant l'algorithme.

    `want` = liste de (position, normale) de depart. Renvoie la liste des
    ((pos, nrm) depart, (pos, nrm) arrivee). Une fleche ne peut donc pas
    raconter autre chose que ce que fait l'algorithme.
    """
    c = Cube()
    for k in list(c.st):
        c.st[k] = k                      # chaque facette porte son origine
    c.apply(alg)
    dest = {origin: here for here, origin in c.st.items()}
    out = []
    for k in want:
        assert k in dest, 'facette inconnue : %r' % (k,)
        out.append((k, dest[k]))
    return out


def _travel_2d(a, b, bulge=0.9):
    """(depart, arrivee, point de controle) en 2D pour la fleche de trajet.

    Le point de controle est pousse vers l'exterieur du cube : la courbe passe
    au-dessus de la surface au lieu de la traverser.
    """
    a3, b3 = sticker_center(*a), sticker_center(*b)
    mid = _mul(_add(a3, b3), 0.5)
    out = _norm(mid) if any(abs(c) > 1e-9 for c in mid) else _norm(_add(a3, b3))
    return project(a3), project(_add(mid, _mul(out, bulge))), project(b3)


def _arrow_defs():
    return ('<defs>'
            '<marker id="h3" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="4.6" '
            'markerHeight="4.6" orient="auto-start-reverse">'
            '<path d="M0.5,1 L11,6 L0.5,11 z" fill="%s" stroke="%s" '
            'stroke-width="1.6" stroke-linejoin="round"/></marker></defs>'
            % (CHALK, INK))


def _stroke_pair(d):
    """Trace deux fois : liseré sombre dessous, coeur clair dessus."""
    return [_path(d, INK, 7.0), _path(d, CHALK, 3.4, ' marker-end="url(#h3)"')]


# rayons des arcs : sur la face, autour d'une tranche, autour du cube entier
R_FACE, R_SLICE, R_WHOLE = 0.95, 2.15, 2.45
SPAN_QUARTER, SPAN_HALF, SPAN_WHOLE = 150.0, 250.0, 210.0
LIFT = 0.42


def arc3(face, clockwise=True, span=SPAN_QUARTER, radius=R_FACE, depth=1.92):
    """Arc EN 3D au-dessus d'une face, montrant le sens de rotation du mouvement.

    (u, v, n) est direct : tourner de u vers v (theta croissant) est ANTIhoraire
    vu depuis l'exterieur de la face. Un mouvement sans prime — horaire par
    definition de la notation — parcourt donc theta DECROISSANT. Verifie contre
    le moteur par tools/test_render3d.py, pour chacune des six faces.

    L'arc est centre sur la direction de la face qui **fait face a la camera** :
    la fleche se lit alors sur la partie visible, et non derriere le cube.

    `depth` est la distance du plan de l'arc au centre du cube, le long de la
    normale : 1.92 le pose juste au-dessus de la face, 0 au milieu du cube (pour
    une tranche), -1.92 au-dessus de la face opposee.

    Le rendu comme les tests passent par cette fonction : le sens verifie est
    donc bien celui qui est dessine, et non une reconstitution.
    """
    n = NORMALS[face]
    u, v = basis(n)
    w = [d - k * _dot(_D, n) for d, k in zip(_D, n)]      # camera projetee dans le plan
    w = _norm(w)
    mid = math.degrees(math.atan2(_dot(w, v), _dot(w, u)))
    half = span / 2.0
    a0, a1 = (mid + half, mid - half) if clockwise else (mid - half, mid + half)
    c = _mul(n, depth)
    pts = []
    steps = 28
    for i in range(steps + 1):
        t = math.radians(a0 + (a1 - a0) * i / steps)
        pts.append(_add(c, _add(_mul(u, radius * math.cos(t)),
                                _mul(v, radius * math.sin(t)))))
    return pts


def turn_points(face, clockwise=True, span=SPAN_QUARTER, radius=R_FACE, depth=1.92):
    """Le meme arc, projete a l'ecran."""
    return [project(p) for p in arc3(face, clockwise, span, radius, depth)]



def move_arcs_3d(token):
    """Arcs EN 3D montrant ce que fait UN mouvement — deduits de `MOVES`, la
    table du moteur. L'axe, les tranches concernees et le sens ne sont donc pas
    ressaisis ici : une fleche ne peut pas contredire le mouvement qu'elle nomme.
    """
    (base, mult), = parse(token)
    axis, layers, q1 = MOVES[base]
    quarters = (q1 * mult) % 4
    assert quarters, 'mouvement sans effet : %r' % token
    n = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}[axis]
    face = NORMAL_TO_FACE[n]
    # quarters compte les quarts de tour HORAIRES autour de l'axe positif :
    # 1 -> horaire, 3 -> antihoraire, 2 -> demi-tour (le sens ne veut rien dire)
    clockwise = quarters != 3
    span = SPAN_HALF if quarters == 2 else SPAN_QUARTER

    if len(layers) == 3:                       # rotation du cube entier
        return [arc3(face, clockwise, SPAN_WHOLE, R_WHOLE, 0.0)]
    out = []
    for lay in sorted(layers, reverse=True):   # de l'axe positif vers l'autre
        if lay == 0:                           # tranche du milieu : on l'encercle
            out.append(arc3(face, clockwise, span, R_SLICE, 0.0))
        else:                                  # face exterieure : arc pose dessus
            out.append(arc3(face, clockwise, span, R_FACE, lay * (1.5 + LIFT)))
    return out


def move_arcs(token):
    """Les memes arcs, projetes a l'ecran."""
    return [[project(p) for p in a] for a in move_arcs_3d(token)]


# --- rendu -----------------------------------------------------------------
def _scene(cube, keep=None, arrows=(), turns=(), arcs=()):
    """Geometrie d'une figure, en unites de cubie — rien n'est encore mis a
    l'echelle. Sert aussi bien a une figure isolee qu'a une vignette de bande,
    ce qui garantit que les deux se dessinent exactement pareil."""
    quads = []
    for (pos, nrm), col in cube.st.items():
        if not visible(nrm):
            continue
        if keep is not None and face_index(pos, nrm) not in keep:
            col = '.'
        c = sticker_center(pos, nrm)
        quads.append((_dot(c, _D), [project(q) for q in sticker_quad(pos, nrm)], col))
    quads.sort(key=lambda q: q[0])            # du plus loin au plus proche

    corners = [(sx * 1.5, sy * 1.5, sz * 1.5)
               for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)]
    body = _hull([project(p) for p in corners])
    return dict(quads=quads, body=body,
                arcs=[turn_points(f, cw) for f, cw in turns] + [list(a) for a in arcs],
                curves=[_travel_2d(a, b) for a, b in arrows])


def _extent(scenes):
    """Boite englobante commune a plusieurs figures.

    Commune, et non par figure : sans ca le cube sauterait d'une vignette a
    l'autre au gre de la place prise par les fleches, et la bande deviendrait
    illisible."""
    geo = []
    for sc in scenes:
        geo += [q for _d, q, _c in sc['quads']] + [sc['body']] + sc['arcs']
        geo += [list(c) for c in sc['curves']]
    xs = [p[0] for g in geo for p in g]
    ys = [p[1] for g in geo for p in g]
    return min(xs), max(xs), min(ys), max(ys)


def _paint(scene, sc, labels=()):
    parts = [_poly([sc(p) for p in scene['body']], BODY, EDGE, 2.0)]
    for _d, quad, col in scene['quads']:
        parts.append(_poly([sc(p) for p in quad], PAINT[col]))
    for pts in scene['arcs']:
        d = 'M %.2f,%.2f' % sc(pts[0]) + ''.join(' L %.2f,%.2f' % sc(p) for p in pts[1:])
        parts += _stroke_pair(d)
    for pa, ctrl, pb in scene['curves']:
        parts += _stroke_pair('M %.2f,%.2f Q %.2f,%.2f %.2f,%.2f'
                              % (sc(pa) + sc(ctrl) + sc(pb)))
    for face, text in labels:
        x, y = sc(project(_mul(NORMALS[face], 1.62)))
        parts.append(_text(x, y, text, 30))
    return parts


def _text(x, y, txt, size, weight=700):
    return ('<text x="%.1f" y="%.1f" text-anchor="middle" '
            'dominant-baseline="central" font-family="system-ui,sans-serif" '
            'font-size="%d" font-weight="%d" fill="%s" stroke="%s" '
            'stroke-width="4" paint-order="stroke">%s</text>'
            % (x, y, size, weight, CHALK, INK, _esc(txt)))


def _esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _svg(w, h, parts, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
            'width="%.0f" height="%.0f" role="img" aria-label="%s">'
            '<title>%s</title>%s</svg>'
            % (w, h, w, h, _esc(title), _esc(title), ''.join(parts)))


def render3d(cube, title='Cube', keep=None, arrows=(), turns=(), labels=(), cam=CAM):
    """Vue isometrique du cube.

    keep    : ensemble de (face, index) a garder en couleur (le reste grise)
    arrows  : liste de ((pos,nrm), (pos,nrm)) — trajets de pieces
    turns   : liste de (face, clockwise) — sens d'un mouvement
    labels  : liste de (face, texte) — lettre posee au centre de la face
    cam     : point de vue (CAM par defaut, CAM_BAS pour voir la couche du bas)
    """
    set_camera(cam)
    try:
        scene = _scene(cube, keep, arrows, turns)
        minx, maxx, miny, maxy = _extent([scene])
        w = (maxx - minx) * SCALE + 2 * PAD
        h = (maxy - miny) * SCALE + 2 * PAD

        def sc(p):
            return ((p[0] - minx) * SCALE + PAD, (p[1] - miny) * SCALE + PAD)

        parts = ['<rect x="0" y="0" width="%.1f" height="%.1f" rx="8" fill="%s"/>'
                 % (w, h, BODY)]
        parts += _paint(scene, sc, labels)
        if scene['arcs'] or scene['curves']:
            parts.insert(1, _arrow_defs())
        return _svg(w, h, parts, title)
    finally:
        set_camera()


# --- bande de vignettes ----------------------------------------------------
CELL = 132.0        # largeur d'une vignette a l'ecran, en pixels
CELL_GAP = 7.0
CAPTION = 30.0      # bandeau du nom du mouvement, sous la vignette
MAX_COLS = 6


def filmstrip(alg, start, title='', last='', cam=CAM):
    """Bande « pas a pas » : une vignette par mouvement, montrant l'etat AVANT
    de tourner, la fleche du mouvement en cours et son nom.

    Les etats comme les fleches sont calcules en deroulant `alg` sur `start`
    avec le moteur : la bande ne peut donc pas raconter autre chose que
    l'algorithme qu'elle illustre. Une derniere vignette montre le resultat.
    """
    set_camera(cam)
    try:
        return _filmstrip(alg, start, title, last)
    finally:
        set_camera()


def _filmstrip(alg, start, title, last):
    cube = start.copy()
    scenes, caps = [], []
    for tok in alg.split():
        scenes.append(_scene(cube, arcs=move_arcs(tok)))
        caps.append(tok)
        cube = cube.copy().apply(tok)
    scenes.append(_scene(cube))                 # le resultat, sans fleche
    caps.append(last)

    minx, maxx, miny, maxy = _extent(scenes)
    n = len(scenes)
    rows = (n + MAX_COLS - 1) // MAX_COLS
    cols = (n + rows - 1) // rows               # rangees equilibrees
    k = (CELL - 2 * PAD) / (maxx - minx)        # pixels par unite de cubie
    ch = (maxy - miny) * k + 2 * PAD            # hauteur de la partie cube
    cellh = ch + CAPTION
    w = cols * CELL + (cols - 1) * CELL_GAP
    h = rows * cellh + (rows - 1) * CELL_GAP

    def sc(p):                                   # coordonnees internes a l'echelle SCALE
        return ((p[0] - minx) * SCALE + PAD * SCALE / k,
                (p[1] - miny) * SCALE + PAD * SCALE / k)

    parts = [_arrow_defs()]
    for i, (scene, cap) in enumerate(zip(scenes, caps)):
        ox = (i % cols) * (CELL + CELL_GAP)
        oy = (i // cols) * (cellh + CELL_GAP)
        parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" '
                     'fill="%s"/>' % (ox, oy, CELL, cellh, BODY))
        # le contenu est dessine a l'echelle native puis reduit : les epaisseurs
        # de trait et les pointes de fleche gardent donc les memes proportions
        parts.append('<g transform="translate(%.2f,%.2f) scale(%.4f)">' % (ox, oy, k / SCALE))
        parts += _paint(scene, sc)
        parts.append('</g>')
        parts.append(_text(ox + CELL / 2.0, oy + ch + CAPTION / 2.0 - 2, cap, 20))
    return _svg(w, h, parts, title)
