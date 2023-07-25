import matplotlib.pyplot as plt
import csv
import os
import sys
from plotting import Plotter

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: 'python convergence_analysis.py  source_directory'")
    exit()
#We already have the results in a file, we only have to plot them
folder = sys.argv[1]
out = folder.split("/")[-2]

results = open(folder+out+"_results.csv")
outputname = folder+sys.argv[2]+".png"

Plotter(results, outputname)
