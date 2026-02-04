# Compare Two FIles(Command Line)
# Problem Statement:
## Write a program which accepts two file names through command line arguments and 
## compares the contents of both files.
#### If both files contain the same contents, display Success
#### Otherwise display Failure

import sys

def main():
    if len(sys.argv) != 3:
        return
    
    try:
        f1 = open(sys.argv[1],"r")
        f2 = open(sys.argv[2],"r")

        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")

        f1.close()
        f2.close()
        
    except FileNotFoundError:
        print("Files not exist")

if __name__ == "__main__":
    main()