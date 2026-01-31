# Write a program which contains one lambda function which accepts two parameters and return its multiplication.

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ret = lambda No1 , No2 : No1 * No2

print(Ret(No1,No2))