# Write a lambda function which accepts three numbers and returns largest number.

No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
No3 = int(input("Enter third number : "))

Ret = lambda No1,No2,No3 : No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)

print(Ret(No1,No2,No3))