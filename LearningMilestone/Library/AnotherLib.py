import os
print(os.getcwd())
print(os.listdir(".")) #List all the files

import shutil
shutil.copy('source.txt','destination.txt')
