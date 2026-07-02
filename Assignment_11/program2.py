#write a program which accepts one number from user and prints count of digits in that number.
#Input : 7521
# Output : 4


def CountDigit(No):
    Digit = 0
    Count = 0

    if(No < 0):
        No = -No

    while(No != 0):
       Digit = No % 10

       Count += 1

       No = No // 10

    return Count

    

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = CountDigit(Value)

    print(Ret)

if __name__ == "__main__":
    main()