# Write a program which accept one number and display below pattern
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def Display(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end="   ")
        print()

Ret = int(input("Enter a number : "))
Display(Ret)