# Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
#### Extract all even elements from the list.
#### Calculate and display their sum.
# The OddList thread should:
#### Extract all odd elements from the list.
#### Calculate and display their sum.
# Threads should run concurrently.


import threading

def EvenList(Data):
    Sum = 0
    for No in Data:
        if No % 2 == 0:
            print(No)
            Sum = Sum + No

    print("SUm of even numbers : ",Sum)

def OddList(Data):
    Odd = 0
    for No in Data:
        if No % 2 != 0:
            print(No)
            Odd = Odd + No
    
    print("Sum of odd numbers : ",Odd)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the elements {i+1} : "))
        Data.append(No)

    t1 = threading.Thread(target=EvenList, args=(Data,),)
    t2 = threading.Thread(target=OddList, args=(Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()