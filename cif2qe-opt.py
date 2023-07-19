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
    'calculation':'vc-relax',         #Specify, type of calculation to perform
    'prefix': 'opt',                  #Default:	'pwscf' it's just for the name of the files
    'conv_thr'         : 1.0e-10,     #Default:	1.D-6, Convergence threshold for selfconsistency
    'diago_david_ndim' : 4,           #Default:	2, For Davidson diagonalization: dimension of workspace (number of wavefunction packets, at least 2 needed). A larger value may yield a smaller number of iterations in the algorithm but uses more memory and more CPU time in subspace diagonalization (cdiaghg/rdiaghg)
    'mixing_beta'  : 0.25,            #Default:	0.7D0, mixing factor for self-consistency            
    'startingwfc'      : 'atomic+random', #Default:	'atomic+random', chooses the starting wavefunction use 'file' to Start from an existing wavefunction file in the directory specified by variables prefix and outdir.
    'startingpot'      : 'atomic',    #similar to wavefunct but no random
    'ecutwfc'     : 50,               #kinetic energy cutoff (Ry) for wavefunctions               
    'ecutrho'     : 450,              #Default:	4 * ecutwfc, Kinetic energy cutoff (Ry) for charge density and potential
    'input_dft'   : 'VDW-DF2-B86R',   #Default:	read from pseudopotential files. Exchange-correlation functional: eg 'PBE', 'BLYP' etc.See Modules/funct.f90 for allowed values.
    'occupations':       'smearing',  
    'degauss':           0.001,       #Default:	0.D0 Ry
    'smearing'    : 'm-p',            #Default:	'gaussian'
    'tstress'   : False,              #Default:	.false. calculate stress. It is set to .TRUE. automatically if calculation == 'vc-md' or 'vc-relax'
    'tprnfor'      : True,            #calculate forces. It is set to .TRUE. automatically if calculation == 'relax','md','vc-md'
    'verbosity'    : "normal",        #Default:	'low'
    'outdir'       : './uio-opt',     
    'pseudo_dir'   : "/home/vol08/scarf1228/pseudos/",
    'disk_io'      : "none",          #Default is 'low' for the scf case, 'medium' otherwise. Defines what to store in memory
    'restart_mode' : 'from_scratch',  #Default:	'from_scratch'
    'nstep'        : 400,             #Default:	1 if calculation == 'scf', 'nscf', 'bands'; 50 for the other cases. number of molecular-dynamics or structural optimization steps
    'scf_must_converge' : False,      #Default:	.TRUE. If .false. do not stop molecular dynamics or ionic relaxation when electron_maxstep is reached. Use with care.
    'electron_maxstep':  200,         #Default:	100
    'etot_conv_thr':     1e-06,       #Default:	1.0D-4 Convergence threshold on total energy (a.u) for ionic  minimization:
    'forc_conv_thr':     1e-05,       #Default:	1.0D-3 Convergence threshold on forces (a.u) for ionic minimization
    'ion_dynamics':      'bfgs',      #Specify
    'cell_dynamics':     'bfgs',      #Default: bfgs
    'ibrav': 0,                       #Specify. Bravais-lattice index. 14=triclinic. If 0, must use CELL_PARAMETERS (it is a card to put later in the file) and specify the cell parameters
    'cell_dofree':       'ibrav'      #Default:	'all'. Select what parameters to move. ibrav moves all axis and angles but the lattice stays constant
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
         'I':'I.pbe-n-kjpaw_psl.0.2.UPF', 'Cu 63.546 Cu.pbe-dn-rrkjus_psl.1.0.0.UPF'}

a.wrap()
write(to,a,input_data=opts,pseudopotentials = pots, crystal_coordinates=False,  format="espresso-in")


