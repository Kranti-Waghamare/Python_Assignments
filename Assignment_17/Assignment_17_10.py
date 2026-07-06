'''
write a program which accept number from user and return addition of digits in that number.
Input : 5187934
Output : 37

'''
def AddDigits(No):
    Digit = 0
    Sum = 0

    while(No > 0):
        Digit = No % 10

        Sum = Sum + Digit

        No = No // 10
    
    return Sum

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = AddDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()