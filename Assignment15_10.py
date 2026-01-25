# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

Data = [1,2,3,4,5,6,7,8,9,10]

ChkOdd = lambda No : No % 2 == 1

FData = len(list(filter(ChkOdd,Data)))

print(FData)