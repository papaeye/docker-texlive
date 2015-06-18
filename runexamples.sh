#!/bin/sh

cd $(dirname $0)/examples

docker run --rm -v $PWD:/data papaeye/texlive:japanese               -u -l japanese && mv japanese.pdf japanese-noembed.pdf
docker run --rm -v $PWD:/data papaeye/texlive:japanese-ipaex         -u -l japanese && mv japanese.pdf japanese-ipaex.pdf
docker run --rm -v $PWD:/data papaeye/texlive:japanese-hiragino-pron -u -l japanese && mv japanese.pdf japanese-hiragino-pron.pdf
