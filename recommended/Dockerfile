FROM papaeye/texlive:basic
MAINTAINER papaeye@gmail.com

RUN tlmgr install \
		collection-fontsrecommended \
		collection-latexrecommended \
	&& rm /texlive/tlpkg/texlive.tlpdb.*
