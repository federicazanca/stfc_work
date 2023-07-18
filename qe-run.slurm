#!/usr/bin/env bash

#SBATCH -N 1
#SBATCH --exclusive

##SBATCH --ntasks-per-node=64
##SBATCH --ntasks-per-node=24
#SBATCH --ntasks-per-node=32

#SBATCH --cpus-per-task=1

##SBATCH -C scarf20b
#SBATCH -C scarf20|scarf21
##SBATCH -C scarf18

##SBATCH --mem=950G
##SBATCH  --account=scddevel
##SBATCH --reservation=scddevel

#SBATCH -t 12:00:00

echo "starting"
date +'%m/%d/%Y'
date +%c


module purge

module load amd-modules
#module load skylake-modules

module load QuantumESPRESSO/7.1-foss-2022a

srun pw.x  -in cubht-opt.in > cubht-opt.log

echo "finished"
date +'%m/%d/%Y'
date +%c
