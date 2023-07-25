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
outputname = sys.argv[2]
results = open(folder+"/"+outputname+"geom_conv.csv", "w")
results.write("Step,Energy"+"\n")
Lines = log_file.readlines()
step = 0
xy_list = []
for line in Lines:
    if "!    total energy              =" in line:
        y = line.split()[-2]
        step += 1
        xy_list.append([step,y])
        results.write(str(step)+","+str(y)+"\n")
conv_threshold = 0.000001
for j in range(len(xy_list)-1):
    if float(xy_list[j][1]) - float(xy_list[j+1][1]) <= conv_threshold:
        print("converged")

results.close()
results = folder+"/"+outputname+"geom_conv.csv"


Plotter(results, outputname)

