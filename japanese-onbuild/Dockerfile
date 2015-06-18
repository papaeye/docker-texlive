FROM papaeye/texlive:japanese
MAINTAINER papaeye@gmail.com

ONBUILD COPY fonts /texlive/texmf-local/fonts/opentype/
ONBUILD RUN mktexlsr
