#write a program which accepts radius of circle and prints area of circle.

def PrintArea(Radius, PI = 3.14):
    Area = 0

    Area = PI * Radius * Radius

    print(Area)

def main():
    print("Enter the radius : ")
    Value = int(input())

    PrintArea(Value)

if __name__ == "__main__":
    main()