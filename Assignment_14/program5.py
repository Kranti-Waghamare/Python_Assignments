#write a program which accepts one number and return true if number is even otherwise false

Even = lambda No : (No % 2 == 0)

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Even(Value)

    if(Ret == True):
        print("It is even number ")
    else:
        print("It is odd number")

if __name__ == "__main__":
    main()