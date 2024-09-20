#!/bin/bash
#SBATCH -M snowy
#SBATCH -A staff

# Don't! Gives error:
#
# Lmod has detected the following error:  Cannot load module "conda/latest" because these module(s) are loaded:
#    python
#
# module load python/3.11.4

module load conda/latest
module load python/3.11.4

pip install pyopencl

# Fixes:
#
# /home/richel/.local/lib/python3.11/site-packages/pytools/persistent_dict.py:63: RecommendedHashNotFoundWarning: Unable to import recommended hash 'siphash24.siphash13', falling back to 'hashlib.sha256'. Run 'python3 -m pip install siphash24' to install the recommended hash.
#   warn("Unable to import recommended hash 'siphash24.siphash13', "
#
pip install siphash24

# Fixes PLATFORM_NOT_FOUND_KHR,
# from https://stackoverflow.com/a/77318195
#
pip install pocl-binary-distribution

module load intel-oneapi
module load init_opencl/2023.1.0
python opencl_test.py 