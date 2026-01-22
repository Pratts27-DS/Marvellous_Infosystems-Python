# Write a program which accepts one number and prints sum of digits.

def SumDigits(No):
    Ans = 0
    while No > 0:
        Ans = Ans + No % 10
        No = No // 10
    print(Ans)

Result = int(input("Enter a number : "))
SumDigits(Result)
