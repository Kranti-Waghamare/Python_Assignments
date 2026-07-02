#write a program which accepts the one number from and prints sum of digits.
#Input : 123
#Output : 6

def SumDigits(No):
    Digit = 0
    Sum = 0

    if(No < 0):
        No = -No

    while(No > 0):
        Digit = No % 10

        Sum = Sum + Digit

        No = No // 10

    return Sum    

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = SumDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()