# Count Lines in a File
# Problem statement:
## Write a program which accepts a file name from the user 
# and counts how many lines are present in the file.

def main():
    filename = input("Enter the name of file: ")

    try:
        file = open(filename,"r")
        count = 0

        for line in file:
            count = count + 1

        file.close()
        print("Number of lines: ",count)

    except FileNotFoundError:
        print("There is no such file")

if __name__ == "__main__":
    main()