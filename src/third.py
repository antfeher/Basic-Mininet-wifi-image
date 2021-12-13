#!/usr/bin/python

'This example shows how to work with Radius Server'

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.node import UserAP
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi( controller=Controller, accessPoint=UserAP,
                        link=wmediumd, wmediumd_mode=interference )

    info("*** Creating nodes\n")
    h1 = net.addStation( 'h1', radius_passwd='sdnteam', encrypt='wpa2',
                           radius_identity='joe', position='100,100,0' )
    h2 = net.addStation( 'h2', radius_passwd='hello', encrypt='wpa2',
                           radius_identity='bob', position='150,150,0' )
    h3 = net.addStation( 'h3', radius_passwd='hell', encrypt='wpa2',
                           radius_identity='xol', position='100,150,0' )
    ap1 = net.addAccessPoint( 'ap1', ssid='wifi', authmode='8021x',
                              mode='a', channel='36', encrypt='wpa2',
                              position='150,100,0' )
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1',
			 port=6653)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(h1, ap1)
    net.addLink(h2, ap1)

    net.plotGraph(max_x=300, max_y=300)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start( [c0] )

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()













