# Design automation script which accept directory name and display Checksum of all files.
## Usage: DirectoryChecksum.py "Demo"
## Demo is name of directory

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


def DirectoryChecksum(DirName, logf):
    if not os.path.exists(DirName):
        logf.write("Error : Directory does not exist\n")
        return

    if not os.path.isdir(DirName):
        logf.write("Error : Given path is not a directory\n")
        return

    for foldername, subfolder, filenames in os.walk(DirName):
        for fname in filenames:
            filepath = os.path.join(foldername, fname)
            checksum = CalculateChecksum(filepath)

            if checksum is not None:
                logf.write(filepath + " : " + checksum + "\n")


def main():
    if len(sys.argv) != 2:
        print("Error : Invalid number of arguments")
        print("Usage : DirectoryChecksum.py Demo")
        return

    timestamp = time.ctime()
    logname = "DirectoryChecksum_%s.log" % timestamp
    logname = logname.replace(" ", "_").replace(":", "_")

    try:
        logf = open(logname, "w")

        logf.write("-" * 50 + "\n")
        logf.write("Directory Checksum Automation Script\n")
        logf.write("Log created at : " + timestamp + "\n")
        logf.write("-" * 50 + "\n")

        DirectoryChecksum(sys.argv[1], logf)

        logf.write("-" * 50 + "\n")

        logf.close()  

    except Exception:
        pass


if __name__ == "__main__":
    main()
