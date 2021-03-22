# main.py

from investigation import *

inv = Investigation("89.234.183.191")
#inv = Investigation("46.163.76.170")
inv.dumpVersions()
inv.run()
inv.print()
