# Search a Word in File
# Problem Statement:
## Write a program which accepts a file name and a word from the user 
# and checks whether that word is present in th file or not.

def main():
    filename = input("Enter the name of file: ")
    word = input("Enter a word to search in file: ")

    try:
        file = open(filename,"r")
        Ret = False

        for line in file:
            if word in line:
                Ret = True
                break

        file.close()

        if Ret:
            print("Word is present in the file")
        else:
            print("Word is not present in the file")

    except FileNotFoundError:
        print("There is no such file")

if __name__ == "__main__":
    main()