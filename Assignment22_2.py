# Write a Python program to implement a class named circle with the following requirements:
## The class should contains three instance variables: Radius, Area and Circumference
## The class should contains one class variable named PI, initialized o 3.14
## Define a constructor (__init__) that initializes all instance variables to 0.0
## Implement the following instance methods:
#### Accept() - accepts the radius of the circle from the user
#### CalculateArea() - calculates the area of the circle and stores it in the Area variable.
#### CalculateCircumference() - calculates the circumference of the circle and stores it in the Circumference variable
#### Display() - displays the values of Radius, Area and Circumference
## Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of circle : ",self.Radius)
        print("Area of circle : ",self.Area)
        print("CIrcumference of circle : ",self.Circumference)
        print("---------------------------------")

def main():
    Ret = int(input("Enter number of circles : "))

    for i in range(Ret):
        print(f"\nCircle {i+1}")
        
        obj = Circle()
        obj.Accept()
        obj.CalculateArea()
        obj.CalculateCircumference()
        obj.Display()

if __name__ == "__main__":
    main()