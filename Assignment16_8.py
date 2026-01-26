# Write a program which accept number from user and print that number of "*" on screen.

def Display(No):
    for i in range(No):
        print("*",end=" ")
    
Ans = int(input("Enter a number : "))
Display(Ans)