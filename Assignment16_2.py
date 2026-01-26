# Write a program which contains one function names as ChkNum() which accept one parameter as number. If number is even then it should display "Even Number" otherwise display "Odd number" on console.

def ChkNum(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

No = int(input("Enter a number : "))
ChkNum(No)