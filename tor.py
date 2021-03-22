# tor.py

from utils import *
import json

class Tor:
    def __init__(self, ip):
        self.ip = ip
        self.isTorExitNode = None
        self.cache = None

    # *** Utils ***
    def fetchTorSummary(self):
        commande = ["curl", "https://onionoo.torproject.org/summary"]
        (cmd_stdin, cmd_stdout, cmd_stderr, cmd_exit, timeout) = exec_cmd(commande)
        if cmd_exit != 0:
            return "(error fetch)"
        self.cache = json.loads(cmd_stdout)
    # *** End Utils ***

    def getName(self):
        return "tor (onionoo api)"

    def getVersion(self):
        if not self.cache:
            self.fetchTorSummary()

        if "version" in self.cache:
            return self.cache["version"]
        return "(error json)"

    def isInstalled(self):
        return True

    def run(self):
        if not self.cache:
            self.fetchTorSummary()

        if "relays" in self.cache:
            exitNodes = []
            for entry in self.cache["relays"]:
                exitNodes.append(entry["a"][0])
            if self.ip in exitNodes:
                self.isTorExitNode = True
            else:
                self.isTorExitNode = False

    def print(self):
        print("\n*** Tor ***")
        print("IP \"" + self.ip + "\" is ", end='')
        if not self.isTorExitNode:
            print("not ", end='')
        print("an exit Tor relay")

