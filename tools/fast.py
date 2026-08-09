"""Etat = chaine de 54 caracteres UNIQUES (un par facette d'origine).
Les tables de permutation sont DERIVEES du moteur geometrique, jamais saisies.
"""
import sys
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from cube import Cube, FACES, face_index

ORDER = [(f, i) for f in FACES for i in range(9)]
IDX = {k: n for n, k in enumerate(ORDER)}
SOLVED = ''.join(chr(33 + n) for n in range(54))


def perm_of(move):
    c = Cube()
    for key in list(c.st):
        c.st[key] = IDX[face_index(*key)]
    c.apply(move)
    fl = c.facelets()
    return [fl[f][i] for f, i in ORDER]


MOVESET = [m + s for m in 'RUFLDB' for s in ('', "'", '2')]
PERM = {m: perm_of(m) for m in MOVESET}


def turn(state, move):
    p = PERM[move]
    return ''.join(state[i] for i in p)


def apply_seq(state, seq):
    for m in seq.split():
        state = turn(state, m)
    return state
