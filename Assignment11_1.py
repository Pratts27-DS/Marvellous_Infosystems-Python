#Write a program which accepts one number and checks whether it is prime or not.

def ChkPrime(No):
    Ans = 0
    for i in range(1,No+1):
        if No % i == 0:
            Ans = Ans + 1

    if Ans == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

Result = int(input("Enter a number : "))
ChkPrime(Result)