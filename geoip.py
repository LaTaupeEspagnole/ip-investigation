# geoip.py

from utils import *

class GeoIP:
    def __init__(self, ip):
        self.ip = ip
        self.country = "placeholder"
        self.countryCode = "placeholder"

    def getName(self):
        return "geoip"

    def getVersion(self):
        return "(no version)"

    def isInstalled(self):
        commande = ['geoiplookup', '-h']
        (_, _, _, cmd_exit, _) = exec_cmd(commande)
        return cmd_exit == 0

    def run(self):
        commande = ['geoiplookup', self.ip]
        (_, cmd_stdout, _, cmd_exit, _) = exec_cmd(commande)

        if cmd_exit != 0:
            return

        self.country = cmd_stdout.split()[4]
        self.countryCode = cmd_stdout.split()[3]

    def print(self):
        print("*** GeoIP ***")
        print("IP: " + self.ip)
        print("Country: " + self.country)
        print("Country code: " + self.countryCode)
