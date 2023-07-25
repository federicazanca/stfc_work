import os
import sys

if len(sys.argv) < 3:
    print("ERROR: not enough arguments.  Usage: 'python copy_opt_struct.py  sourcefile.log sourcefile.in'")
    exit()

filepath = sys.argv[1]
templatepath = sys.argv[2]
folder = os.path.dirname(filepath)
outputpath = folder = os.path.dirname(filepath)+"/"+templatepath.split(".")[-2].split("/")[-1]+"_continue.in"
print(outputpath)
folder = os.path.dirname(filepath)
outfile=open(outputpath, "w")

start_marker_1 = "End of BFGS Geometry Optimization"
start_marker = "CELL_PARAMETERS "
end_marker = "Writing config-only to output data dir "

copy_lines = True
with open(templatepath, "r") as templ:
    for line in templ:
        if start_marker in line:
            copy_lines = False
        if copy_lines:
            outfile.write(line)

outfile.close()
endofbfgs = False
with open(filepath, "r") as infile, open(outputpath, "a") as outfile:
    for line in infile:
        if start_marker_1 in line:
            endofbfgs = True
        if endofbfgs:
            if start_marker in line:
                copy_lines = True
            elif end_marker in line:
                copy_lines = False
            if copy_lines:
                outfile.write(line)

outfile.close()
