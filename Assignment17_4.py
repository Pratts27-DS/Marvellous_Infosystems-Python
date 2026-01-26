# Write a program which accept one number from user and return addition of its factors.

def Display(No):
    Ans = 0
    for i in range(1,No+1):
        if No % i == 0:
            Ans = Ans + i
    return Ans

Ret = int(input("Enter a number : "))

Result = Display(Ret)
print(Result)