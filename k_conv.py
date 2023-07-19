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

#N is the number of files that we want to create
N = 2
#we are inside a folder and check how many input files are there.
#we are going to run the k-point convergence so ideally we should only have one input file and it should end with _g.in (gamma point)
n_of_infiles = files_endingwith(sys.argv[1],'.in')
n_of_gamma = files_endingwith(sys.argv[1],'_g.in')
print("There are " + str(n_of_infiles) + " input files in the folder")
print("There are " + str(n_of_gamma) + " input files with gamma only in the folder")
#first case, there is 1 input file and is gamma
if n_of_infiles == 1 and n_of_gamma == 1:
    print("1 input file and it is gamma, calculation can start")
    mof = mofname(sys.argv[1],"_g.in")
    for i in range(1, N+1):
        newfile = sys.argv[1]+"/"+mof+"_"+str(i)+".in"
        shutil.copyfile(sys.argv[1]+"/"+mof+"_g.in", newfile)
        replace(newfile, "K_POINTS gamma", "K_POINTS automatic \n"+ str(i) + " " + str(i) + " " + str(i) + " 0 0 0")
#second case: there are no input files
elif n_of_infiles == 0:
    print("no input files found")
#third case: there are already more input files
else:
    print("too many .in files")




