# Write a program which accepts one number and prints that many numbers in reverse order.

def Display(No):
    for i in range(No,0,-1):
        print(i,end=" ")

Result = int(input("Enter a number : "))
Display(Result)
