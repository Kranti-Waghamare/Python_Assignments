#write a program which contains one function named as Add() which accept two numbers from user and return addition of that two numbers.
#Input : 11 5
#Output : 16

def Add(No1, No2):
    return No1 + No2

def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = Add(Value1, Value2)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()