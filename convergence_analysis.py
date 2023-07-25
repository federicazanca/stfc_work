import os
import sys


if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: 'python convergence_analysis.py  source_directory' to only get the results, 'python convergence_analysis.py  source_directory outputfile' to get the plot saved with the name outputfile")
    exit()

def converged(file):
    open_file = open(file, 'r')
    Lines = open_file.readlines()
    converge = False
    for line in Lines:
        if "convergence has been achieved" in line:
            converge = True
            break
    return converge

def custom_sort(item):
    if item[0] == 'g':
        return (0, item[1])  # Sorting by 'g' first, then by the second element (number)
    else:
        return (1, item[0])  # Sorting all other elements by their first element (number)

#1st part: getting the results

folder = sys.argv[1]
out = folder.split("/")[-2]
results = open(folder+out+"_results.csv", "w")
results.write(out+",energy\n")
xy_list =[]
for file in os.listdir(folder):
    if file.endswith("log"):
        print(file)
        x = file.split("_")[1].split(".")[0]
        print(x)
        open_file = open(folder+file, 'r')
        Lines = open_file.readlines()
        if converged(folder+file) == True:
            print(True)
            for line in Lines:
                if "!    total energy              =" in line:
                    y = line.split()[-2]
                    print(y)
                    xy_list.append([str(x),str(y)])
                    #results.write(','+y+"\n")
        else:
            print("not converged")
xy_list = sorted(xy_list, key=custom_sort)
for i in range(len(xy_list)):
    results.write(xy_list[i][0]+","+xy_list[i][1]+"\n")

conv_threshold = 0.01
for j in range(len(xy_list)):
    if float(xy_list[j][1]) - float(xy_list[j+1][1]) <= conv_threshold:
        print("use" + str(xy_list[j]))
        break

results.close()


if len(sys.argv) == 3:
    import matplotlib.pyplot as plt
    import csv
    from plotting import Plotter
    #2nd part: plotting the results
    results = folder+out+"_results.csv"
    outputname = sys.argv[2]

    Plotter(results, outputname)
    
