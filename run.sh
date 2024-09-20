#!/bin/bash
#SBATCH -M snowy
module load python/3.11.4
module load conda/latest
module load intel-oneapi
module load init_opencl/2023.1.0"
python opencl_test.py 