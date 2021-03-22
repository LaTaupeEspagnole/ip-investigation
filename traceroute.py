# traceroute.py

from utils import *

class Traceroute:
    def __init__(self, ip):
        self.ip = ip
        self.route = []

    # *** Utils ***
    def parseOutputLine(self, line):
        if len(line.split()) > 1 and line.split()[1] != "to":
            return line.split()[1]
        return None
    # *** End Utils ***

    def getName(self):
        return "traceroute"

    def getVersion(self):
        commande = ['traceroute', '--version']
        (_, _, cmd_stderr, cmd_exit, _) = exec_cmd(commande)

        if cmd_exit != 0:
            return ""

        lines = cmd_stderr.split("\n")
        words = lines[0].split()
        return words[5]

    def isInstalled(self):
        commande = ['traceroute', '--version']
        (_, _, _, cmd_exit, _) = exec_cmd(commande)
        return cmd_exit == 0

    def run(self):
        commande = ['traceroute', '-I', '-n', self.ip]
        (cmd_stdin, cmd_stdout, cmd_stderr, cmd_exit, timeout) = exec_cmd(commande)
        for line in cmd_stdout.split("\n"):
            res = self.parseOutputLine(line)
            if (res):
                self.route.append(res)

    def print(self):
        print("\n*** Traceroute ***")
        print("IP: " + self.ip)
        print("Route :")
        i = 1
        for step in self.route:
            print(str(i) + ". " + step)
            i += 1

