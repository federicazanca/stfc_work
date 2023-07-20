import os
import sys
import shutil
import fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

if len(sys.argv) < 2:
    print("ERROR: not enough arguments.  Usage: python k_conv.py  source_directory")
    exit()

def files_endingwith(folder,end):
    """ In a folder tells you how many file ending with a specific string there are
        keywords = strings
        Return int
    """
    this_many=0
    for file in os.listdir(folder):
        if file.endswith(end):
            this_many = this_many+1
    return this_many

def mofname(folder,end):
    """ From the target file ending with something specific, gets the MOF name
        Keywords = strings. end keyword must contain "_"
        Return string
    """
    for file in os.listdir(folder):
        if file.endswith(end):
            mof = str(file.split("_")[0])
    return mof

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

target_folder = sys.argv[1]

#N is the number of files that we want to create
N = 85
#we are inside a folder and check how many input files are there.
#we are going to run the k-point convergence so ideally we should only have one input file and it should end with _40.in (gamma point)
n_of_infiles = files_endingwith(target_folder,'.in')
n_of_40 = files_endingwith(target_folder,'_40.in')
print("There are " + str(n_of_infiles) + " input files in the folder")
print("There are " + str(n_of_40) + " input files with 40 ecutwfc in the folder")
#first case, there is 1 input file and is gamma
if n_of_infiles == 1 and n_of_40 == 1:
    print("1 input file and it is 40, calculation can start")
    mof = mofname(target_folder,"_40.in")
    for i in range(45, N, 5):
        ecut = str(i*9)
        newfile = target_folder+"/"+mof+"_"+str(i)+".in"
        shutil.copyfile(target_folder+"/"+mof+"_40.in", newfile)
        replace(newfile, "ecutwfc          = 40", "ecutwfc          = "+ str(i))
        replace(newfile, "ecutrho          = 360", "ecutrho          = "+ ecut)
    os.system(f"cd {target_folder}; sbatch *.slurm")
#second case: there are no input files
elif n_of_infiles == 0:
    print("no input files found")
#third case: there are already more input files
else:
    print("too many .in files")
