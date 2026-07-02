#write a program which accepts one two numbers and prints addition, substaction, multiplication, division.

def PerformOperation(No1, No2):
    Ans = No1 + No2

    print(Ans)

    Ans = No1 - No2

    print(Ans)

    Ans = No1 * No2

    print(Ans)

    Ans = No1 // No2

    print(Ans)

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    PerformOperation(Value1, Value2)

if __name__ == "__main__":
    main()