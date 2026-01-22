# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater(No1,No2):
    if (No1 > No2):
        print(No1,"is greater")
    else:
        print(No2,"is greater")

def main():

    ChkGreater(10,20)

if __name__ == "__main__":
    main()