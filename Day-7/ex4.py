import os
import inspect

print("Current Working Directory:", os.getcwd())

# functions=inspect.getmembers(os, inspect.isbuiltin)
# print("All function in os module: ")
# for n, func in functions:
#     print(n, end=', ')

list_of_files=os.listdir()
print("\nList of files and directories in the current directory:")
for n in list_of_files:
    print(n, end=', ')

#Create a folder inside current directory
cdir=os.getcwd()
folder_name=input("\nEnter folder name to create: ")
folder_path=os.path.join(cdir, folder_name)
if(os.path.exists(folder_path)):
    print("Folder already exists!")
else:
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder {folder_name} created successfully at {folder_path}!")

#Rename a folder
#os.rename('old_folder_name', 'new_folder_name')
# write a code to rename a folder
#you will take foldername as input from user
# if it is exists, you will ask new name to rename
# if it is not exists, you will print "Folder does not exist!"
# old_folder_name=input("\nEnter folder name to rename: ")
# if(os.path.exists(old_folder_name)):
#     new_folder_name=input("Enter new folder name: ")
#     os.rename(old_folder_name, new_folder_name)
#     print(f"Folder renamed successfully from {old_folder_name} to {new_folder_name}!")
# else:
#     print("Folder does not exist!")