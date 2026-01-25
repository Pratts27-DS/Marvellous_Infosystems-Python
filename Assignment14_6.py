# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

No = int(input("Enter a number : "))
Ret = lambda No : True if No % 2 == 1 else False

print(Ret(No))