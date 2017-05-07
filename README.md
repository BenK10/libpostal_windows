Libpostal for Windows
=========================
------------------------
Building libpostal
------------------------

Install MSYS.  
Use pacman to install autoconf, automake, and libtools: pacman -S yourpackage  
Run build_libpostal.sh from MinGW.    
You should now have libpostal-1.dll (henceforth assumed to be renamed to libpostal.dll), which will be 32 bit if 
you used MinGW32 and 64 bit if you used MinGW64.  
There is also libpostal.dll.a - don't confuse them! 

-------------------
Using libpostal
-------------------
If using MSVC:  
Build a .lib out of libpostal.dll. It needs to be the same bitness as the DLL:  
  -method 1: Digital Mars' implib tool  
  -method 2: MSVC lib tool.   
     &nbsp;&nbsp;&nbsp;Run the following commands from VC\bin directory  
     &nbsp;&nbsp;&nbsp;vcvars32.bat (or amd64\vcvars64.bat for 64 bit)  
     &nbsp;&nbsp;&nbsp;lib /def:libpostal.def /out:libpostal.lib  

In your driver program, include libpostal.h (surround with extern "C" if the driver is C++)  
Link the driver to libpostal.lib and put libpostal.dll in the .exe's directory.  
Note that if the driver is C++, MSVC may not run the debug build. Release config should work.  

If using libpostal in a multithreaded way, each thread needs to implement its own concurrency around its
libpostal API calls.

