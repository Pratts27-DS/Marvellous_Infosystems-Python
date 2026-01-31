# Design a Python application that creates two threads.
## Thread1 should calculate and display the maximum element from an list.
## Thread2 should calculate and display the minimum element from an list.
## The list should be accepted from the user.

import threading

def Max(Data):
    print("----Thread1----")
    Max = Data[0]
    for No in Data:
        if No > Max:
            Max = No
    
    print("Maximun element is : ",Max)

def Min(Data):
    print("----Thread2----")
    Min = Data[0]
    for No in Data:
        if No < Min:
            Min = No

    print("Minimun element is : ",Min)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        No = int(input(f"Enter the element {i+1} : "))
        Data.append(No)

    t1 = threading.Thread(target=Max, args=(Data,),)
    t2 = threading.Thread(target=Min, args=(Data,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of application")

if __name__ == "__main__":
    main()