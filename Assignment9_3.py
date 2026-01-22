# Write a program which accepts one number and prints square of that number.

def Square(No):
    Ans = No * No
    return Ans

Result = int(input("Enter a number : "))
print("Square is ",Square(Result))