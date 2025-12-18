#Create a folder named my_output and print the full path to a file inside it
import os
folder="output-folder"
os.makedirs(folder,exist_ok=True) #exist_ok=True prevents error if folder already exists
print(f"the folder'{folder}' created")

#creating path with file
file="filedemo.txt"
full_path=os.path.join(folder,file)
print("path created succesfully")
print(full_path)
