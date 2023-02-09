from nmap import nmap
from Infrastructure import Infrastructure
import xml.dom.pulldom as pulldom
import xml.etree.cElementTree as ET

class Scanner:

    def __init__(self, network, interface):
        self.network = network
        self.interface = interface

    def start_scan(self):
        hosts = []
        scanner = nmap.PortScanner()
        scanner.scan(hosts=self.network, arguments=f'-e {self.interface} -sn')

        for ipv4 in scanner.all_hosts():
            host = Infrastructure(ipv4)
            host.start_scan()
            hosts.append(host)

        return hosts

    def test(ipv4):
        infrastucture = Infrastructure(ipv4)
        infrastucture.start_scan()
        return infrastucture
