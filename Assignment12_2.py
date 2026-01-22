# Write a program which accepts one number and prints its factors.

def Factors(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i,end=" ")

Result = int(input("Enter a number : "))
Factors(Result)