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
    print("ERROR: not enough arguments.  Usage: 'python crun....py  source_directory' to only get the results, 'python convergence_analysis.py  source_directory outputfile' to get the plot saved with the name outputfile")
    exit()


folder = sys.argv[1]
input_files = "/work4/scd/scarf1228/uio/"
#input_files = "/home/federica/"
for root, dirs, files in os.walk(folder):
        for file in files:
              #find the scf files (they should be 2 in each folder) and get the needed info: scf folder and MOF name
              if file.endswith("scf.in"):
                    mofname = file[:-7]
                    print(mofname)
                    ready = True
                    # Construct the full path to the file using os.path.join
                    full_path = os.path.join(root, file)
                    for line in open(full_path, "r"):
                         #scf folder
                         if "outdir" in line:
                            scf_dir = (line.split()[2]).split("/")[1]
                            print(scf_dir)
                         if "disk_io          = 'none'" in line:
                            ready = False
                            print(mofname+" didn't run the complete scf")
                            break
                    if ready == True:
                        #create folder for bader charges for each mof
                        print("making directory for "+mofname)
                        target = os.path.join(root, "bader", mofname)
                        print(target)
                        if os.path.isdir(target):
                            print("directory already exists")
                        else:
                            os.makedirs(target)
                            shutil.copyfile(input_files+"pp.in",  target+"/pp.in")
                            shutil.copyfile(input_files+"pp.slurm",  target+"/pp.slurm")
                            inp = target + "/pp.in"
                            slurm = target + "/pp.slurm"
                            #modify pp files for specific mof inside the bader folder
                            for parameter in open(inp):
                                if "outdir = '../uio-scf2'" in parameter:
                                    replace(inp, "'../uio-scf2'", "../../"+scf_dir)
                                if "fileout = 'uio-CH3_2_Pdc.cube'" in parameter:
                                    replace(inp, "uio-CH3_2_Pdc.cube", mofname+".cube")
                            for i in open(slurm):
                                if "uio-CH3_Pdc-charge.log" in i:
                                    replace(slurm, "uio-CH3_Pdc", mofname)
                                if "UiO-66Zr-Pd-8.cube" in i:
                                    replace(slurm, "UiO-66Zr-Pd-8.cube", mofname+".cube")
                            os.system(f"cd {target}; sbatch pp.slurm")

                             
                             


