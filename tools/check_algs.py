import json, sys
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from cube import solved, is_ll_alg, case_state, canonical, parse

DATA = os.path.join(_HERE, '..', 'data', '%s.json')
bad = []


def audit(kind, expected):
    rows = json.load(open(DATA % kind, encoding='utf-8'))
    print('=== %s : %d entrees (attendu %d) ===' % (kind.upper(), len(rows), expected))
    sigs = {}
    for cid, name, alg, grp in rows:
        try:
            parse(alg)
        except ValueError as e:
            print('  SYNTAXE  %-4s %s' % (cid, e)); bad.append(cid); continue
        if not is_ll_alg(alg):
            print('  CASSE F2L %-4s %-28s %s' % (cid, name, alg)); bad.append(cid); continue
        st = case_state(alg)
        if kind == 'pll' and not all(c == 'Y' for c in st.facelets()['U']):
            print('  PAS PUR   %-4s %s (oriente mal la couche)' % (cid, name)); bad.append(cid); continue
        if kind == 'oll' and all(c == 'Y' for c in st.facelets()['U']):
            print('  DEJA FAIT %-4s %s (cas resolu)' % (cid, name)); bad.append(cid); continue
        sig = canonical(alg, kind)
        if sig in sigs:
            print('  DOUBLON   %-4s %-24s == %s' % (cid, name, sigs[sig])); bad.append(cid); continue
        sigs[sig] = cid
    print('  -> %d cas distincts / %d attendus' % (len(sigs), expected))
    return len(sigs) == expected


ok_oll = audit('oll', 57)
print()
ok_pll = audit('pll', 21)
print()
if bad:
    print('ALGOS A CORRIGER : %s' % ', '.join(bad)); sys.exit(1)
if ok_oll and ok_pll:
    print('COMPLETUDE PROUVEE : 57 OLL + 21 PLL, tous distincts, tous valides.')
