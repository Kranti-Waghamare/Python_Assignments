#write a program which accepts one number from user and prints square of that number.

def SquareNumber(No):
    print("square of that number is : ", No * No)

def main():
    value = 0

    print("Enter number :")
    Value = int(input())

    SquareNumber(Value)

if __name__ == "__main__":
    main()
