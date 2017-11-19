Libpostal for Windows
=========================

This project has some build script files from [libpostal](https://github.com/openvenues/libpostal) modified so that the project is buildable in Windows on MinGW/MSYS2 and produces a DLL. 
See the changelog for details about these changes.

It should be noted that there are better alternatives for using libpostal on Windows. Libpostal can be compiled and run without modification using a virtual machine or Docker container or the Windows Subsystem for Linux on Windows 10. This project is intended to be used when those options are not available.

This version of libpostal_windows differs from the original in that `declspec(dllexport)` statements are injected into the relevant places in the code as `DLLEXPORT` macros with a Python script. 
It therefore does not require any manual modification of the libpostal source.
The locations where `DLLEXPORT` macros are added is controlled through a file read by the Python script.

------------------------
Building libpostal
------------------------
These instructions assume a 64-bit machine. Your version of MSYS2, and gcc toolchain and parameters for MSVC's vcvarsall and lib will be different for 32-bit.

Install MSYS2.  
Use pacman to install autoconf, automake, make, libtools, mingw-w64-x86_64-gcc (the gcc toolchain), and Python: pacman -S yourpackage
Clone libpostal to your working directory or use curl from MinGW: `curl -sL https://github.com/openvenues/libpostal/tarball/master | tar xz`
Rename the downloaded folder to "libpostal" (curl's rename function doesn't seem to work from MinGW so you'll have to do this manually)
Run build_libpostal_windows.sh from MinGW. This script will copy some files and call a Python script that injects `declspec(dllexport` into the code in places defined in dllexports.txt.    
You should now have libpostal-1.dll (henceforth assumed to be renamed to libpostal.dll)  
There is also libpostal.dll.a - don't confuse them! 

-------------------
Using libpostal
-------------------
If using MSVC:  
Build a .lib out of libpostal.dll. It needs to be the same bitness as the DLL:  
  -method 1: Digital Mars' implib tool  
  -method 2: MSVC lib tool.   
     &nbsp;&nbsp;&nbsp;Run the following commands from VC\bin directory  
     &nbsp;&nbsp;&nbsp;`vcvarsall x64` (not sure if this step is necessary)
     &nbsp;&nbsp;&nbsp;`lib /def:libpostal.def /out:libpostal.lib /machine:x64` 

In your driver program, include libpostal.h (surround with extern "C" if the driver is C++)  
Link the driver to libpostal.lib and put libpostal.dll in the .exe's directory.  
Note that if the driver is C++, MSVC may not run the debug build. Release config should work.  
