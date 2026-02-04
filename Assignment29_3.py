# Copy File Contents into a New File(Command Line)
# Problem statement:
## Write a program which accepts an existing file name through command line arguments,
## and compares the contents of both files.
#### If both files contain the same contents display Success
#### Otherwise display Failure

import sys

def main():
    if len(sys.argv) != 3:
        return
    
    try:
        f1 = open(sys.argv[1], "r")
        data = f1.read()
        f1.close()

        f2 = open(sys.argv[2], "w")
        f2.write(data)
        f2.close()

        f1 = open(sys.argv[1], "r")
        f2 = open(sys.argv[2], "r")

        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")

        f1.close()
        f2.close()
        
    except FileNotFoundError:
        print("Files not found")

if __name__ == "__main__":
    main()