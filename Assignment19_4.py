# Write a program which contains filter(), map() and reduce in it. Python application which contains
# one list of numbers. List contains the numbers which are accepted from user. FIlter should filter out
# all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the element {i+1}: "))
        Data.append(No)

    print(Data)

    FData = list(filter(lambda A: A % 2 == 0, Data))
    print("Data after filter : ",FData)

    MData = list(map(lambda A: A * A, FData))
    print("Data after map : ",MData)

    RData = reduce(lambda A,B: A + B, MData)
    print("Data after reduce : ",RData)

if __name__ == "__main__":
    main()