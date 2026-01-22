# Write a program which accepts one number and checks whether it is palindrome or not.

def Display(No):
    Ans = 0
    Result = No
    while Result > 0:
        Ans = Ans * 10 + Result % 10
        Result = Result // 10

    if No == Ans:
        print("Palindrome")
    else:
        print("Not Palindrome")

Ret = int(input("Enter a number : "))
Display(Ret)