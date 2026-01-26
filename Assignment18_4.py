# Write a program which accept N numbers from user and store it into list.
# Accept one another number from user and return frequency of that numbers from list.

def main():
    Size = int(input("Enter the number of elements : "))
    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    element = int(input("Element to search : "))

    count = 0
    for i in range(Size):
        if Data[i] == element:
            count = count + 1

    print(count)

if __name__ == "__main__":
    main()