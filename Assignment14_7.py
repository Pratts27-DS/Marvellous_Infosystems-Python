# Write a lambda function which accepts one number and returns True if divisible by 5.

No = int(input("Enter a number : "))
Ret = lambda No : True if No % 5 == 0 else False

print(Ret(No))