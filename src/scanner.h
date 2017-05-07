#ifndef SCANNER_H
#define SCANNER_H

 

#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#include "token_types.h"
#include "tokens.h"

//added for making win32 DLL
#ifdef _WIN32
#    define SCANNER_DLLEXPORT __declspec(dllexport)
#elif __GNUC__ >= 4
#  define SCANNER_DLLEXPORT __attribute__ ((visibility("default")))
#else
#  define SCANNER_DLLEXPORT
#endif

typedef struct scanner {
    unsigned char *src, *cursor, *start, *end;
} scanner_t;

uint16_t scan_token(scanner_t *s);

SCANNER_DLLEXPORT scanner_t scanner_from_string(const char *input, size_t len);

SCANNER_DLLEXPORT void tokenize_add_tokens(token_array *tokens, const char *input, size_t len, bool keep_whitespace);
SCANNER_DLLEXPORT token_array *tokenize_keep_whitespace(const char *input);
SCANNER_DLLEXPORT token_array *tokenize(const char *input);


 

#endif
