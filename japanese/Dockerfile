FROM papaeye/texlive:slim
MAINTAINER papaeye@gmail.com

RUN tlmgr install \
		adobemapping \
		cjk-gs-integrate \
		cjkpunct \
		cjkutils \
		dnp \
		xcjk2uni \
		convbkmk \
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
	&& rm /texlive/tlpkg/texlive.tlpdb.*

ENTRYPOINT ["ptex2pdf"]
