#ifndef FEATURES_H
#define FEATURES_H

#include <stdlib.h>
#include <stdarg.h>
#include "collections.h"
#include "string_utils.h"

//added for making win32 DLL
#ifdef _WIN32
#    define FEATURE_DLLEXPORT __declspec(dllexport)
#elif __GNUC__ >= 4
#  define FEATURE_DLLEXPORT __attribute__ ((visibility("default")))
#else
#  define FEATURE_DLLEXPORT
#endif

#define FEATURE_SEPARATOR_CHAR "|"

// Add feature to array

FEATURE_DLLEXPORT void feature_array_add(cstring_array *features, size_t count, ...);

// Add feature using printf format
void feature_array_add_printf(cstring_array *features, char *format, ...);

// Add feature count to dictionary

bool feature_counts_add(khash_t(str_double) *features, char *feature, double count); 
bool feature_counts_add_no_copy(khash_t(str_double) *features, char *feature, double count);
bool feature_counts_update(khash_t(str_double) *features, char *feature, double count); 
bool feature_counts_update_no_copy(khash_t(str_double) *features, char *feature, double count); 

VECTOR_INIT(feature_count_array, khash_t(str_double) *)

#endif