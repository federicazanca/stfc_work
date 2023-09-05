import os
import sys
import shutil
import fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


def replace(file_path, pattern, subst):
    """
    Replace a specific pattern in a file with another one
    Keyword arguments = strings
    """
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: 'python run....py  source_directory' to only get the results, 'python convergence_analysis.py  source_directory outputfile' to get the plot saved with the name outputfile")
    exit()


folder = sys.argv[1]

for root, dirs, files in os.walk(folder):
        a=11
        for file in files:
            #find the scf files (they should be 2 in each folder) and get the needed info: scf folder and MOF name
            if file.endswith("scf.in"):
                mofname = file[:-7]
                outp = file[:-2]+"log"
                print(mofname)
                correct = True
                # Construct the full path to the file using os.path.join
                full_path = os.path.join(root, file)
                for line in open(full_path, "r"):
                    if "disk_io          = 'none'" in line:
                        correct = False
                        print(mofname+" didn't run the complete scf")
                        break
                if correct == False:
                    replace(full_path, "uio-scf", "uio-scf"+str(a)) 
                    replace(full_path,"none", "low")     
                
                    print(f"cd {root}; sbatch qe-run.slurm {file} {outp}")
                    os.system(f"cd {root}; sbatch qe-run.slurm {file} {outp}")
                a += 1 


                             
                             

 