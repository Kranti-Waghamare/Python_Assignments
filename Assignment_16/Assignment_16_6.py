#write a program which accept number from user and check whethter that number is positive or negative or zero.

def ChkNum(No):

    if(No > 0):
        print("Positive Number")

    elif(No < 0):
        print("Negative Number")

    else:
        print("Zero")

def main():

    print("Enter the number : ")
    Value = int(input())

    ChkNum(Value)

if __name__ == "__main__":
    main()