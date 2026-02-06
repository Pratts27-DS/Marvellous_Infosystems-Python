# Design automation script which accepts directory name and write names of duplicate files 
# from that directory into log file names as Log.txt. Log.txt file should be created into current directory.
## Usage: DirectoryDuplicate.py "Demo"

import os
import sys
import hashlib
import time


def CalculateChecksum(FileName):
    try:
        fobj = open(FileName, "rb")
        hobj = hashlib.md5()

        buffer = fobj.read(1024)
        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = fobj.read(1024)

        fobj.close()
        return hobj.hexdigest()

    except Exception:
        return None


def FindDuplicateFiles(DirName, logf):
    if not os.path.exists(DirName):
        logf.write("Error : Directory does not exist\n")
        return

    if not os.path.isdir(DirName):
        logf.write("Error : Given path is not a directory\n")
        return

    Duplicate = {}

    for foldername, subfolder, filenames in os.walk(DirName):
        for fname in filenames:
            filepath = os.path.join(foldername, fname)
            checksum = CalculateChecksum(filepath)

            if checksum is not None:
                if checksum in Duplicate:
                    Duplicate[checksum].append(filepath)
                else:
                    Duplicate[checksum] = [filepath]

    logf.write("Duplicate files are :\n")

    for value in Duplicate.values():
        if len(value) > 1:
            for file in value:
                logf.write(file + "\n")
            logf.write("\n")


def main():
    if len(sys.argv) != 2:
        print("ERROR : Invalid number of arguments")
        print("Usage : DirectoryDuplicate.py Demo")
        return

    try:
        logf = open("Log.txt", "w")

        logf.write("-" * 50 + "\n")
        logf.write("Directory Duplicate File Finder\n")
        logf.write("Log created at : " + time.ctime() + "\n")
        logf.write("-" * 50 + "\n")

        FindDuplicateFiles(sys.argv[1], logf)

        logf.write("-" * 50 + "\n")
        logf.close()

    except Exception:
        pass


if __name__ == "__main__":
    main()
