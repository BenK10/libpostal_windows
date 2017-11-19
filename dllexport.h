#ifndef DLLEXPORT_H
#define DLLEXPORT_H

#ifdef _WIN32
#    define DLLEXPORT __declspec(dllexport)
#elif __GNUC__ >= 4
#  define DLLEXPORT __attribute__ ((visibility("default")))
#else
#  define DLLEXPORT
#endif

#endif