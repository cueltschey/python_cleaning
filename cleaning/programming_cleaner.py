import glob
import shutil
import os


def programmingClean():
    folders = {"py":"python/","c":"C/","asm":"C/","v":"verilog/","db":"SQL/","cs":"C#/","kt":"Kotlin/","js":"javascript/","ts":"javascript/","cpp":"c++/","html":"html/"}

    root = os.getcwd() + "/" 
    files = [(f, f.split('.')[-1]) for f in glob.glob(root + "*")]
    for file in files:
        if(file[1] in folders.keys()):
            shutil.move(file[0], root + folders[file[1]] + file[0].split("/")[-1])
