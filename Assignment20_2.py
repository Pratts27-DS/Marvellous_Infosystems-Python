# Design a python application that creates two threads nambed EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
#### Identify all even factors of the given number.
#### Calculate and display the sum of even factors.
# The OddFactor thread should:
#### Identify all odd factors of the given number.
#### Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
# "Exit from main"

import threading

def EvenFactor(No):
    
    Sum = 0
    for i in range(1, No+1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i

    print("Sum of even factors : ",Sum)

def OddFactor(No):
    
    Odd = 0
    for i in range(1, No+1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            Odd = Odd + i
    
    print("Sum of odd factors : ",Odd)

def main():
    Num = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactor, args=(Num,),)
    t2 = threading.Thread(target=OddFactor, args=(Num,),)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()