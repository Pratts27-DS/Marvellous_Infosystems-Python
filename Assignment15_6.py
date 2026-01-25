# Write a lambda function using recuce() which accepts a list of numbers and returns the minimum number.

from functools import reduce

Data = [10,20,30,40,50]

Min = lambda A,B : A if A < B else B

RData = reduce(Min,Data)

print(RData)