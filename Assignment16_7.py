# Write a program which contains one function that accept one number from user and returns true if divisible by 5 otherwise return false.

def Display(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
Ans = int(input("Enter a number : "))
Result = Display(Ans)

print(Result)