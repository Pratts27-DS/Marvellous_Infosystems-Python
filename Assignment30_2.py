# Count Words in a file
# Problem statement:
## Write a program which accepts a file name from user 
# and counts the total number of words in that file.

def main():
    filename = input("Enter the name of file: ")

    try:
        file = open(filename,"r")
        count = 0

        for line in file:
            words = line.split()
            count = count + len(words)

        file.close()
        print("Number of words: ",count)

    except FileNotFoundError:
        print("There is no such file")

if __name__ == "__main__":
    main()