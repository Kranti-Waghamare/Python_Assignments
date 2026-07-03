#write a lambda function which accepts one number and return true if number is even otherwise false

Even = lambda No : (No % 2 == 0)

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Even(Value)

    print(Ret)

if __name__ == "__main__":
    main()