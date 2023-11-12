import glob
import shutil

root = "/mnt/c/Users/chase ueltschey/OneDrive/Pictures/Saved Pictures/"
allFiles = glob.glob(root + "*")

for file in allFiles:
    filename = file.split("/")[-1]
    ext = filename.split(".")[-1]
    if("." not in filename):
        continue
    if(ext.lower() == "jpg"):
        shutil.move(file, root + "jpg/" + filename)

    if(ext.lower() == "png"):
        shutil.move(file, root + "png/" + filename)

    if(ext.lower() == "mp4"):
        shutil.move(file, root + "mp4/" + filename)

    if(ext.lower() == "heic"):
        shutil.move(file, root + "heic/" + filename)

    
