import matplotlib.pyplot as plt
import csv
import os
import sys
from plotting import Plotter

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: 'python plot_only.py  source_directory'")
    exit()
#We already have the results in a file, we only have to plot them
folder = sys.argv[1]
out = folder.split("/")[-2]

for file in os.listdir(folder):
    if file.endswith(".csv"):
        results = os.path.join(folder, file)
        outputname = folder+sys.argv[2]+".png"
        Plotter(results, outputname)
