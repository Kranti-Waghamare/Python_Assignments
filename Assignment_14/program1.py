#write a lambda function which accept one number and return square of that number.

Square = lambda No: No * No

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Square(Value)

    print(Ret)

if __name__ == "__main__":
    main()