import os
import shutil

'''
Run the script in a certain directory and it will organise all the files according to the extension
Works with all file types
'''

def organise_files():
# --- Get the directory where the script is located --- #
  script_dir = os.path.dirname(os.path.realpath(__file__))

# --- Create a dictionary to map file types to directories --- #
  file_types = {}

# --- Walk through all files in the directory --- #
  for root, dirs, files in os.walk(script_dir):
    for file in files:
      
# --- get file extension
      file_ext = file.split('.')[-1]
      if file_ext not in file_types:
        
# --- Create a new directory for the file type --- #
        file_types[file_ext] = file_ext + '_files'
        os.makedirs(file_types[file_ext])
        
# --- Move the file to the appropriate directory --- #
      shutil.move(os.path.join(root, file), os.path.join(file_types[file_ext], file))

# --- Test the function --- #
organise_files()
