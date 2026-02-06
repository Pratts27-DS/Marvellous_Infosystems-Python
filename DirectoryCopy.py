# Design automation script which accept two directory names. Copy all files from first directory into second directory.
# Second directory should be created at run time.
## Usage: DirectoryCopy.py "Demo" "Temp"
## Demo is the name of dirrectory which is existing and contains files in it.
## We have to create new Directory as Temp and copy all files from Demo to Temp.

import sys
import os
import shutil
import time


def DirectoryCopy(ExDir="Demo", NewDir="Temp"):
    Border = "-" * 50
    timestamp = time.ctime()

    LogFile = "DirectoryCopy.log"
    fobj = open(LogFile, "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Copy Script\n")
    fobj.write(Border + "\n")

    if not os.path.exists(ExDir):
        fobj.write("Error : Old directory does not exist\n")
        fobj.close()
        return

    if not os.path.isdir(ExDir):
        fobj.write("Error : Old path is not a directory\n")
        fobj.close()
        return

    if not os.path.exists(NewDir):
        os.mkdir(NewDir)
        fobj.write("New directory created : " + NewDir + "\n")

    CopyCount = 0

    for FolderName, SubFolder, FileNames in os.walk(ExDir):
        for fname in FileNames:
            ExDirPath = os.path.join(FolderName, fname)
            NewDirPath = os.path.join(NewDir, fname)

            shutil.copy2(ExDirPath, NewDirPath)
            CopyCount += 1
            fobj.write("Copied : " + fname + "\n")

    fobj.write(Border + "\n")
    fobj.write("Total files copied : " + str(CopyCount) + "\n")
    fobj.write("Log file created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()


def main():
    if len(sys.argv) != 3:
        with open("DirectoryCopy.log", "w") as fobj:
            fobj.write("Error : Invalid number of arguments\n")
            fobj.write("Usage : DirectoryCopy.py Demo Temp\n")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
