# adds DLLEXPORT macros to functions listed in file


# function that gets lines from dllexports_signatures list

# for each file names on that list, make a copy in the main libpostal_windows directory with "backup" appended to the name

# function that goes through the source line by line and checks whether a line in the list is a substring of it.
# if it is, prepend DLLEXPORT to that line
# write out file


# if MAIN, get arg, which is a .txt file with signatures to use. Abort if number of args is not 1


# ======= pseudocode =========
#process ref file line by line

#dict{} lines (key: file name value: list of lines)
#for each line
#  if line begins with '[' and ends with ']'
#  enter the content in between them as dictionary key
#  and all subsequent lines into that key's list
  
#for each key (=filename) in dictionary 
#  copy the file to main directory with suffix "original"
  
#for each key (=filename) in dictionary
#  for each src_line in src_file
#    for each ref_line in list
#     if ref_line is a substring of src_line
#       prepend DLLEXPORT to src_line
#       break       
#    add src_line to output buffer
#write out modified src file    

# =============================
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
  
    
      
    