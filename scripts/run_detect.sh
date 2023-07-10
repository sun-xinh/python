#!/bin/bash

### for run py

#SBATCH -J slurm_python
#SBATCH --partition=express
#SBATCH -o %A_%a.output
#SBATCH -e %A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:02:00
#SBATCH --mem=2G

python3 scripts/detect_encoding.py 1/1.TXT
