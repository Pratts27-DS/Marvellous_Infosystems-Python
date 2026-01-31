# Design a Python application that creates two threads
## Thread1 should compare the sum of elements from the list.
## Thread2 should compute the product of elements from the same list.
## Return the results to the main thread and display them.

import threading

Sum = 0
Product = 1

def DisplaySum(Data):
    global Sum
    total = 0
    for No in Data:
        total = total + No
    Sum = total

def DisplayProduct(Data):
    global Product
    Ret = 1
    for No in Data:
        Ret = Ret * No
    Product = Ret

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the element {i+1} : "))
        Data.append(No)

    t1 = threading.Thread(target=DisplaySum, args=(Data,),)
    t2 = threading.Thread(target=DisplayProduct, args=(Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements : ",Sum)
    print("Product of elements : ",Product)
    print("Exit from main")

if __name__ == "__main__":
    main()