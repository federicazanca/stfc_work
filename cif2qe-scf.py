#!/usr/bin/env python3

import argparse
from ase.io import read,write

cli=argparse.ArgumentParser()

cli.add_argument(
  "--cif",
  type=str,
  default='',
)

cli.add_argument(
  "--to",
  type=str,
  default='',
  )

args = cli.parse_args()

cif = args.cif
to = args.to
a=read(cif)


opts = {
    'calculation':'scf',              #Default:	'scf'
    'prefix': '_scf',                 #Default:	'pwscf' it's just for the name of the files
    'conv_thr'         : 1.0e-10,     #Default:	1.D-6, Convergence threshold for selfconsistency
    'diago_david_ndim' : 4,           #Default:	2, For Davidson diagonalization: dimension of workspace (number of wavefunction packets, at least 2 needed). A larger value may yield a smaller number of iterations in the algorithm but uses more memory and more CPU time in subspace diagonalization (cdiaghg/rdiaghg)
    'mixing_beta'  : 0.25,            #Default:	0.7D0, mixing factor for self-consistency            
    'startingwfc'      : 'atomic+random', #Default:	'atomic+random', chooses the starting wavefunction use 'file' to Start from an existing wavefunction file in the directory specified by variables prefix and outdir.
    'startingpot'      : 'atomic',    #similar to wavefunct but no random
    'ecutwfc'     : 50,               #kinetic energy cutoff (Ry) for wavefunctions               
    'ecutrho'     : 450,              #Default:	4 * ecutwfc, Kinetic energy cutoff (Ry) for charge density and potential
    'input_dft'   : 'VDW-DF2-B86R',   #Default:	read from pseudopotential files. Exchange-correlation functional: eg 'PBE', 'BLYP' etc.See Modules/funct.f90 for allowed values.
    'occupations':       'smearing',  #tetrahedra for dos? check. for band structure smearing
    'degauss':           0.001,       #Default:	0.D0 Ry
    'smearing'    : 'm-p',            #Default:	'gaussian'
    'tstress'   : False,              #Default:	.false. calculate stress. It is set to .TRUE. automatically if calculation == 'vc-md' or 'vc-relax'
    'tprnfor'      : True,            #calculate forces. It is set to .TRUE. automatically if calculation == 'relax','md','vc-md'
    'verbosity'    : "normal",        #Default:	'low'
    'outdir'       : './uio-scf',     #to define correctly
    'pseudo_dir'   : "/home/vol08/scarf1228/pseudos/",   #to define correctly
    'disk_io'      : "none",          #Default is 'low' for the scf case, 'medium' otherwise. Defines what to store in memory
    'restart_mode' : 'from_scratch',  #Default:	'from_scratch'
    'scf_must_converge' : True,       #Default:	.TRUE. If .false. do not stop molecular dynamics or ionic relaxation when electron_maxstep is reached. Use with care.
    'electron_maxstep':  200,         #Default:	100
        }

pots = { 'C':'C.pbe-n-rrkjus_psl.1.0.0.UPF',
         'O':'O.pbe-n-rrkjus_psl.1.0.0.UPF',
         'Zr':'Zr.pbe-spn-rrkjus_psl.1.0.0.UPF',
         'H': 'H.pbe-rrkjus_psl.1.0.0.UPF',
          'Cl': 'Cl.pbe-nl-rrkjus_psl.1.0.0.UPF',
          'Br': 'Br.pbe-n-rrkjus_psl.1.0.0.UPF',
         'N':'N.pbe-n-rrkjus_psl.1.0.0.UPF',
         'Pd':'Pd.pbe-spn-rrkjus_psl.1.0.0.UPF',
         'S':'S.pbe-n-rrkjus_psl.1.0.0.UPF',
         'I':'I.pbe-n-kjpaw_psl.0.2.UPF', 
         'Cu': 'Cu 63.546 Cu.pbe-dn-rrkjus_psl.1.0.0.UPF'}

a.wrap()
write(to,a,input_data=opts,pseudopotentials = pots, crystal_coordinates=False,  format="espresso-in")
