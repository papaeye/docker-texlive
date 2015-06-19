FROM papaeye/texlive-ja

COPY fonts /texlive/texmf-local/fonts/opentype/
RUN mktexlsr && kanji-config-updmap-sys --jis2004 hiragino-pron
