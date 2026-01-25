# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

Data = [7,9,13,15,25,30,60]

Ret = lambda No : No % 3 == 0 and No % 5 == 0

FData = list(filter(Ret,Data))

print(FData)