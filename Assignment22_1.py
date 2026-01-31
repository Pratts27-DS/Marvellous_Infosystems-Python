# Write a Python program to implement a class named Demo with the following specifications:
## The class should contains two instance varibles: no1 and no2
## The class should contains one class variable named Value
## Define a constructor (__init__) that accepts two parameters and initialize the instance variables
## Implement two instance methods:
#### Fun() - displays the values of instance variables no1 and no2
#### Gun() - displays the values of instance variables no1 and no2
# create two objects of the Demo class as follows:
## obj1 = Demo(11,21)
## obj2 = Demo(51,101)
# Call the instance methods in the given sequence:
## obj1.Fun()
## obj2.Gun()
## obj1.Gun()
## obj2.Fun()

class Demo:
    Value = 0

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Value of no1: ",self.no1)
        print("Value of no2: ",self.no2)

    def Gun(self):
        print("Value of no1: ",self.no1)
        print("Value of no2: ",self.no2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Gun()
    obj1.Gun()
    obj2.Fun()

if __name__ == "__main__":
    main()