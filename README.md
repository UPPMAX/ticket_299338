# ticket_299338

Notes for RT ticket 299338

## Progress

### Attempt 2

This is the error that needs fixing:

```
Loading init_opencl version 2023.1.0
/home/richel/.local/lib/python3.11/site-packages/pytools/persistent_dict.py:63: RecommendedHashNotFoundWarning: Unable to import recommended hash 'siphash24.siphash13', falling back to 'hashlib.sha256'. Run 'python3 -m pip install siphash24' to install the recommended hash.
  warn("Unable to import recommended hash 'siphash24.siphash13', "
[<pyopencl.Platform 'NVIDIA CUDA' at 0x2c69030>]
[<pyopencl.Device 'Quadro K2200' on 'NVIDIA CUDA' at 0x2cb7680>]
```


### Attempt 1

```
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

pip install pyopencl

module load intel-oneapi
module load init_opencl/2023.1.0
python opencl_test.py 
```

```
[richel@rackham3 ticket_299338]$ ./run.sh 
The variable CONDA_ENVS_PATH contains the location of your environments. Set it to your project's environments folder if you have one.
Otherwise, the default is ~/.conda/envs. Remember to export the variable with export CONDA_ENVS_PATH=/proj/...

You may run "source conda_init.sh" to initialise your shell to be able
to run "conda activate" and "conda deactivate" etc.
Just remember that this command adds stuff to your shell outside the scope of the module system.

REMEMBER TO USE 'conda clean -a' once in a while

Defaulting to user installation because normal site-packages is not writeable
Collecting pyopencl
  Obtaining dependency information for pyopencl from https://files.pythonhosted.org/packages/b2/fe/e91597055c9d38e654f60a359db88848be8c5ea845a5b5199d312248ee81/pyopencl-2024.2.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata
  Downloading pyopencl-2024.2.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.7 kB)
Requirement already satisfied: numpy in /sw/comp/python/3.11.4/rackham/lib/python3.11/site-packages (from pyopencl) (1.24.4)
Requirement already satisfied: platformdirs>=2.2.0 in /sw/comp/python/3.11.4/rackham/lib/python3.11/site-packages (from pyopencl) (3.10.0)
Collecting pytools>=2024.1.5 (from pyopencl)
  Obtaining dependency information for pytools>=2024.1.5 from https://files.pythonhosted.org/packages/70/19/87514026ff33ae67681e7e721872db8d34fd0fc25ec28906fb7b1e5c57d0/pytools-2024.1.14-py3-none-any.whl.metadata
  Downloading pytools-2024.1.14-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: typing-extensions>=4 in /sw/comp/python/3.11.4/rackham/lib/python3.11/site-packages (from pytools>=2024.1.5->pyopencl) (4.7.1)
Downloading pyopencl-2024.2.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (697 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 698.0/698.0 kB 15.7 MB/s eta 0:00:00
Downloading pytools-2024.1.14-py3-none-any.whl (89 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 89.9/89.9 kB 14.6 MB/s eta 0:00:00
Installing collected packages: pytools, pyopencl
Successfully installed pyopencl-2024.2.7 pytools-2024.1.14
WARNING: There was an error checking the latest version of pip.
Loading init_opencl version 2023.1.0
/home/richel/.local/lib/python3.11/site-packages/pytools/persistent_dict.py:63: RecommendedHashNotFoundWarning: Unable to import recommended hash 'siphash24.siphash13', falling back to 'hashlib.sha256'. Run 'python3 -m pip install siphash24' to install the recommended hash.
  warn("Unable to import recommended hash 'siphash24.siphash13', "
[<pyopencl.Platform 'NVIDIA CUDA' at 0x2c69030>]
[<pyopencl.Device 'Quadro K2200' on 'NVIDIA CUDA' at 0x2cb7680>]
```

And here is our error:

```
Loading init_opencl version 2023.1.0
/home/richel/.local/lib/python3.11/site-packages/pytools/persistent_dict.py:63: RecommendedHashNotFoundWarning: Unable to import recommended hash 'siphash24.siphash13', falling back to 'hashlib.sha256'. Run 'python3 -m pip install siphash24' to install the recommended hash.
  warn("Unable to import recommended hash 'siphash24.siphash13', "
[<pyopencl.Platform 'NVIDIA CUDA' at 0x2c69030>]
[<pyopencl.Device 'Quadro K2200' on 'NVIDIA CUDA' at 0x2cb7680>]
```

## Communication

In reverse order, i.e. most recent at the top

### 2024-09-20

From the user:

> Sure, here is some additional information / scripts. The particular script I was running is "CellModellerGUI.py", found at /domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/Scripts/CellModellerGUI.py. 
>
> In the resulting GUI I select "Load Model", then select /domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/Examples/Conjugation/test_growth_rate_class.py as the model file, whereupon the code tries to find which OpenCL platforms are available for use and crashes with the traceback in my first email.
>
> However, all this with the GUI is probably quite a bit of overkill. I created a minimal script called opencl_test.py, found at /domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/Scripts/opencl_test.py. This scripts imports pyopencl and runs the function to identify available opencl platforms. For instance, when I run opencl_test.py on my laptop, I get the following output:

```
$ python opencl_test.py 
[<pyopencl.Platform 'Intel(R) CPU Runtime for OpenCL(TM) Applications' at 0x5629e025ea10>]
[<pyopencl.Device 'Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz' on 'Intel(R) CPU Runtime for OpenCL(TM) Applications' at 0x5629e0216fe8>]
```

> I think that if this script works, then this particular problem will be solved.
> 
> I also attach the output of conda list in the environment in which I am working.

### 2024-09-19

Email 2, as a reply to the user:

> I think your suspicions may be right. I will take a look at this now and
tomorrow and report tomorrow/Friday before 16:00 with my
progress/success/problems.
>
>It would be even more helpful if I'd get all the scrips you've used, so that I
can exactly reproduce the problem and verify I got things to work. Sure,
simplifying those scripts is a great idea too: it should be a script that when
I get it to run, you consider your problem solved :-)

Email 1, from the user:

> I am trying to run some python code on Snowy that depends on OpenCL. I have loaded the intel-oneapi and init_opencl/2023.1.0 modules. If I try to run the "clinfo" command to get info about avaialble OpenCL platforms, I get "bash: clinfo: command not found". Consistent with this, when I try to identify OpenCL platforms from within a Python script, I get:

```
"Traceback (most recent call last):
File "/domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/CellModeller/GUI/PyGLCMViewer.py", line 212, in load
  self.loadModelFile(modfile)
File "/domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/CellModeller/GUI/PyGLCMViewer.py", line 215, in loadModelFile
  if self.getOpenCLPlatDev():
     ^^^^^^^^^^^^^^^^^^^^^^^
File "/domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/CellModeller/GUI/PyGLCMViewer.py", line 69, in getOpenCLPlatDev
  return self.getOpenCLPlatform() and self.getOpenCLDevice()
         ^^^^^^^^^^^^^^^^^^^^^^^^
File "/domus/h1/danjo773/code/Conj_plas_cellmodell/CellModeller-master/CellModeller/GUI/PyGLCMViewer.py", line 73, in getOpenCLPlatform
  platforms = cl.get_platforms()
              ^^^^^^^^^^^^^^^^^^
pyopencl._cl.LogicError: clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR
Aborted (core dumped)"
```

> Here is the complete list of loaded modules:

```
"[danjo773@s15 Scripts]$ module list

Currently Loaded Modules:
1) uppmax   2) conda/latest   3) intel-oneapi   4) init_opencl/2023.1.0"
```

> I assume I am missing a dependency or perhaps need to load an additional module. Any help is appreciated.

