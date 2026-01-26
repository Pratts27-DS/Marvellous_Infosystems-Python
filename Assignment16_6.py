# Write a program which accept number from user and check whether that number is positive or negative or zero.

def Display(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

Ans = int(input("Enter a number : "))
Display(Ans)