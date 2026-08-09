"""Rendu SVG des etats de cube. Zero dependance, zero ressource externe.

Deux vues :
  - render_net()  : cube deplie (patron en croix), pour la methode debutant
  - render_ll()   : vue de dessus + bandeaux lateraux, standard OLL/PLL
Le corps du cube est dessine en gris fonce : lisible en theme clair comme sombre.
"""
from cube import face_index

PAINT = {
    'Y': '#f5cf2e', 'W': '#f4f4f1', 'G': '#2ea44f',
    'B': '#2f6fd0', 'O': '#ef8b22', 'R': '#d0342c',
    '.': '#8a9099',            # facette masquee (non pertinente a cette etape)
}
BODY = '#23262c'
EDGE = '#15171b'

S = 26      # cote d'un autocollant
G = 4       # espace entre autocollants
T = 11      # epaisseur des bandeaux lateraux
P = 6       # marge interne du corps


def _sticker(x, y, col, w=S, h=S):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" '
            'fill="%s" stroke="%s" stroke-width="1.2"/>') % (x, y, w, h, PAINT[col], EDGE)


def _body(x, y, w, h):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="7" '
            'fill="%s"/>') % (x, y, w, h, BODY)


def _svg(w, h, parts, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.0f %.0f" '
            'width="%.0f" height="%.0f" role="img" aria-label="%s">'
            '<title>%s</title>%s</svg>') % (w, h, w, h, title, title, ''.join(parts))


def _grid(fl, face, ox, oy, keep=None):
    out = []
    for i in range(9):
        col = fl[face][i]
        if keep is not None and (face, i) not in keep:
            col = '.'
        out.append(_sticker(ox + (i % 3) * (S + G), oy + (i // 3) * (S + G), col))
    return out


def render_net(cube, keep=None, title='Etat du cube'):
    """Patron deplie :   U
                       L F R B
                         D
    `keep` = ensemble de (face, index) a garder en couleur ; le reste est grise.
    """
    fl = cube.facelets()
    blk = 3 * S + 2 * G          # cote d'une face
    gap = 10
    w = 4 * blk + 3 * gap + 2 * P
    h = 3 * blk + 2 * gap + 2 * P
    parts = [_body(0, 0, w, h)]
    col_x = [P + i * (blk + gap) for i in range(4)]
    row_y = [P + i * (blk + gap) for i in range(3)]
    parts += _grid(fl, 'U', col_x[1], row_y[0], keep)
    for k, f in enumerate(['L', 'F', 'R', 'B']):
        parts += _grid(fl, f, col_x[k], row_y[1], keep)
    parts += _grid(fl, 'D', col_x[1], row_y[2], keep)
    return _svg(w, h, parts, title)


def render_ll(cube, mode='pll', arrows=None, title='Derniere couche'):
    """Vue de dessus (face U) entouree des rangees hautes de F/R/B/L.
    mode='oll' : seule l'orientation compte -> jaune vs gris.
    """
    fl = cube.facelets()
    blk = 3 * S + 2 * G
    w = h = blk + 2 * (T + 4) + 2 * P
    o = P + T + 4                       # origine de la face U
    parts = [_body(0, 0, w, h)]

    def col_of(c):
        if mode == 'oll':
            return 'Y' if c == 'Y' else '.'
        return c

    for i in range(9):
        parts.append(_sticker(o + (i % 3) * (S + G), o + (i // 3) * (S + G),
                              col_of(fl['U'][i])))
    # bandeaux : ordre deduit de la geometrie (cf. cube.face_index)
    for k, i in enumerate([0, 1, 2]):                       # B au-dessus, inverse
        parts.append(_sticker(o + k * (S + G), P, col_of(fl['B'][2 - i]), S, T))
    for k, i in enumerate([0, 1, 2]):                       # F en dessous
        parts.append(_sticker(o + k * (S + G), o + blk + 4, col_of(fl['F'][i]), S, T))
    for k, i in enumerate([0, 1, 2]):                       # L a gauche
        parts.append(_sticker(P, o + k * (S + G), col_of(fl['L'][i]), T, S))
    for k, i in enumerate([0, 1, 2]):                       # R a droite, inverse
        parts.append(_sticker(o + blk + 4, o + k * (S + G), col_of(fl['R'][2 - i]), T, S))

    if arrows:
        parts.append('<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" '
                     'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
                     '<path d="M0,1 L9,5 L0,9 z" fill="#15171b"/></marker></defs>')
        for (i, j) in arrows:
            x1 = o + (i % 3) * (S + G) + S / 2
            y1 = o + (i // 3) * (S + G) + S / 2
            x2 = o + (j % 3) * (S + G) + S / 2
            y2 = o + (j // 3) * (S + G) + S / 2
            parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                         'stroke="#15171b" stroke-width="3.2" stroke-linecap="round" '
                         'marker-end="url(#a)" opacity="0.85"/>' % (x1, y1, x2, y2))
    return _svg(w, h, parts, title)


def pll_arrows(alg):
    """Fleches de permutation, calculees depuis l'algo lui-meme.

    On etiquette chaque autocollant par sa position resolue, on genere le cas
    (inverse de l'algo) et on lit ou chaque piece de la couche U doit aller.
    """
    from cube import Cube, invert
    c = Cube()
    for key in list(c.st):
        f, i = face_index(*key)
        c.st[key] = (f, i)
    c.apply(invert(alg))
    fl = c.facelets()
    out = []
    for i in (0, 1, 2, 3, 5, 6, 7, 8):
        lbl = fl['U'][i]
        if lbl[0] == 'U' and lbl[1] != i:
            out.append((i, lbl[1]))
    return out
