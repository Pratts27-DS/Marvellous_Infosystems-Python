# Frequency of a String in File
# Problem statement:
## Write a program which accepts a file name and one string from the user,
## returns the frequency (count of occurences) of that string in the file.

def main():
    filename = input("Enter the name of file: ")
    string = input("Enter string to search on file: ")

    try:
        file = open(filename,"r")
        data = file.read()
        file.close()

        count = data.count(string)
        print("Frequency of string: ",count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()