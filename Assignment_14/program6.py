#write a lambda function which accepts one number and return true if number is odd otherwise false

Odd = lambda No : (No % 2 != 0)

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Odd(Value)

    print(Ret)

if __name__ == "__main__":
    main()