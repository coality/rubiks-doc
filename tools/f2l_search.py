"""Algorithmes F2L de la paire avant-droite, calcules par recherche exhaustive.

Profondeur iterative sur <R,U,F> : le premier algorithme trouve pour un cas est
donc le plus court existant dans ce jeu de mouvements. Aucun algo saisi a la main.
"""
import sys, time, json
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from fast import SOLVED, turn, PERM, IDX

MOVES = [m + s for m in 'RUF' for s in ('', "'", '2')]
UP = PERM['U']

FIXED = [IDX[(f, i)] for f, idxs in
         (('D', [0, 1, 3, 4, 5, 6, 7, 8]), ('F', [3, 4, 6, 7]),
          ('R', [4, 5, 7, 8]), ('L', [3, 4, 5, 6, 7, 8]),
          ('B', [3, 4, 5, 6, 7, 8])) for i in idxs]
PAIR = [IDX[k] for k in (('F', 5), ('F', 8), ('R', 3), ('R', 6), ('D', 2))]
PAIR_ID = frozenset(SOLVED[n] for n in PAIR)


def is_case(s):
    for n in FIXED:
        if s[n] != SOLVED[n]:
            return False
    return True


def sig(s):
    """Ou se trouvent les 5 facettes de la paire, a AUF pres."""
    best = None
    cur = s
    for _ in range(4):
        k = tuple(sorted((c, n) for n, c in enumerate(cur) if c in PAIR_ID))
        if best is None or k < best:
            best = k
        cur = ''.join(cur[i] for i in UP)
    return best


def inv(seq):
    return ' '.join(m[:-1] if m.endswith("'") else (m if m.endswith('2') else m + "'")
                    for m in reversed(seq.split()))


found = {}
t0 = time.time()


def dfs(state, depth, path, last):
    if is_case(state):
        k = sig(state)
        if k not in found:
            found[k] = inv(' '.join(path))
    if depth == 0:
        return
    for m in MOVES:
        if m[0] == last:
            continue
        path.append(m)
        dfs(turn(state, m), depth - 1, path, m[0])
        path.pop()


for d in range(0, 10):
    dfs(SOLVED, d, [], '')
    print('profondeur <= %d : %2d cas F2L  (%.0fs)' % (d, len(found), time.time() - t0), flush=True)
    if len(found) >= 41:
        break

rows = sorted(found.values(), key=lambda a: (len(a.split()), a))
print('\n%d cas F2L trouves ; longueurs %d a %d mouvements'
      % (len(rows), len(rows[0].split()), len(rows[-1].split())))
json.dump(rows, open(os.path.join(_HERE, '..', 'data', 'f2l_raw.json'), 'w'), indent=0)
