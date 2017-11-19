Libpostal for Windows
=========================

This project has some files from [libpostal](https://github.com/openvenues/libpostal) modified so that the project is buildable in Windows on MinGW/MSYS2. Use these files in place of the originals.
See the changelog for details about these changes.

------------------------
Building libpostal
------------------------
These instructions assume a 64-bit machine. Your version of MSYS2, and gcc toolchain and parameters for vcvarsall and lib will be different for 32-bit.

Install MSYS2.  
Use pacman to install autoconf, automake, make, libtools, and mingw-w64-x86_64-gcc (the gcc toolchain): pacman -S yourpackage  
Run build_libpostal.sh from MinGW.    
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
     &nbsp;&nbsp;&nbsp;vcvarsall x64 (n0t sure if this step is necessary)
     &nbsp;&nbsp;&nbsp;lib /def:libpostal.def /out:libpostal.lib /machine:x64 

In your driver program, include libpostal.h (surround with extern "C" if the driver is C++)  
Link the driver to libpostal.lib and put libpostal.dll in the .exe's directory.  
Note that if the driver is C++, MSVC may not run the debug build. Release config should work.  
