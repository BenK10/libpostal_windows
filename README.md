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

-------------------
Changelog
-------------------

added new source files: drand48.h, drand48.c, strdup.h, strdup.c to supply missing functions  
Added DLLEXPORT macro to several source files  
src/Makefile.am: -D UTF8PROC_EXPORTS added to CFLAGS so utf8proc builds  
&nbsp;&nbsp;&nbsp;added -no-undefined to libpostal_la_LDFLAGS  
&nbsp;&nbsp;&nbsp;added drand48.c to beginning of libscanner_la_SOURCES  
&nbsp;&nbsp;&nbsp;removed code building binaries. Some porting is needed for these.  
configure.ac: change LT_INIT([shared]) to LT_INIT([win32-dll])  
In build script, seems necessary to write, eg: C:\libpostal\libpostal_data as /c/libpostal//libpostal_data.   
Note double slash.  
Changed instances of fopen(somefile, "r") to binary mode "rb" to fix premature EOF when encountering 0x1a byte.  
Changed PATH_SEPARATOR for win32 to "/" from "\\". Windows accepts forward slashes so let's avoid escape sequence headaches.
