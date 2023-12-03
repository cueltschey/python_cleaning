import glob
import shutil
import os
import sys


def bundle():
    root = os.getcwd()

    files = [f for f in glob.glob(root + "/*")]

    args = sys.argv

    if(len(args) < 2):
        print("Usage: $bundler <bundle name>")
        return False

    os.mkdir(root + "/" + args[1]) 

    for file in files:
        if("." in file and file.split(".")[1] not in ["ini","dll"]):
            new = root + f"/{args[1]}/" + file.split("/")[-1]
            print(file)
            print(new)
            shutil.move(file, new)
    return True

if(bundle()):
    print("bundling successful")
