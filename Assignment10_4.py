# Write a program which accepts one number and prints all even numbers till that number.

def Even(No):
    for i in range(2,No+1,2):
        print(i, end=" ")

Result = int(input("Enter a number : "))
Even(Result)