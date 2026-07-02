#write a program which accepts one number from user and prints reverse of that number.
#Input :  123
#Output : 321

def ReverseDigit(No):
    Digit = 0
    Reverse = 0

    while(No > 0):
        Digit = No % 10

        Reverse = (Reverse * 10) + Digit

        No = No // 10

    return Reverse
    

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = ReverseDigit(Value)

    print(Ret)

if __name__ == "__main__":
    main()