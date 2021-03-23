# whois.py

from utils import *
import re

class WhoIs:
    def __init__(self, ip):
        self.ip = ip
        self.asNumbers = []
        self.emailAbuse = "(placeholder)"
        self.netname = "(placeholder)"
        self.country = "(placeholder)"
        self.description = "(placeholder)"
        self.netaddresses = []
        self.cache = ""

    # *** Utils ***
    def loadASNumbers(self):
        for line in self.cache:
            if len(line) > 1 and line[0] == "origin" \
                            and len(line[1]) > 2 \
                            and line[1][0:2] == "AS":
                self.asNumbers.append(line[1])

    def loadEmailAbuse(self):
        for line in self.cache:
            if len(line) > 0 and line[0][0:7] == "% Abuse":
                decomp = line[0].split()
                for entry in decomp:
                    entry = entry.strip("'")
                    if re.match("^\S+@\w+\.\w+$", entry):
                        self.emailAbuse = entry

    def loadNetName(self):
        for line in self.cache:
            if len(line) > 1 and line[0] == "netname":
                self.netname = line[1]
                return

    def loadCountry(self):
        for line in self.cache:
            if len(line) > 1 and line[0] == "country":
                self.country = line[1]
                return

    def loadDescription(self):
        for line in self.cache:
            if len(line) > 1 and line[0] == "descr":
                self.description = line[1]
                return

    def loadNetAddresses(self):
        for line in self.cache:
            if len(line) > 1 and line[0] == "address":
                self.netaddresses.append(line[1])
    # *** End Utils ***

    def getName(self):
        return "whois"

    def getVersion(self):
        commande = ['whois', '--version']
        (_, cmd_stdout, _, cmd_exit, _) = exec_cmd(commande)

        if cmd_exit != 0:
            return ""

        lines = cmd_stdout.split("\n")
        print(lines)
        words = lines[0].split()
        print(words)
        return words[1]

    def isInstalled(self):
        commande = ['traceroute', '--version']
        (_, _, _, cmd_exit, _) = exec_cmd(commande)
        return cmd_exit == 0

    def run(self):
        commande = ["whois", self.ip]
        (_, cmd_stdout, _, cmd_exit, _) = exec_cmd(commande)

        if cmd_exit != 0:
            return

        self.cache = cmd_stdout.split("\n")
        for i in range(0, len(self.cache)):
            self.cache[i] = self.cache[i].split(':')
            for e in range(0, len(self.cache[i])):
                self.cache[i][e] = self.cache[i][e].strip()

        self.loadASNumbers()
        self.loadEmailAbuse()
        self.loadNetName()
        self.loadCountry()
        self.loadDescription()
        self.loadNetAddresses()

    def print(self):
        for line in self.cache:
            print(line)

        print()
        print("*** WhoIs ***")
        print("AS numbers:")
        for entry in self.asNumbers:
            print(" - " + entry)
        print("E-mail abuse contact: " + self.emailAbuse)
        print("Network name: " + self.netname)
        print("Country: " + self.country)
        print("Description: " + self.description)
        print("Network addresses :")
        for entry in self.netaddresses:
            print(" - " + entry)

