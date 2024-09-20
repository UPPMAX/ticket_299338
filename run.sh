#!/bin/bash
#SBATCH -M snowy

# Don't! Gives error:
#
# Lmod has detected the following error:  Cannot load module "conda/latest" because these module(s) are loaded:
#    python
#
# module load python/3.11.4

module load conda/latest
module load python/3.11.4
module load intel-oneapi
module load init_opencl/2023.1.0"
python opencl_test.py 