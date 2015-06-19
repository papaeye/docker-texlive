#!/usr/bin/env python
import os
import os.path
import shutil

from jinja2 import Environment, FileSystemLoader


here = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(here))

profile = os.path.join(here, 'texlive.profile')

tags = dict(
    basic=dict(
        scheme='basic',
    ),
    full=dict(
        scheme='full',
    ),
    japanese=dict(
        scheme='basic',
        packages=[
            'collection-fontsrecommended',
            'collection-latexrecommended',
            # collection-langcjk
            'adobemapping',
            'cjk-gs-integrate',
            'cjkpunct',
            'cjkutils',
            'dnp',
            'xcjk2uni',
            # collection-langjapanese
            'convbkmk',
            'japanese',
            'japanese-otf',
            'japanese-otf-uptex',
            'jfontmaps',
            'jsclasses',
            'ptex',
            'ptex2pdf',
            'pxbase',
            'pxchfon',
            'pxcjkcat',
            'pxjahyper',
            'pxrubrica',
            'uptex',
            # useful packages (for me)
            'bera',
            'etoolbox',
        ],
    ),
)


def main():
    template = env.get_template('Dockerfile.jinja2')

    for tag, context in tags.items():
        if not os.path.exists(tag):
            os.mkdir(tag)
        shutil.copy2(profile, tag)
        template.stream(context).dump(os.path.join(tag, 'Dockerfile'))


if __name__ == '__main__':
    main()
