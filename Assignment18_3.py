# Write a program which accept N numbers from user and store it into list.
# Return Minimum number from that list.

def main():
    Size = int(input("Enter the number of elements : "))
    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    min = Data[0]
    for i in range(1,Size):
        if Data[i] < min:
            min = Data[i]

    print(min)

if __name__ == "__main__":
    main()
