# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Result = Add(No1,No2)

print(Result)