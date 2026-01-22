# Write a program which accepts one number and prints reverse of that number.

def Display(No):
    Ans = 0
    for i in range(len(str(No))):
        Ans = Ans * 10 + No % 10
        No = No // 10
    
    print(Ans)

Result = int(input("Enter a number : "))
Display(Result)