# adds DLLEXPORT macros to functions listed in file

import sys
import os
import shutil

def populate_export_dict(ref_file):
  d = {}
  l = []
  lines = open(ref_file).read().splitlines()
  for line in lines:
    if line[0]=='[' and line[len(line)-1]==']':
      current_filename = line[1:len(line)-1]
      l = []
      continue
    l.append(line)  
    d[current_filename] = l
  return d
    
    
def replace_lines(filename, replacements):
    lines = []
    with open(filename) as infile:
      for line in infile:
        for original, replacement in replacements.iteritems():
          line = line.replace(original, replacement)
          lines.append(line)
    with open(filename, "w") as outfile:
      for line in lines:
        outfile.write(line)
    
def backup_files(d, dir):
  if not os.path.exists("src_backups"):
    os.mkdir("src_backups")
  for key in d:
    if not os.path.isfile(os.path.join("src_backups", key + "_backup")):
      shutil.copy(os.path.join(dir, key), os.path.join("src_backups", key + "_backup"))

def add_dllexports(d, dir):
  for key in d:
    is_included = False
    output_src_lines = []
    with open(os.path.join(dir, key)) as infile:
    # close file here    
      for src_line in infile:
        if not is_included and src_line.find('#include')!=-1:
          src_line = '#include \"dllexport.h\"\n' + src_line
          is_included = True
        for ref_line in d[key]:
          if src_line.find(ref_line)!=-1:
            src_line = "DLLEXPORT " + src_line
            break
        output_src_lines.append(src_line)
     # write out file here
    with open(os.path.join(dir, key), "w") as outfile:
      for line in output_src_lines:
        outfile.write(line)

if __name__ == "__main__":
  if len(sys.argv)!=3:
    print("Usage: " + sys.argv[0] + " <input_file> <src_directory>")
    exit()
  d = populate_export_dict(sys.argv[1])
  backup_files(d, sys.argv[2])
  add_dllexports(d, sys.argv[2])
  
    
      
    
