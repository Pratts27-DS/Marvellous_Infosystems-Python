# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

Data = ["Java", "Python", "Machine Learning", "AI", "C++", "Java Script"]

Ret = lambda A : len(A) > 5

FData = list(filter(Ret,Data))

print(FData)