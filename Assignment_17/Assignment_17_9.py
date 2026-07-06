'''
write a program which accept number from user and return number of digits in that number.
Input : 5187934
Output : 7

'''
def DisplayDigits(No):
    Digit = 0
    Count = 0

    while(No > 0):
        Digit = No % 10

        Count += 1

        No = No // 10
    
    return Count

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = DisplayDigits(Value)

    print(Ret)

if __name__ == "__main__":
    main()