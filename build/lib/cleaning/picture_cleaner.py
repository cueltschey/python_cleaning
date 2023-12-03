import glob
import shutil
import os


def pictureClean():
    root = os.getcwd() + "/"
    files = [(f, f.split(".")[-1]) for f in glob.glob(root + "*")]

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

    
