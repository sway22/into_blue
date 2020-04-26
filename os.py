#os.walk(path) --> lists out directories and subdirs
import os

pwd = os.getcwd()
list_directory = os.walk(pwd)
for directory in list_directory:
    print (directory)
