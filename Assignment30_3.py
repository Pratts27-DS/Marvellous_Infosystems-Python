# Display File Line by Line
# Problem statement:
## Write a program which accepts a file name from the user and 
# display the contents of the file line by line on the screen.

def main():
    filename = input("Enter the name of file: ")

    try:
        file = open(filename,"r")

        for line in file:
            print(line, end="")

        file.close()

    except FileNotFoundError:
        print("There is no such file")

if __name__ == "__main__":
    main()