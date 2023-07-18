import os
import sys
from bandgap import bandgap
if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: python findbg.py  source_directory")
    exit()

elenco = open("bg", "w")

for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
        if file == "OUTCAR":
            complete = False
