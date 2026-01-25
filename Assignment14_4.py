# Write a lambda function which accepts two numbers and returns minimum number.

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Ret = lambda No1,No2 : No1 if No1 < No2 else No2

print(Ret(No1,No2) ,"is minimum")