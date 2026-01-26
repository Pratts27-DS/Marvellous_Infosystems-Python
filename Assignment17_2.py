# Write a program which accept one number and display below pattern.
# *   *   *   *   *   
# *   *   *   *   *   
# *   *   *   *   *   
# *   *   *   *   *   
# *   *   *   *   *   

def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end="    ")
        print()

Result = int(input("Enter a number : "))
Display(Result)