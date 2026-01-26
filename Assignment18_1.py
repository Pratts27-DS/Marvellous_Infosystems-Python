# Write a program which accept N numbers from user and store it into list. 
# Return addition of all elements from that List.

def main():
    Size = int(input("Enter the number of elements : "))
    Data = list()
    Value = 0

    print("Enter the elements : ")
    for i in range(Size):
        Ans = int(input())
        Data.append(Ans)
        Value = Value + Ans

    print(Value)

if __name__ == "__main__":
    main()