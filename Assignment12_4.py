# Write a program which accepts one number and prints that many numbers starting from 1.

def Display(No):
    for i in range(1,No+1):
        print(i,end=" ")

Result = int(input("Enter a number : "))
Display(Result)
