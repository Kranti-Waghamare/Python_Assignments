#write a program which accepts one number from user and prints square of that number.

def SquareNumber(No):
    Ans = 0

    Ans = No * No

    return Ans

def main():
    value = 0
    Ret = 0

    print("Enter number :")
    Value = int(input())

    Ret = SquareNumber(Value)

    print("Square of the number is : ", Ret)

if __name__ == "__main__":
    main()
