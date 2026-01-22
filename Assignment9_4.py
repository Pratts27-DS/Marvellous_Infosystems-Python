# Write a program which accepts one number and prints cube of that number.

def Cube(No):
    Ans = No **3
    return Ans

Result = int(input("Enter a number : "))
print("Cube is ",Cube(Result))