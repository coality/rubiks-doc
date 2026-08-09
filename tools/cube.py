"""Moteur de Rubik's cube 3x3 — modele geometrique (position, normale).

Chaque autocollant est repere par (position, normale) dans {-1,0,1}^3.
Un mouvement = rotation d'une ou plusieurs tranches. Les indices de facettes
sont deduits de la geometrie, donc aucune table de cycles a recopier (et donc
aucune faute de frappe possible dans les permutations).

Reperes : x droite, y haut, z vers l'observateur (avant).
Schema de couleurs : U jaune, D blanc, F vert, B bleu, R orange, L rouge.
"""

FACES = ['U', 'R', 'F', 'D', 'L', 'B']

NORMALS = {
    'U': (0, 1, 0), 'D': (0, -1, 0),
    'R': (1, 0, 0), 'L': (-1, 0, 0),
    'F': (0, 0, 1), 'B': (0, 0, -1),
}
NORMAL_TO_FACE = {v: k for k, v in NORMALS.items()}

COLORS = {'U': 'Y', 'D': 'W', 'F': 'G', 'B': 'B', 'R': 'O', 'L': 'R'}


# --- rotations elementaires (sens horaire vu depuis l'axe positif) -----------
def _rx(p):  # autour de +x : y'=z, z'=-y
    x, y, z = p
    return (x, z, -y)


def _ry(p):  # autour de +y : x'=-z, z'=x
    x, y, z = p
    return (-z, y, x)


def _rz(p):  # autour de +z : x'=y, y'=-x
    x, y, z = p
    return (y, -x, z)


ROT = {'x': _rx, 'y': _ry, 'z': _rz}
AXIS_IDX = {'x': 0, 'y': 1, 'z': 2}

# mouvement -> (axe, tranches concernees, nb de quarts de tour horaires
#               autour de l'axe POSITIF pour un tour "prime-less")
MOVES = {
    'R': ('x', (1,), 1),      'L': ('x', (-1,), 3),   'M': ('x', (0,), 3),
    'U': ('y', (1,), 1),      'D': ('y', (-1,), 3),   'E': ('y', (0,), 3),
    'F': ('z', (1,), 1),      'B': ('z', (-1,), 3),   'S': ('z', (0,), 1),
    'r': ('x', (1, 0), 1),    'l': ('x', (-1, 0), 3),
    'u': ('y', (1, 0), 1),    'd': ('y', (-1, 0), 3),
    'f': ('z', (1, 0), 1),    'b': ('z', (-1, 0), 3),
    'x': ('x', (1, 0, -1), 1),
    'y': ('y', (1, 0, -1), 1),
    'z': ('z', (1, 0, -1), 1),
}


def face_index(pos, normal):
    """(position, normale) -> (face, index 0..8) selon l'orientation standard."""
    x, y, z = pos
    f = NORMAL_TO_FACE[normal]
    if f == 'U':
        r, c = z + 1, x + 1
    elif f == 'D':
        r, c = 1 - z, x + 1
    elif f == 'F':
        r, c = 1 - y, x + 1
    elif f == 'B':
        r, c = 1 - y, 1 - x
    elif f == 'R':
        r, c = 1 - y, 1 - z
    else:  # L
        r, c = 1 - y, z + 1
    return f, r * 3 + c


class Cube:
    def __init__(self):
        # {(pos, normale): couleur}
        self.st = {}
        for f, n in NORMALS.items():
            for a in (-1, 0, 1):
                for b in (-1, 0, 1):
                    if f in ('U', 'D'):
                        pos = (a, n[1], b)
                    elif f in ('R', 'L'):
                        pos = (n[0], a, b)
                    else:
                        pos = (a, b, n[2])
                    self.st[(pos, n)] = COLORS[f]

    def copy(self):
        c = Cube.__new__(Cube)
        c.st = dict(self.st)
        return c

    def _turn(self, axis, layers, quarters):
        rot = ROT[axis]
        i = AXIS_IDX[axis]
        for _ in range(quarters % 4):
            new = {}
            for (pos, nrm), col in self.st.items():
                if pos[i] in layers:
                    new[(rot(pos), rot(nrm))] = col
                else:
                    new[(pos, nrm)] = col
            self.st = new
        return self

    def apply(self, alg):
        for tok in parse(alg):
            base, quarters = tok
            axis, layers, q1 = MOVES[base]
            self._turn(axis, layers, (q1 * quarters) % 4)
        return self

    def facelets(self):
        """dict face -> liste de 9 couleurs."""
        out = {f: [None] * 9 for f in FACES}
        for (pos, nrm), col in self.st.items():
            f, i = face_index(pos, nrm)
            out[f][i] = col
        return out

    def is_solved(self):
        fl = self.facelets()
        return all(len(set(v)) == 1 for v in fl.values())

    def f2l_intact(self):
        """Vrai si les deux premieres couronnes (tout sauf la couche U) sont
        resolues : c'est le test qui valide qu'un algo est bien un algo de
        derniere couche."""
        fl = self.facelets()
        if len(set(fl['D'])) != 1:
            return False
        for f in ('F', 'R', 'B', 'L'):
            # lignes du milieu et du bas de chaque face laterale
            if len(set(fl[f][3:])) != 1:
                return False
        return True


def parse(alg):
    """'R U2 R'' -> [('R',1), ('U',2), ('R',3)]  (quarts de tour horaires)."""
    toks = []
    for raw in alg.replace('(', ' ').replace(')', ' ').split():
        raw = raw.strip()
        if not raw:
            continue
        base = raw[0]
        if base not in MOVES:
            raise ValueError('mouvement inconnu : %r dans %r' % (raw, alg))
        suf = raw[1:].replace('’', "'")
        if suf in ('', ' '):
            q = 1
        elif suf == "'":
            q = 3
        elif suf == '2':
            q = 2
        elif suf in ("2'", "'2"):
            q = 2
        else:
            raise ValueError('suffixe inconnu : %r dans %r' % (raw, alg))
        toks.append((base, q))
    return toks


def invert(alg):
    out = []
    for base, q in reversed(parse(alg)):
        if q == 1:
            out.append(base + "'")
        elif q == 2:
            out.append(base + '2')
        else:
            out.append(base)
    return ' '.join(out)


def solved():
    return Cube()


def from_case(alg):
    """Etat a reconnaitre : cube resolu auquel on applique l'inverse de l'algo.
    Appliquer `alg` a cet etat le resout donc par construction."""
    return Cube().apply(invert(alg))


# --- orientation canonique ---------------------------------------------------
ORIENTATIONS = [a + (' ' + b if b else '')
                for a in ('', 'x', 'x2', "x'", 'z', "z'")
                for b in ('', 'y', 'y2', "y'")]


def orient_std(cube):
    """Remet le cube dans l'orientation standard (U jaune, F vert) en le
    tournant en bloc. Indispensable : beaucoup d'algos (A-perm, E-perm...)
    contiennent une rotation et laissent le cube tenu autrement."""
    for seq in ORIENTATIONS:
        c = cube.copy().apply(seq) if seq else cube.copy()
        fl = c.facelets()
        if fl['U'][4] == 'Y' and fl['F'][4] == 'G':
            return c
    raise RuntimeError('orientation introuvable')


def is_ll_alg(alg):
    """L'algo n'affecte-t-il QUE la derniere couche ?"""
    return orient_std(solved().apply(alg)).f2l_intact()


def derotate(alg):
    """Ajoute la rotation de bloc qui annule la rotation nette de l'algo.
    Effet physique identique, mais le cube finit tenu comme au depart : sans
    ca, un algo contenant x ou y produit un etat de cas fantaisiste."""
    for seq in ORIENTATIONS:
        c = solved().apply(alg)
        if seq:
            c.apply(seq)
        fl = c.facelets()
        if fl['U'][4] == 'Y' and fl['F'][4] == 'G':
            return (alg + ' ' + seq).strip() if seq else alg
    raise RuntimeError('rotation nette introuvable')


def case_state(alg, pre=0, post=0):
    """Etat a reconnaitre avant d'executer `alg` (avec AUF avant/apres)."""
    alg = derotate(alg)
    c = solved()
    if pre:
        c.apply(' '.join(['U'] * pre))
    c.apply(invert(alg))
    if post:
        c.apply(' '.join(['U'] * post))
    return orient_std(c)


def signature(state, mode):
    fl = state.facelets()
    if mode == 'oll':
        sides = [fl[f][i] for f in ('F', 'R', 'B', 'L') for i in (0, 1, 2)]
        return tuple([s == 'Y' for s in fl['U']] + [s == 'Y' for s in sides])
    return tuple(fl[f][i] for f in ('F', 'R', 'B', 'L') for i in (0, 1, 2))


def canonical(alg, mode):
    """Signature invariante par AUF avant et apres : identifie le CAS."""
    return min(signature(case_state(alg, a, b), mode)
               for a in range(4) for b in range(4))
