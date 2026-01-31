# Design a Python application that creates two threads named Prime and NonPrime.
## Both threads should accept a list of integers.
## The Prime thread should display all prime numbers from the list.
## The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def DisplayPrime(Data):
    print("Prime Numbers")
    for No in Data:
        if Prime(No):
            print(No)

def NonPrime(Data):
    print("NonPrime Numbers")
    for No in Data:
        if not Prime(No):
            print(No)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the elements {i+1} : "))
        Data.append(No)

    t1 = threading.Thread(target=DisplayPrime, args=(Data,),)
    t2 = threading.Thread(target=NonPrime, args=(Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()