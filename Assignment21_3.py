# Design a Python application where multiple threads update a shared variable.
## Use a Lock to avoid race condition.
## Each thread should increment the shared counter multiple time.
## Display the final value of the counter after all threads complete execution.

import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(1000):
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():
    Data = list()

    for i in range(5):  # create multiple threads
        t = threading.Thread(target=Increment, )
        Data.append(t)
        t.start()

    for j in Data:  # wait to finish all threads
        t.join()

    print("Final value of counter : ",counter)
    print("Exit from main")

if __name__ == "__main__":
    main()