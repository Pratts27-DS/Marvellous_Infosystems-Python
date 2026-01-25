# Write a lambda function which accepts one number and returns True if number is even otherwise False.

No = int(input("Enter a number : "))
Ret = lambda No : True if No % 2 == 0 else False

print(Ret(No))