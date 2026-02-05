# Copy File Contents into Another File
# Problem statement:
## Write a program which accepts two file names from the user.
#### First file is an existing file
#### Second file is a new file
## Copy all contents from the first file into the second file.

def main():
    file1 = input("Enter the name first file: ")
    file2 = input("Enter the name of second file: ")

    try:
        f1 = open(file1,"r")
        Data = f1.read()
        f1.close()

        f2 = open(file2,"w")
        f2.write(Data)
        f2.close()

        print("File copied successfully")

    except FileNotFoundError:
        print("File not found")
        
if __name__ == "__main__":
    main()