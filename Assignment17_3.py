# Write a program which accept one number from user and return its factorial.

def Fact(No):
    Ans = 1
    for i in range(1,No+1):
        Ans = Ans * i
    return Ans

Ret = int(input("Enter a number : "))

Result = Fact(Ret)
print(Result)