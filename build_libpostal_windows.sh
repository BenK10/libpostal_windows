#!/usr/bin/env bash
cp drand48.c drand48.h libpostal/src/klib
cp strndup.c strndup.h dllexport.h src_make/Makefile.am libpostal/src
cp Makefile.am libpostal
python add_dllexport.py dllexports.txt libpostal/src
cd libpostal
./bootstrap.sh
mkdir -p /c/libpostal//libpostal_data
./configure --datadir=/c/libpostal//libpostal_data
make
make install
#ldconfig