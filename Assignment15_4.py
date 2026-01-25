# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

Data = [1,3,4,6,8]

Add = lambda A,B : A + B

RData = reduce(Add,Data)

print(RData)