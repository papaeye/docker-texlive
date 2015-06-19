FROM papaeye/texlive:basic
MAINTAINER papaeye@gmail.com

RUN tlmgr install \
		collection-fontsrecommended \
		collection-latexrecommended \
		# collection-langcjk
		adobemapping \
		cjk-gs-integrate \
		cjkpunct \
		cjkutils \
		dnp \
		xcjk2uni \
		convbkmk \
		# collection-langjapanese
		japanese \
		japanese-otf \
		japanese-otf-uptex \
		jfontmaps \
		jsclasses \
		ptex \
		ptex2pdf \
		pxbase \
		pxchfon \
		pxcjkcat \
		pxjahyper \
		pxrubrica \
		uptex \
		# useful packages (for me)
		bera \
		etoolbox \
	&& rm /texlive/tlpkg/texlive.tlpdb.*
