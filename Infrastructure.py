import subprocess
import re
from Software import Software
from StringFunctions import StringFunctions
import uuid


class Infrastructure:

    def __init__(self, ipv4):
        self.id = f'infrastructure--{uuid.uuid4()}'
        self.type = "infrastructure"
        self.spec_version = "2.1"
        self.ipv4 = ipv4
        self.hostName = ''
        self.mac = ''
        self.os = ''
        self.tcpOpen = []
        self.udpOpen = []
        self.installedSoftwares = []

    def start_scan(self):
        print(f'Scanning infrastructure on {self.ipv4 }')
        #self.__snmp_get_softwares()
        self.__snmp_get_mac()
        self.__snmp_get_name()
        self.__snmp_get_os_family()
        self.__snmp_get_tcp_ports()
        self.__snmp_get_udp_ports()

    def __snmp_get_softwares(self):
        snmpwalk_raw = subprocess.run(
            ['snmpwalk', '-v3', '-n', "", '-u', 'RFXHKS', '-a', 'MD5', '-A', 'ujMFw2E8uJ', '-x', 'DES', '-X',
             'ujMFw2E8uJ', '-l', 'authPriv', self.ipv4, '1.3.6.1.2.1.25.6.3.1.2'],
            capture_output=True,
            encoding='utf-8')
        installed_raw_lines = snmpwalk_raw.stdout.split('\n')

        for row in installed_raw_lines:
            try:
                software_name = row.split('"')[1]

                # Get version_substr number from string.
                version_number = StringFunctions.search_version_substr(software_name)

                # Remove version number from software name.
                software_name = re.sub(version_number, "", software_name)

                # Search for archi_substr in raw string. Ex.: (64bit x64)
                archi = StringFunctions.search_archi_substr(software_name)

                # Delete unnecessary chars from raw string.
                software_name = StringFunctions.del_chars_from_softw_name(software_name)

                # New software Instance.
                software = Software(software_name, version_number, archi)
                software.setup_attributes()
                self.installedSoftwares.append(software)

            except IndexError:
                pass

    def __snmp_get_mac(self):
        snmpwalk_raw = subprocess.run(['sudo', '-S', 'nmap', '-sn', self.ipv4], capture_output=True, encoding='utf-8')

        self.mac = snmpwalk_raw.stdout[34:51]

    def __snmp_get_name(self):
        snmpwalk_raw = subprocess.run(
            ['snmpwalk', '-v3', '-n', "", '-u', 'RFXHKS', '-a', 'MD5', '-A', 'ujMFw2E8uJ', '-x', 'DES', '-X',
             'ujMFw2E8uJ', '-l', 'authPriv', self.ipv4, '1.3.6.1.2.1.1.5.0'], capture_output=True, encoding='utf-8')

        self.hostName = snmpwalk_raw.stdout[31:51]

    def __snmp_get_os_family(self):
        snmpwalk_raw = subprocess.run(
            ['snmpwalk', '-v3', '-n', "", '-u', 'RFXHKS', '-a', 'MD5', '-A', 'ujMFw2E8uJ', '-x', 'DES', '-X',
             'ujMFw2E8uJ', '-l', 'authPriv', self.ipv4, '1.3.6.1.2.1.1.1.0'], capture_output=True, encoding='utf-8')

        self.os = snmpwalk_raw.stdout[31:51]

    def __snmp_get_tcp_ports(self):
        snmpwalk_raw = subprocess.run(
            ['snmpwalk', '-v3', '-n', "", '-u', 'RFXHKS', '-a', 'MD5', '-A', 'ujMFw2E8uJ', '-x', 'DES', '-X',
             'ujMFw2E8uJ', '-l', 'authPriv', self.ipv4, '1.3.6.1.2.1.6.13.1.3'],
            capture_output=True,
            encoding='utf-8')
        port_raw_lines = snmpwalk_raw.stdout.split('\n')

        for port in port_raw_lines:
            try:
                self.tcpOpen.append(port.split('INTEGER: ')[1])
            except IndexError:
                pass

    def __snmp_get_udp_ports(self):
        snmpwalk_raw = subprocess.run(
            ['snmpwalk', '-v3', '-n', "", '-u', 'RFXHKS', '-a', 'MD5', '-A', 'ujMFw2E8uJ', '-x', 'DES', '-X',
             'ujMFw2E8uJ', '-l', 'authPriv', self.ipv4, '1.3.6.1.2.1.7.5.1.2'],
            capture_output=True,
            encoding='utf-8')
        port_raw_lines = snmpwalk_raw.stdout.split('\n')

        for port in port_raw_lines:
            try:
                self.udpOpen.append(port.split('INTEGER: ')[1])
            except IndexError:
                pass
