FROM ubuntu:16.04
USER root

RUN apt-get update
RUN apt-get -y install software-properties-common net-tools wget curl nano \
    sudo gcc make automake git dpkg-dev build-essential iputils-ping

COPY ./src/packages.sh /etc
RUN /etc/packages.sh

RUN git clone git://github.com/intrig-unicamp/mininet-wifi
RUN /mininet-wifi/util/install.sh -Wlnfv 

COPY ./src/first.py /mininet-wifi/examples
COPY ./src/second.py /mininet-wifi/examples
COPY ./src/third.py /mininet-wifi/examples

RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install xfce4
RUN apt-get install dialog && apt-get -y install xfce4-goodies

RUN apt-get -y install tightvncserver
ENV USER=root
COPY ./src/vncserver.py /etc/
RUN  /etc/vncserver.py

CMD service openvswitch-switch start && vncserver && sleep infinity

