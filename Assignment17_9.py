# Write a program which accept number from user and return number of digits in that number.

def Display(No):
    Ans = 0
    while No != 0:
        No = No // 10
        Ans = Ans + 1
    return Ans

Ret = int(input("Enter a number : "))

Result = Display(Ret)
print(Result)