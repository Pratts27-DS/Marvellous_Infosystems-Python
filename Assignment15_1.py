# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

Data = [1,2,3,4,5]

Square = lambda No : No * No

MData = list(map(Square,Data))

print(MData)