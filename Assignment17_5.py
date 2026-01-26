# Write a program which accept one number from user and check whether number is prime or not.

def Display(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

Ret = int(input("Enter a number : "))

if Display(Ret):
    print("It is Prime Number")
else:
    print("It is not a Prime Number")