# Write a program which contains filter(), map() and reduce() in it. Python application contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will 
# multiply each number by 2. Reduce will return Maximum number from tha numbers.

from functools import reduce

def prime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def mult(No):
    return No * 2

def max(A,B):
    if A > B:
        return A
    return B

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the elements {i+1}: "))
        Data.append(No)

    print(Data)

    FData = list(filter(prime, Data))
    print("Data after filter : ",FData)

    MData = list(map(mult, FData))
    print("Data after map : ",MData)

    RData = reduce(max,MData)
    print("Data after reduce : ",RData)

if __name__ == "__main__":
    main()