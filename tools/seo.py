# -*- coding: utf-8 -*-
"""Post-traitement SEO du site statique, execute apres les trois builds MkDocs.

Le site est trilingue et servi comme trois sous-sites (/, /en/, /bis/). MkDocs
ne sait pas qu'ils sont traductions l'un de l'autre : ce script ajoute ce qui
manque pour un referencement correct.

  - <link rel="alternate" hreflang> croises entre les trois langues + x-default
    (et suppression de ceux, faux au niveau page, generes par extra.alternate)
  - <html lang="ceb"> sur le site bisaya (MkDocs Material ne connait pas ceb)
  - <meta name="description"> par page, tiree du premier paragraphe
  - Open Graph + Twitter Card par page
  - JSON-LD (WebSite) sur les trois pages d'accueil
  - robots.txt et sitemap.xml (index des trois sitemaps de langue)

Idempotent : le build MkDocs nettoie site/ a chaque fois, et le script ne
reinjecte jamais deux fois (marqueur <!--seo-->).
"""
import html as _html
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(_HERE, '..'))
SITE = ROOT + '/site'
ORIGIN = 'https://rubik.coality.net'
MARK = '<!--seo-->'

# (code, prefixe d'URL, hreflang, code og:locale)
LANGS = [('fr', '', 'fr', 'fr_FR'),
         ('en', 'en/', 'en', 'en_US'),
         ('bis', 'bis/', 'ceb', 'ceb_PH')]

# chemin FR -> chemin commun aux versions en/bis (les slugs y sont en anglais)
PATHS = {
    '': '',
    'notation/': 'notation/',
    'debutant/': 'beginner/',
    'debutant/1-croix-blanche/': 'beginner/1-white-cross/',
    'debutant/2-coins-blancs/': 'beginner/2-white-corners/',
    'debutant/3-deuxieme-couronne/': 'beginner/3-second-layer/',
    'debutant/4-croix-jaune/': 'beginner/4-yellow-cross/',
    'debutant/5-aretes-jaunes/': 'beginner/5-yellow-edges/',
    'debutant/6-coins-places/': 'beginner/6-corners-placed/',
    'debutant/7-coins-orientes/': 'beginner/7-corners-oriented/',
    'cfop/': 'cfop/',
    'cfop/croix/': 'cfop/cross/',
    'cfop/f2l/': 'cfop/f2l/',
    'cfop/4lll/': 'cfop/4lll/',
    'avance/oll/': 'advanced/oll/',
    'avance/pll/': 'advanced/pll/',
    'avance/f2l/': 'advanced/f2l/',
    'vitesse/': 'speed/',
    'depannage/': 'troubleshooting/',
    'glossaire/': 'glossary/',
}

SITE_NAME = {'fr': "Résoudre le Rubik's Cube",
             'en': "Solving the Rubik's Cube",
             'bis': "Pagsulbad sa Rubik's Cube"}


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def save(p, s):
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(s)


def text_of(fragment):
    """Texte brut d'un fragment HTML, espaces normalises."""
    t = re.sub(r'<[^>]+>', '', fragment)
    return re.sub(r'\s+', ' ', _html.unescape(t)).strip()


def first_paragraph(doc):
    """Premier vrai paragraphe de l'article, pour la meta description."""
    art = re.search(r'<article[^>]*>(.*?)</article>', doc, re.S)
    body = art.group(1) if art else doc
    for m in re.finditer(r'<p>(.*?)</p>', body, re.S):
        t = text_of(m.group(1))
        if len(t) >= 60:
            return t
    return ''


def clip(t, n=155):
    if len(t) <= n:
        return t
    cut = t[:n]
    sp = cut.rfind(' ')
    return (cut[:sp] if sp > 60 else cut).rstrip(' ,;:') + '…'


def page_title(doc):
    m = re.search(r'<title>(.*?)</title>', doc, re.S)
    return text_of(m.group(1)) if m else ''


def url_for(lang_prefix, fr_path):
    common = PATHS[fr_path]
    return '%s/%s%s' % (ORIGIN, lang_prefix, common if lang_prefix else fr_path)


def file_for(code, fr_path):
    common = PATHS[fr_path]
    if code == 'fr':
        sub = fr_path
    else:
        sub = ('en/' if code == 'en' else 'bis/') + common
    return os.path.join(SITE, sub, 'index.html')


def inject(code, prefix, hreflang, locale, fr_path):
    path = file_for(code, fr_path)
    if not os.path.exists(path):
        print('  ! manquant : %s' % path)
        return False
    doc = read(path)
    if MARK in doc:
        return True

    canonical = url_for(prefix, fr_path)
    desc = clip(first_paragraph(doc))
    title = page_title(doc)

    # Material derive des <link rel="alternate"> de extra.alternate, mais ils
    # pointent tous vers les pages d'accueil : faux au niveau de la page, et en
    # conflit avec les notres. On les retire avant d'injecter les bons.
    doc = re.sub(r'<link rel="alternate" href="[^"]*" hreflang="[^"]*">', '', doc)

    tags = [MARK]
    for c2, p2, hl2, _lc in LANGS:
        tags.append('<link rel="alternate" hreflang="%s" href="%s">'
                    % (hl2, url_for(p2, fr_path)))
    tags.append('<link rel="alternate" hreflang="x-default" href="%s">'
                % url_for('', fr_path))
    if desc:
        tags.append('<meta property="og:description" content="%s">'
                    % _html.escape(desc, quote=True))
        tags.append('<meta name="twitter:description" content="%s">'
                    % _html.escape(desc, quote=True))
    tags += ['<meta property="og:type" content="article">',
             '<meta property="og:site_name" content="%s">' % _html.escape(SITE_NAME[code]),
             '<meta property="og:locale" content="%s">' % locale,
             '<meta property="og:title" content="%s">' % _html.escape(title, quote=True),
             '<meta property="og:url" content="%s">' % canonical,
             '<meta name="twitter:card" content="summary">',
             '<meta name="twitter:title" content="%s">' % _html.escape(title, quote=True)]

    if fr_path == '':
        tags.append(
            '<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"WebSite","name":"%s","url":"%s","inLanguage":"%s"}</script>'
            % (SITE_NAME[code].replace('"', '\\"'), canonical, hreflang))

    # description : MkDocs met celle du site, on la remplace par celle de la page
    if desc:
        doc, n = re.subn(r'<meta name="description" content="[^"]*">',
                         '<meta name="description" content="%s">'
                         % _html.escape(desc, quote=True), doc, count=1)
        if not n:
            tags.append('<meta name="description" content="%s">'
                        % _html.escape(desc, quote=True))

    doc = doc.replace('</head>', ''.join(tags) + '</head>', 1)
    save(path, doc)
    return True


def fix_lang_attribute():
    """Material ne connait pas le cebuano : le site bisaya sort en lang="en"."""
    n = 0
    for base, _d, files in os.walk(SITE + '/bis'):
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(base, f)
            doc = read(p)
            new = re.sub(r'(<html[^>]*?)\blang="[a-zA-Z-]+"', r'\1lang="ceb"', doc, count=1)
            if new != doc:
                save(p, new)
                n += 1
    return n


def write_robots():
    save(SITE + '/robots.txt',
         'User-agent: *\n'
         'Allow: /\n'
         '\n'
         'Sitemap: %s/sitemap.xml\n' % ORIGIN)


def write_sitemap_index():
    """MkDocs ecrit un sitemap par langue. On expose un index a la racine.

    Le sitemap francais est deplace en /sitemap-fr.xml pour liberer le nom
    canonique /sitemap.xml, qui devient l'index des trois."""
    fr = SITE + '/sitemap.xml'
    if os.path.exists(fr):
        os.replace(fr, SITE + '/sitemap-fr.xml')
    if os.path.exists(SITE + '/sitemap.xml.gz'):
        os.replace(SITE + '/sitemap.xml.gz', SITE + '/sitemap-fr.xml.gz')
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc in ('/sitemap-fr.xml', '/en/sitemap.xml', '/bis/sitemap.xml'):
        parts.append('<sitemap><loc>%s%s</loc></sitemap>' % (ORIGIN, loc))
    parts.append('</sitemapindex>')
    save(SITE + '/sitemap.xml', '\n'.join(parts) + '\n')


def main():
    if not os.path.isdir(SITE):
        sys.exit('site/ absent : lancer le build MkDocs avant seo.py')
    ok = 0
    missing = 0
    for fr_path in PATHS:
        for code, prefix, hreflang, locale in LANGS:
            if inject(code, prefix, hreflang, locale, fr_path):
                ok += 1
            else:
                missing += 1
    n = fix_lang_attribute()
    write_robots()
    write_sitemap_index()
    print('SEO : %d pages annotees (hreflang + OG + description), '
          'lang="ceb" sur %d fichiers, robots.txt + sitemap index ecrits' % (ok, n))
    if missing:
        sys.exit('SEO : %d pages attendues sont absentes du site' % missing)


if __name__ == '__main__':
    main()
