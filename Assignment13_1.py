# Write a program which accepts length and width of rectangle and prints area.

def Area(l,w):
    return l * w

def main():
    length = float(input("Enter length of reactangle : "))
    width = float(input("Enter width of rectangle : "))

    print("Area of rectangle : ",Area(length,width))

if __name__ == "__main__":
    main()