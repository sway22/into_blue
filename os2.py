#os.walk(path) --> lists out directories and subdirs
#os.listdir(path) --> lists out directories
import os

for root,dirs,files in os.walk(".",topdown=False):
    for name in files:
            print("OS path " + name + " Root " + root + os.path.join(root,name))
    for name in dirs:
            print("these are the dirs " + name)
