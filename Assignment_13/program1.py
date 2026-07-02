#Write a program which accepts length and width of rectangle and prints area.

def PrintArea(Length, Width):
    Area = 0

    Area = Length * Width

    print(Area)

def main():
    print("Enter length of recatangle : ")
    Value1 = int(input())

    print("Enter width of rectangle : ")
    Value2 = int(input())

    PrintArea(Value1, Value2)

if __name__ == "__main__":
    main()