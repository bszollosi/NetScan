from Scanner import Scanner
import requests
import json

NETWORK = '192.168.0.0/24' #'10.3.13.0/24'
INTERFACE = 'eth0' #'tun0'

Scanner = Scanner(NETWORK, INTERFACE)

ScannedHosts = Scanner.start_scan()

#TestHost = Scanner.test('192.168.0.10')

# todo: write to json.
#with open('json_data.json', 'w') as outfile:
#    json.dump(asd, outfile)
