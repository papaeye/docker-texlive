FROM debian:jessie
MAINTAINER papaeye@gmail.com

RUN apt-get update \
	&& apt-get install -y --no-install-recommends perl wget \
	&& rm -rf /var/lib/apt/lists/*

COPY texlive.profile /tmp/

RUN mkdir /usr/src/install-tl \
	&& wget -qO- http://mirrors.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
		| tar -xzC /usr/src/install-tl --strip-components=1 \
	&& /usr/src/install-tl/install-tl -profile /tmp/texlive.profile -scheme full \
	&& rm /tmp/texlive.profile \
	&& rm -rf /usr/src/install-tl

ENV PATH /texlive/bin/x86_64-linux:$PATH

RUN mkdir /data
WORKDIR /data
