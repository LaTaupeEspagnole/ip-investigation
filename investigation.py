# investigation.py

from utils import *
from traceroute import *
from geoip import *

#class Tor:
#    def __init__(self, ip):
#        self.ip = ip
#
#    def run(self):
#        #FIXME
#
#class WhoIs:
#    def __init__(self, ip):
#        self.ip = ip
#
#    def run():
#        #FIXME
#
#class NMap:
#    def __init__(self, ip):
#        self.ip = ip
#
#    def run():
#        #FIXME

class Investigation:
    def __init__(self, ip):
        self.ip = ip
        self.modules = []
        self.modules.append(Traceroute(ip))
        self.modules.append(GeoIP(ip))
#        self.tor = Tor(ip)
#        self.whois = WhoIs(ip)
#        self.nmap = NMap(ip)

    def dumpVersions(self):
        print("Modules :")
        for module in self.modules:
            print(" - " + module.getName() + " version " + module.getVersion())

    def run(self):
        for module in self.modules:
            module.run()

    def print(self):
        for module in self.modules:
            module.print()

    def to_json(self):
        return "not implemented"

