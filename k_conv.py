import os
import sys
import shutil

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: python k_conv.py  source_directory")
    exit()

elenco = open("bg", "w")

N = 16
for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if not any(file.endswith('_g.in'):
                print("no gamma input file found")
            else:
                for i in range(1, N):
                    shutil.copyfile(file,  )




