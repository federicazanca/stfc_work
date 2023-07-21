import os
import sys
import matplotlib.pyplot as plt
import csv

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
results.close()



#2nd part: plotting the results
results = open(folder+out+"_results.csv")
# Read data from the file (we actually already have the data from before, but this is to make it generic)
x_field = None
y_field = None


reader = csv.DictReader(results)
header = reader.fieldnames
x_field = header[0]
y_field = header[1]

x = []
y = []

for row in reader:
    x.append(row[x_field])
    y.append(float(row[y_field]))

# Plot the data
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel(x_field.capitalize())  # Use the first column name as the X-axis label
plt.ylabel(y_field.capitalize())  # Use the second column name as the Y-axis label
plt.title('Plot of {} vs {}'.format(y_field.capitalize(), x_field.capitalize()))
plt.grid(True)

# Save the plot as an image (PNG or JPEG)
plt.savefig(folder+out+"_.png")  


# Show the plot
plt.show()
