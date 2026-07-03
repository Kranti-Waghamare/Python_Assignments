#write a program which accepts one number and print binary equivalent.

def PrintBinary(No):

    Binary = 0
    Place = 1

    if(No < 0):
        No = -No

    while(No > 0):

        Digit = No % 2

        Binary = Binary + (Digit * Place)

        Place = Place * 10

        No = No // 2

    print(Binary)

def main():

    print("Enter the number : ")
    Value = int(input())

    PrintBinary(Value)

if __name__ == "__main__":
    main()