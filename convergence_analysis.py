import os
import sys

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: python convergence_analysis.py  source_directory output_file")
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

folder = sys.argv[1]
out = folder.split("/")[-2]
results = open(out+"_results.csv", "w")
results.write(out+",energy\n")
x_list = []
y_list = []
for file in os.listdir(folder):
    if file.endswith("log"):
        print(file)
        x = file.split("_")[1].split(".")[0]
        print(x)
        x_list.append(x)
        open_file = open(folder+file, 'r')
        Lines = open_file.readlines()
        if converged(folder+file) == True:
            print(True)
            for line in Lines:
                if "!    total energy              =" in line:
                    y = line.split()[-2]
                    print(y)
                    y_list.append(y)
                    #results.write(','+y+"\n")
        else:
            print("not converged")
x_list.sort()
y_list.sort()
for i in range(len(x_list)):
    results.write(x_list[i]+","+y_list[i]+"\n")
results.close()
