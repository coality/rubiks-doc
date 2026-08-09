"""Auto-tests du moteur. Aucune dependance externe."""
import sys
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from cube import Cube, solved, invert, parse, FACES

fails = []


def check(name, cond):
    print(('  OK   ' if cond else '  FAIL ') + name)
    if not cond:
        fails.append(name)


print('--- integrite de base ---')
c = solved()
fl = c.facelets()
check('54 facettes', sum(len(v) for v in fl.values()) == 54)
check('aucune facette manquante', all(all(s is not None for s in v) for v in fl.values()))
counts = {}
for v in fl.values():
    for s in v:
        counts[s] = counts.get(s, 0) + 1
check('9 autocollants par couleur', sorted(counts.values()) == [9] * 6)
check('cube neuf resolu', c.is_solved())

print('--- ordre des mouvements (X^4 = identite) ---')
for m in ['U', 'D', 'L', 'R', 'F', 'B', 'M', 'E', 'S', 'r', 'u', 'x', 'y', 'z']:
    check('%s^4 = identite' % m, solved().apply(' '.join([m] * 4)).is_solved())

print('--- inverses ---')
for alg in ["R U R' U'", "F R U R' U' F'", "M2 E2 S2", "r U R' U' r' F R F'"]:
    c = solved().apply(alg).apply(invert(alg))
    check('%-24s puis son inverse = resolu' % alg, c.is_solved())

print('--- identites connues ---')
check("(R U R' U') x6 = identite", solved().apply("R U R' U' " * 6).is_solved())
check("(R U R' U' ) x3 != identite", not solved().apply("R U R' U' " * 3).is_solved())
check("T-perm x2 = identite",
      solved().apply("R U R' U' R' F R2 U' R' U' R U R' F' " * 2).is_solved())
check("(R' D' R D) x6 = identite", solved().apply("R' D' R D " * 6).is_solved())

print('--- geometrie des rotations ---')
# rotation x : la face F doit venir en U
fl = solved().apply('x').facelets()
check("x : vert (F) monte en U", set(fl['U']) == {'G'})
check("x : blanc (D) vient en F", set(fl['F']) == {'W'})
fl = solved().apply('y').facelets()
check("y : orange (R) vient en F", set(fl['F']) == {'O'})
check("y : vert (F) part en L", set(fl['L']) == {'G'})
fl = solved().apply('z').facelets()
check("z : rouge (L) monte en U", set(fl['U']) == {'R'})

print('--- test f2l_intact (le test qui valide les algos LL) ---')
check("F R U R' U' F' preserve les 2 couronnes", solved().apply("F R U R' U' F'").f2l_intact())
check("R U R' U' casse les 2 couronnes", not solved().apply("R U R' U'").f2l_intact())
check("U seul preserve les 2 couronnes", solved().apply("U").f2l_intact())
check("R seul casse les 2 couronnes", not solved().apply("R").f2l_intact())
check("Sune preserve les 2 couronnes", solved().apply("R U R' U R U2 R'").f2l_intact())
check("T-perm preserve les 2 couronnes",
      solved().apply("R U R' U' R' F R2 U' R' U' R U R' F'").f2l_intact())

print()
if fails:
    print('%d ECHEC(S) : %s' % (len(fails), fails))
    sys.exit(1)
print('TOUS LES TESTS PASSENT')
