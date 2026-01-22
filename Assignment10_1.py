# Write a program which accepts one number and prints multiplication table of that number.

def Multiplication_Table(No):
    for i in range(1,11):
        print(No * i, end=" ")

Ans = int(input("Enter a number : "))
Multiplication_Table(Ans)