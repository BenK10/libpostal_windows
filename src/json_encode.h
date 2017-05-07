#ifndef JSON_ENCODE_H
#define JSON_ENCODE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "collections.h"
#include "string_utils.h"
#include "utf8proc/utf8proc.h"

//added for making win32 DLL
#ifdef _WIN32
#    define JSONENCODE_DLLEXPORT __declspec(dllexport)
#elif __GNUC__ >= 4
#  define JSONENCODE_DLLEXPORT __attribute__ ((visibility("default")))
#else
#  define JSONENCODE_DLLEXPORT
#endif

JSONENCODE_DLLEXPORT char *json_encode_string(char *str);

#endif