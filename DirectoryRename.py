# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extension.
## Usage: DirectoryRename.py "Demo" ".txt" ".doc"
## Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
## After execution this script each .txt file gets renamed as .doc.

import sys
import os
import time

def DirectoryRename(DirName="Demo", OldExt=".txt", Newext=".doc"):
    Border = "-" * 50
    timestamp = time.ctime()

    LogFile = "DirectoryRename.log"
    fobj = open(LogFile,"w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Rename Script\n")
    fobj.write(Border + "\n")

    if not os.path.exists(DirName):
        fobj.write("Error: Directory does not esixts\n")
        fobj.close()
        return
    
    if not os.path.isdir(DirName):
        fobj.write("Error: Given path is not a directory\n")
        fobj.close()
        return
    
    RenameCount = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for fname in FileNames:
            if fname.endswith(OldExt):
                OldPath = os.path.join(FolderName, fname)
                NewName = fname.replace(OldExt, Newext)
                NewPath = os.path.join(FolderName, NewName)
                os.rename(OldPath, NewPath)
                RenameCount = RenameCount + 1
                fobj.write("Renamed : "+ fname + " -> " + NewName + "\n")

    fobj.write(Border + "\n")
    fobj.write("Total files renamed: "+ str(RenameCount) + "\n")
    fobj.write("Log file created at: "+ timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()


def main():
    if len(sys.argv) != 4:
        with open("DirectoryRename.log", "w") as fobj:
            fobj.write("Error: Invalid number of arguments\n")
            fobj.write("Usage: DirectoryRename.py Demo .txt .doc\n")
        return
    
    DirectoryRename(sys.argv[1], sys.argv[2],sys.argv[3])


if __name__ == "__main__":
    main()