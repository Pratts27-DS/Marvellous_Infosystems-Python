# Write a program which accepts one mumber and checks whether it is divisible by 3 and 5.

def ChkDivisible(No):
    if No % 3 == 0 and No % 5 == 0:
        print("DIvisible by 3 And 5")
    else:
        print("Not divisible by 3 and 5")

Ans = int(input("Enter a number : "))
ChkDivisible(Ans)