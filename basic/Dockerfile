FROM buildpack-deps:jessie-curl
MAINTAINER papaeye@gmail.com

COPY texlive.profile /tmp/

RUN apt-get update \
	&& apt-get install -y --no-install-recommends perl \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/src/install-tl \
	&& curl -sSL http://mirrors.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
		| tar -xzC /usr/src/install-tl --strip-components=1 \
	&& /usr/src/install-tl/install-tl -profile /tmp/texlive.profile \
	&& rm /tmp/texlive.profile \
	&& rm -rf /usr/src/install-tl

ENV PATH /texlive/bin/x86_64-linux:$PATH

RUN mkdir /data
VOLUME ["/data"]
WORKDIR /data

ENTRYPOINT ["pdflatex"]
