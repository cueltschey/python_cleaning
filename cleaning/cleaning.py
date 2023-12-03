import glob
import shutil
import os
import sys


def bundle():
    root = os.getcwd() + "/"
    files = [f for f in glob.glob(root + "*")]
    args = sys.argv

    if(len(args) < 2):
        print("Usage: $bundler <bundle name>")
        return False

    os.mkdir(root + "/" + args[1]) 

    for file in files:
        if("." in file and file.split(".")[1] not in ["ini","dll"]):
            new = root + f"{args[1]}/" + file.split("/")[-1]
            print(file)
            print(new)
            shutil.move(file, new)
    return True

def pictureClean():
    root = os.getcwd() + "/"
    files = [(f, f.split(".")[1]) for f in glob.glob(root + "*")]

    for file in files:
        filename = file[0].split("/")[-1]
        ext = file[1].lower()
        if(ext == ""):
            continue
        if(ext == "jpg"):
            shutil.move(file, root + "jpg/" + filename)

        if(ext == "png"):
            shutil.move(file, root + "png/" + filename)

        if(ext == "mp4"):
            shutil.move(file, root + "mp4/" + filename)

        if(ext == "heic"):
            shutil.move(file, root + "heic/" + filename)

def programmingClean():
    folders = {"py":"python/","c":"C/","asm":"C/","v":"verilog/","db":"SQL/","cs":"C#/","kt":"Kotlin/","js":"javascript/","ts":"javascript/","cpp":"c++/","html":"html/"}

    root = os.getcwd() + "/" 
    files = [(f, f.split('.')[-1]) for f in glob.glob(root + "*")]
    for file in files:
        if(file[1] in folders.keys()):
            if(not os.path.exists(root + folders[file[1]])):
                os.mkdir(root + folders[file[1]])
            shutil.move(file[0], root + folders[file[1]] + file[0].split("/")[-1])
