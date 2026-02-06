# Design automation script which accept directory name and file extension from user. Display all files with that extension.
## Usage: DirectoryFileSearch.py "Demo" ".txt"
### Demo is name of directory and .txt is the extension that we want to search.

import sys
import os
import time


def DirectoryFileSearch(DirName="Marvellous", Extension=".txt"):
    Border = "-" * 50
    timestamp = time.ctime()

    LogFile = "DirectoryFileSearch.log"
    fobj = open(LogFile, "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory File Search Script\n")
    fobj.write(Border + "\n")

    if not os.path.exists(DirName):
        fobj.write("ERROR : Directory does not exist\n")
        fobj.close()
        return

    if not os.path.isdir(DirName):
        fobj.write("ERROR : Given path is not a directory\n")
        fobj.close()
        return

    FileCount = 0
    MatchCount = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for fname in FileNames:
            FileCount += 1
            if fname.endswith(Extension):
                MatchCount += 1
                fobj.write("File Found : " + fname + "\n")

    fobj.write(Border + "\n")
    fobj.write("Total files scanned : " + str(FileCount) + "\n")
    fobj.write("Total matching files : " + str(MatchCount) + "\n")
    fobj.write("Log file created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()


def main():
    if len(sys.argv) != 3:
        with open("DirectoryFileSearch.log", "w") as fobj:
            fobj.write("ERROR : Invalid number of arguments\n")
            fobj.write("Usage : DirectoryFileSearch.py DirectoryName Extension\n")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
