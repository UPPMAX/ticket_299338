# ticket_299338

Notes for RT ticket 299338


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

