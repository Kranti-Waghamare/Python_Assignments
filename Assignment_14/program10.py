#write a lambda fumction which accepts three numbers and returns largest number.


Largest = lambda No1, No2, No3: No1 if (No1 > No2 and No1 > No3) else (No2 if (No2 > No1 and No2 > No3) else No3)

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    print("Enter the third number : ")
    Value3 = int(input())

    Ret = Largest(Value1, Value2, Value3)

    print(Ret)

if __name__ == "__main__":
    main()