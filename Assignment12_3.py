# Write a program which accepts two numbers and prints addition,subtraction,multipliaction and division.

def Display(No1,No2):
    print("Addition is : ",No1+No2)
    print("Subtraction is : ",No1-No2)
    print("Multiplication is : ",No1*No2)
    print("Division is : ",No1/No2)


def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))

    Display(A,B)


if __name__ == "__main__":
    main()