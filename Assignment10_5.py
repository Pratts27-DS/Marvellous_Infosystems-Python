# Write a program which accepts one number and prints all odd numbers till that number.

def Odd(No):
    for i in range(1,No+1,2):
        print(i, end=" ")

Result = int(input("Enter a number : "))
Odd(Result)