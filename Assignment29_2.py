# Display File Contents
# Problem Statement:
## Write a program which accepts a file name from the user, 
# opens that file, and display the entire contents on the console.

def main():
    Filename = input("Enter the name of file : ")

    try:
        fobj = open(Filename,"r")
        print("File gets successfully opened")

        Data = fobj.read()

        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()