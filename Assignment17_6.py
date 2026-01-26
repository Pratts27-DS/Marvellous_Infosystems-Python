# Write a program which accept one number and display below pattern.
# *   *   *   *   *
# *   *   *   *
# *   *   *
# *   *
# *

def Display(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end="   ")
        print()

Ret = int(input("Enter a number : "))
Display(Ret)