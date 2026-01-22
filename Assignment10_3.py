# Write a program which accepts one number and prints factorial of that number.

def Factorial(No):
    Ans = 1
    for i in range(1,No+1):
        Ans = Ans * i

    print(Ans)

Result = int(input("Enter a number : "))
Factorial(Result)