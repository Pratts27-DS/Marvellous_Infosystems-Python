# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Data = [1,3,4,6,7]

Ret = lambda A,B : A * B

RData = reduce(Ret,Data)

print(RData)