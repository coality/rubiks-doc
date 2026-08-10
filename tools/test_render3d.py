# -*- coding: utf-8 -*-
"""Auto-tests du rendu 3D : les fleches doivent dire exactement ce que fait le
moteur. Une fleche a l'envers est un bug silencieux (le schema reste joli), donc
on la verifie mecaniquement, face par face.
"""
import math
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from cube import Cube, NORMALS, MOVES, AXIS_IDX, solved, parse
from render3d import (basis, arc3, travel, project, sticker_center, move_arcs_3d,
                      filmstrip, R_SLICE, SPAN_QUARTER, _dot)

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
            pts3 = arc3(face, cw)
            a0 = math.degrees(math.atan2(_dot(pts3[0], v), _dot(pts3[0], u)))
            a1 = math.degrees(math.atan2(_dot(pts3[-1], v), _dot(pts3[-1], u)))
            d = (a1 - a0 + 180.0) % 360.0 - 180.0
            check((d < 0) == cw,
                  "%s%s : arc dans le mauvais sens (delta %.0f deg)"
                  % (face, '' if cw else "'", d))


def test_arc_is_on_the_visible_side():
    """L'arc doit etre devant, sinon la fleche passe derriere le cube."""
    from render3d import _D
    for face in ('U', 'F', 'R'):
        for p in arc3(face, True):
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


# --- mouvements dessines pas a pas ----------------------------------------
# tous les mouvements que le site illustre, primes et demi-tours compris
TOKENS = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2",
          "F", "F'", "F2", "B", "B'", "M", "M'", "M2", "r", "r'", "l", "u",
          "x", "x'", "y", "y'", "z"]


def _axis_angle(axis, p):
    """Direction d'un point autour d'un axe, en degres, dans le plan normal."""
    n = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}[axis]
    u, v = basis(n)
    r = [a - b * _dot(p, n) for a, b in zip(p, n)]
    return math.degrees(math.atan2(_dot(r, v), _dot(r, u)))


def test_move_arcs_match_engine():
    """Pour chaque mouvement, l'arc dessine tourne dans le sens ou le moteur
    fait tourner les autocollants concernes. C'est LA verification qui empeche
    une bande « pas a pas » de montrer un mouvement a l'envers."""
    for tok in TOKENS:
        (base, mult), = parse(tok)
        axis, layers, q1 = MOVES[base]
        quarters = (q1 * mult) % 4
        i = AXIS_IDX[axis]

        # des facettes qui tournent vraiment : dans une tranche concernee, et
        # pas sur l'axe (celles-la ne feraient que pivoter sur place)
        starts = [k for k in solved().st
                  if k[0][i] in layers and any(k[0][j] for j in range(3) if j != i)]
        check(starts, '%s : aucune facette a verifier' % tok)

        expected = {1: 270.0, 2: 180.0, 3: 90.0}[quarters]
        for src, dst in travel(tok, starts):
            a0 = _axis_angle(axis, sticker_center(*src))
            a1 = _axis_angle(axis, sticker_center(*dst))
            check(abs((a1 - a0) % 360.0 - expected) < 1e-6,
                  '%s : le moteur emmene une facette de %.0f a %.0f deg '
                  '(delta %.0f, attendu %.0f)'
                  % (tok, a0, a1, (a1 - a0) % 360.0, expected))

        arcs = move_arcs_3d(tok)
        check(arcs, '%s : aucun arc dessine' % tok)
        for arc in arcs:
            # somme des pas : un arc peut depasser 180 deg (demi-tour, rotation),
            # donc on ne peut pas simplement comparer le premier et le dernier
            # point — la difference se replierait et changerait de signe.
            d = sum((_axis_angle(axis, b) - _axis_angle(axis, a) + 180.0) % 360.0 - 180.0
                    for a, b in zip(arc, arc[1:]))
            check((d < 0) == (quarters != 3),
                  "%s : l'arc tourne a l'envers de ce que fait le moteur "
                  '(%.0f deg)' % (tok, d))
            if quarters == 2:       # un demi-tour doit se voir : arc plus long
                check(abs(d) > SPAN_QUARTER + 1e-9,
                      '%s : demi-tour dessine comme un quart de tour (%.0f deg)'
                      % (tok, abs(d)))


def test_move_arcs_show_every_moving_layer():
    """Un mouvement large en dessine deux, une tranche une seule, une rotation
    du cube entier un seul anneau : le lecteur doit voir ce qui bouge."""
    for tok, expected in (('R', 1), ("R'", 1), ('M', 1), ('r', 2), ('l', 2),
                          ('u', 2), ('x', 1), ('y', 1)):
        check(len(move_arcs_3d(tok)) == expected,
              '%s : %d arc(s), %d attendu(s)' % (tok, len(move_arcs_3d(tok)), expected))


def test_arcs_never_pass_inside_the_cube():
    """Un arc qui traverse le cube est illisible : le rayon des tranches doit
    degager la section 3x3 (demi-diagonale 2.12), pas seulement ses faces."""
    check(R_SLICE > 1.5 * math.sqrt(2.0), 'rayon de tranche trop court : %.2f' % R_SLICE)
    for tok in TOKENS:
        for arc in move_arcs_3d(tok):
            for p in arc:
                check(max(abs(c) for c in p) > 1.5 + 1e-9,
                      '%s : un point de l\'arc est a l\'interieur du cube %r' % (tok, p))


def test_filmstrip_follows_the_algorithm():
    """La bande a une vignette par mouvement plus une pour le resultat, et les
    legendes sont exactement les mouvements, dans l'ordre."""
    alg = "R' D' R D"
    svg = filmstrip(alg, solved(), 'test', 'fin')
    caps = re.findall(r'<text[^>]*>([^<]*)</text>', svg)
    check(caps == alg.split() + ['fin'],
          'legendes inattendues : %r' % (caps,))
    # une vignette = un fond arrondi ; 4 mouvements + le resultat
    check(svg.count('rx="8"') == 5, 'nombre de vignettes inattendu')
    # le dernier etat est bien celui du moteur : la bande part du cas et finit resolu
    from cube import case_state, orient_std
    end = case_state(alg).apply(alg)
    check(orient_std(end).is_solved(), 'la bande devrait finir sur un cube resolu')


if __name__ == '__main__':
    test_moves_turn_clockwise()
    test_arc_follows_the_move()
    test_arc_is_on_the_visible_side()
    test_travel_matches_engine()
    test_projection_is_not_degenerate()
    test_move_arcs_match_engine()
    test_move_arcs_show_every_moving_layer()
    test_arcs_never_pass_inside_the_cube()
    test_filmstrip_follows_the_algorithm()
    print('rendu 3D : %d verifications OK' % OK)
