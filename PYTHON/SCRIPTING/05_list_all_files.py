#list all files in a folder
import os
current_dir=os.path.abspath(".")
x=os.listdir(current_dir)
for item in x:
    full_path=os.path.join(current_dir,item)
    if os.path.isfile(full_path):
        print(item," is file")
    elif os.path.isdir(full_path):
        print(item," is a directory")
    else:
        print("item is not a directory and a file")
