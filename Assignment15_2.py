# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

Data = [1,2,3,4,5,6,7,8,9,10]

ChkEven = lambda No : No % 2 == 0

FData = list(filter(ChkEven,Data))

print(FData)
