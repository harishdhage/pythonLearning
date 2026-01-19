import os #Operating System library to interact with the operating system
print("Current working directory: ",os.getcwd()) #Get current working directory
print("Files in current directory: ",os.listdir(".")) #List all the files

import shutil #Shell Utilities library to perform high-level file operations
shutil.copy('source.txt','destination.txt') #Copy source.txt to destination.txt
