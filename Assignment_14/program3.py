#write a program which accepts one number and return maximum number.

Max = lambda No1 , No2: No1 if No1 > No2 else No2

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = Max(Value1, Value2)

    print("maximum number is : ", Ret)


if __name__ == "__main__":
    main()