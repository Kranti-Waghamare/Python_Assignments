#write a program which accepts two number and returns Multiplication.

Mult = lambda No1, No2: No1 * No2

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = Mult(Value1, Value2)

    print(Ret)

if __name__ == "__main__":
    main()