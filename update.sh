#!/bin/sh
set -e

cd $(dirname $0)

for scheme in basic full; do
    mkdir -p $scheme
    cp texlive.profile $scheme
    sed 's/{{ scheme }}/'$scheme'/' Dockerfile.template > "$scheme/Dockerfile"
done
