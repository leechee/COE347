#!/bin/bash
#SBATCH -J mach-5-coarse
#SBATCH -o /work2/10189/jasonlee/frontera/COE347/openfoam3/final_project/mach-5-coarse/job.o%j
#SBATCH -e /work2/10189/jasonlee/frontera/COE347/openfoam3/final_project/mach-5-coarse/job.e%j
#SBATCH -p normal
#SBATCH -N 1
#SBATCH -n 4
#SBATCH -t 02:00:00
#SBATCH -A CTS24005

module load openfoam/7.0
cd /work2/10189/jasonlee/frontera/COE347/openfoam3/final_project/mach-5-coarse
./AllrunParallel
