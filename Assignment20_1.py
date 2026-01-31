# Design a python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def Even():
    print("Even Numbers")
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

def Odd():
    print("Odd Numbers")
    for i in range(1,21):
        if i % 2 != 0:
            print(i)

def main():
    t1 = threading.Thread(target=Even,)
    t2 = threading.Thread(target=Odd,)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of Execution")

if __name__ == "__main__":
    main()