#write a lambda function which accept one number and return cube of that number.

Cube = lambda No: No * No * No

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Cube(Value)

    print(Ret)

if __name__ == "__main__":
    main()