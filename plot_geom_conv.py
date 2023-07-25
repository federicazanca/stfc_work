import os
import sys
import matplotlib.pyplot as plt
import csv
from plotting import Plotter


if len(sys.argv) < 3:
    print("ERROR: not enough arguments.  Usage: 'python plot_geom_conv.py  source_file output_figure_file_name'")
    exit()

#Get the output data from the log file and create the results file. Specifically for the geometry optimisation convergence
filepath = sys.argv[1]
folder = os.path.dirname(filepath)
print(folder)
log_file = open(filepath, "r")
results = open(folder+"/geom_opt_conv.csv", "w")
results.write("Step,Energy"+"\n")
Lines = log_file.readlines()
step = 0
for line in Lines:
    if "!    total energy              =" in line:
        y = line.split()[-2]
        step += 1
        #xy_list.append([str(x),str(y)])
        results.write(str(step)+","+str(y)+"\n")

results.close()
results = folder+"/geom_opt_conv.csv"
outputname = sys.argv[2]

Plotter(results, outputname)

