# Check File Exists in Current Directory
# Problem Statements:
## Write a program which accepts a file name from the user and 
# checks whether that file exists in the current directory or not.

import os

def main():
    Filename = input("Enter the name of file : ")

    Ret = os.path.exists(Filename)

    if (Ret == True):
        fobj = open(Filename, "r")
        print("File exist in the current directory")
    else:
        print("File not exist in the current directory")
        
if __name__ == "__main__":
    main()