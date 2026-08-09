# -*- coding: utf-8 -*-
"""Bascule le site d'un domaine a l'autre, en refusant de le faire trop tot.

Changer le domaine dans les fichiers avant que le nouveau ne reponde ferait
pointer les balises canonical, les hreflang et les sitemaps vers un hote
injoignable : c'est exactement ce qui fait perdre un referencement. Ce script
verifie donc d'abord que le nouveau domaine est bien servi, puis reecrit les
quelques endroits ou le domaine apparait.

    python3 tools/switch_domain.py rubiks.coality.net
    python3 tools/switch_domain.py rubiks.coality.net --force   # sans les gardes
"""
import os
import re
import socket
import ssl
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(_HERE, '..'))
OLD = 'rubik.coality.net'

FILES = ['mkdocs.yml', 'mkdocs.en.yml', 'mkdocs.bis.yml',
         'tools/seo.py', 'README.md', 'CLAUDE.md']


def resolves(host):
    try:
        return socket.gethostbyname(host)
    except OSError:
        return None


def https_ok(host):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=8) as sock:
            with ctx.wrap_socket(sock, server_hostname=host):
                return True
    except Exception as exc:
        return str(exc)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    new = sys.argv[1]
    force = '--force' in sys.argv

    ip = resolves(new)
    if not ip:
        print('ARRET : %s ne resout pas encore.' % new)
        print('  Ajouter un enregistrement DNS A  %s -> %s' % (new, resolves(OLD) or '<ip>'))
        if not force:
            sys.exit(1)
    else:
        print('DNS   : %s -> %s' % (new, ip))
        mine = resolves(OLD)
        if mine and ip != mine:
            print('ATTENTION : %s pointe ailleurs que %s (%s)' % (new, OLD, mine))
            if not force:
                sys.exit(1)

    tls = https_ok(new)
    if tls is not True:
        print('ARRET : pas de HTTPS valide sur %s (%s)' % (new, tls))
        print('  Lancer d\'abord :  sudo ./migrate-domain.sh %s' % new)
        if not force:
            sys.exit(1)
    else:
        print('HTTPS : certificat valide sur %s' % new)

    n = 0
    for rel in FILES:
        p = os.path.join(ROOT, rel)
        s = open(p, encoding='utf-8').read()
        if OLD not in s:
            continue
        open(p, 'w', encoding='utf-8').write(s.replace(OLD, new))
        n += s.count(OLD)
        print('  reecrit : %s' % rel)
    print('%d occurrences remplacees. Relancer ./build.sh.' % n)


if __name__ == '__main__':
    main()
