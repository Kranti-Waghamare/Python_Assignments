#write a program which accept one number from user and prints cube of that number.

def CubeNumber(No):
    Ans = 0

    Ans = No * No * No

    return Ans

def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = CubeNumber(Value)

    print("Cube of the number is : ", Ret)

if __name__ == "__main__":
    main()
