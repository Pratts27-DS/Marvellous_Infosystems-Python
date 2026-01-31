# Design a Python application that creates three threads named Small, Capital and Digits.
## All threads should accept a string as input.
## The Small thread should count and display the number od lowercase characters.
## The Capital thread should count and display the number of uppercase characters.
## The Digits thread should cound and display the number of numeric digits.
## Each thread must also display:
#### Thread ID
#### Thread Name

import threading

def Small(str):
    cnt = 0
    for i in str:
        if i.islower():
            cnt = cnt + 1

    t = threading.current_thread()
    print("--Small Thread--")
    print("Count of lowercase characters: ",cnt)
    print("Thread ID: ",t.ident)
    print("Thread Name: ",t.name)
    print("------------------------")

def Capital(str):
    cnt = 0
    for i in str:
        if i.isupper():
            cnt = cnt + 1

    t = threading.current_thread()
    print("--Capital Thread--")
    print("Count of uppercase characters: ",cnt)
    print("Thread ID: ",t.ident)
    print("Thread Name: ",t.name)
    print("------------------------")

def Digits(str):
    cnt = 0
    for i in str:
        if i.isdigit():
            cnt = cnt + 1

    t = threading.current_thread()
    print("--Digits Thread--")
    print("Count of digits: ",cnt)
    print("Thread ID: ",t.ident)
    print("Thread Name: ",t.name)
    print("------------------------")

def main():
    text = input("Enter a name: ")

    t1 = threading.Thread(target=Small, args=(text,),)
    t2 = threading.Thread(target=Capital, args=(text,),)
    t3 = threading.Thread(target=Digits, args=(text,),)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("End of Process")

if __name__ == "__main__":
    main()