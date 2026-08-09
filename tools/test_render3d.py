# -*- coding: utf-8 -*-
"""Auto-tests du rendu 3D : les fleches doivent dire exactement ce que fait le
moteur. Une fleche a l'envers est un bug silencieux (le schema reste joli), donc
on la verifie mecaniquement, face par face.
"""
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from cube import Cube, NORMALS, solved
from render3d import basis, turn_points, travel, project, sticker_center, _dot, _norm

OK = 0


def check(cond, msg):
    global OK
    assert cond, 'ECHEC : ' + msg
    OK += 1


def angle_in_face(face, pos, nrm):
    """Direction d'une facette dans le plan de sa face, en degres."""
    n = NORMALS[face]
    u, v = basis(n)
    c = sticker_center(pos, nrm)
    r = [a - b * _dot(c, n) for a, b in zip(c, n)]
    return math.degrees(math.atan2(_dot(r, v), _dot(r, u))) % 360.0


def test_moves_turn_clockwise():
    """Un mouvement sans prime fait tourner sa face de -90 degres (horaire vu
    de l'exterieur) : c'est la convention sur laquelle turn_points() s'appuie."""
    for face in ('U', 'D', 'F', 'B', 'R', 'L'):
        n = NORMALS[face]
        # les 4 aretes de cette face
        starts = [k for k in solved().st
                  if k[1] == n and sum(1 for c in k[0] if c != 0) == 2]
        check(len(starts) == 4, '%s : 4 aretes attendues, %d' % (face, len(starts)))
        for src, dst in travel(face, starts):
            a0 = angle_in_face(face, *src)
            a1 = angle_in_face(face, *dst)
            d = (a1 - a0) % 360.0
            check(abs(d - 270.0) < 1e-6,
                  '%s : la facette a %.0f deg va a %.0f deg (delta %.0f, attendu 270 '
                  '= -90 horaire)' % (face, a0, a1, d))


def test_arc_follows_the_move():
    """L'arc dessine doit parcourir la face dans le sens du mouvement."""
    for face in ('U', 'D', 'F', 'B', 'R', 'L'):
        n = NORMALS[face]
        u, v = basis(n)
        for cw in (True, False):
            pts3 = _arc_3d(face, cw)
            a0 = math.degrees(math.atan2(_dot(pts3[0], v), _dot(pts3[0], u)))
            a1 = math.degrees(math.atan2(_dot(pts3[-1], v), _dot(pts3[-1], u)))
            d = (a1 - a0 + 180.0) % 360.0 - 180.0
            check((d < 0) == cw,
                  "%s%s : arc dans le mauvais sens (delta %.0f deg)"
                  % (face, '' if cw else "'", d))


def _arc_3d(face, cw, span=150.0, radius=0.95):
    """Memes points que turn_points(), mais gardes en 3D pour le test."""
    n = NORMALS[face]
    u, v = basis(n)
    from render3d import _D
    w = _norm([d - k * _dot(_D, n) for d, k in zip(_D, n)])
    mid = math.degrees(math.atan2(_dot(w, v), _dot(w, u)))
    half = span / 2.0
    a0, a1 = (mid + half, mid - half) if cw else (mid - half, mid + half)
    out = []
    for i in range(3):
        t = math.radians(a0 + (a1 - a0) * i / 2.0)
        out.append(tuple(u[k] * radius * math.cos(t) + v[k] * radius * math.sin(t)
                         for k in range(3)))
    return out


def test_arc_is_on_the_visible_side():
    """L'arc doit etre devant, sinon la fleche passe derriere le cube."""
    from render3d import _D
    for face in ('U', 'F', 'R'):
        for p in _arc_3d(face, True):
            check(_dot(p, _D) > -0.5,
                  "%s : un point de l'arc est derriere le cube" % face)


def test_travel_matches_engine():
    """Les fleches de trajet sont bien celles calculees par le moteur."""
    # F2 descend le petale avant : facette avant de l'arete UF -> face D
    (src, dst), = travel('F2', [((0, 1, 1), (0, 0, 1))])
    check(dst == ((0, -1, 1), (0, 0, 1)), 'F2 : arrivee inattendue %r' % (dst,))
    # R fait monter la facette avant-droite sur la face du haut
    (src, dst), = travel('R', [((1, 0, 1), (0, 0, 1))])
    check(dst[1] == (0, 1, 0), 'R : la facette avant-droite devrait finir en haut')
    # un algo complet ne peut pas mentir : depart != arrivee
    pairs = travel("U R U' R' U' F' U F", [((0, 1, 1), (0, 0, 1))])
    check(pairs[0][0] != pairs[0][1], 'insertion droite : la piece devrait bouger')


def test_projection_is_not_degenerate():
    """Bug corrige une fois : les quads projetes doivent avoir une aire non nulle."""
    from render3d import sticker_quad
    for (pos, nrm) in solved().st:
        pts = [project(p) for p in sticker_quad(pos, nrm)]
        area = abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1]
                       for i in range(4))) / 2.0
        check(area > 0.05, 'facette %r : quad projete degenere (aire %.3f)' % ((pos, nrm), area))


if __name__ == '__main__':
    test_moves_turn_clockwise()
    test_arc_follows_the_move()
    test_arc_is_on_the_visible_side()
    test_travel_matches_engine()
    test_projection_is_not_degenerate()
    print('rendu 3D : %d verifications OK' % OK)
