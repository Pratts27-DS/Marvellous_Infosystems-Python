# Design a Python application that creates two threads named Thread1 ad Thread2.
# Thread1 should display numbers from 1 to 50.
# Thrread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
#### Thread2 start execution only after Thread1 has completed.
# Use appropriate thread syncronization.

import threading

def Display():
    print("Thread1 execution started")
    for i in range(1, 51):
        print(i)
    print("Thread2 execution completed\n")

def Show():
    print("Thread2 execution started")
    for i in range(50,0,-1):
        print(i)
    print("Thread2 execution completed")

def main():
    t1 = threading.Thread(target=Display)
    t2 = threading.Thread(target=Show)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of Process")

if __name__ == "__main__":
    main()