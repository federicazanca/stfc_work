import os
import sys
import matplotlib.pyplot as plt
import csv
from plot import Plotter


if len(sys.argv) < 3:
    print("ERROR: not enough arguments.  Usage: 'python plot_geom_conv.py  source_file output_figure_file_name'")
    exit()

#Get the output data from the log file and create the results file. Specifically for the geometry optimisation convergence
filepath = sys.argv[1]
folder = filepath.split("/")[-2]
log_file = open(filepath, "r")
results = open(folder+"geom_opt_conv.csv", "w")
results.write("Step,Energy")
Lines = log_file.readlines()
step = 0
for line in Lines:
    if "!    total energy              =" in line:
        y = line.split()[-2]
        step += 1
        #xy_list.append([str(x),str(y)])
        results.write(str(step)+","+str(y))

results.close()
results = open(folder+"geom_opt_conv.csv", "w")
outputname = sys.argv[2]

Plotter(results, outputname)

