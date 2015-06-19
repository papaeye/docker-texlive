#!/bin/sh

cd $(dirname $0)/examples

docker run --rm -v $PWD:/data papaeye/texlive-ja               ptex2pdf -u -l japanese && mv japanese.pdf japanese-noembed.pdf
docker run --rm -v $PWD:/data papaeye/texlive-ja:ipaex         ptex2pdf -u -l japanese && mv japanese.pdf japanese-ipaex.pdf
docker run --rm -v $PWD:/data papaeye/texlive-ja:hiragino-pron ptex2pdf -u -l japanese && mv japanese.pdf japanese-hiragino-pron.pdf
