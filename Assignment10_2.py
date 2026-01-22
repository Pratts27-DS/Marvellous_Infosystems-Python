# Write a program which accepts one number and prints sum of first N natural numbers.

def Natural_Number(No):
    Ans = 0
    for i in range(1,No+1):
        Ans = Ans + i

    print(Ans)

Result = int(input("Enter a number : "))
Natural_Number(Result)