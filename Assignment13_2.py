# Write a program which accepts radius of circle and prints area of circle.

from math import pi

def Area(r):
    return pi * r **2

def main():
    radius = float(input("Enter radius of circle : "))
    print("Area of Circle : ",Area(radius))

if __name__ == "__main__":
    main()