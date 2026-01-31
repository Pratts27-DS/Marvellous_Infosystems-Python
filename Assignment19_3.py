# Write a program which contains filter(), map() and reduce in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted  from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce

def main():

    size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(size):
        No = int(input(f"Enter the element {i+1} : "))
        Data.append(No)

    print(Data)

    FData = list(filter(lambda A: A >= 70 and A <= 90, Data))
    print("Data after filter : ",FData)

    MData = list(map(lambda A: A + 10, FData))
    print("Data after map : ",MData)

    RData = reduce(lambda A,B: A * B, MData)
    print("Data after reduce : ",RData)

if __name__ == "__main__":
    main()