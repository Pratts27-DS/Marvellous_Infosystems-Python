# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

Data = [10,20,30,40,50]

Max = lambda A,B : A if A > B else B

RData = reduce(Max,Data)

print(RData)