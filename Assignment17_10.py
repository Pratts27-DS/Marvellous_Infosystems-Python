# Write a program which accept number from user and return addition of digits in that number.

def Display(No):
    Ans = 0
    if No < 0:
        No = -No
    while No != 0:
        Ans = Ans + (No % 10)
        No = No // 10
    return Ans

Ret = int(input("Enter a number : "))
print(Display(Ret))