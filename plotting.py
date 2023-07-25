import csv
import matplotlib.pyplot as plt
import os

def Plotter(resultpath,outputname):
    """The function plots x, y data from a csv file that has a header and x,y data only
    resultpath = the path to the csv file"""
    results = open(resultpath)
    # Read data from the file 
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
    folderpath = os.path.dirname(resultpath)
    print(folderpath)
    plt.savefig(folderpath+"/"+outputname+".png")


    # Show the plot
    plt.show()