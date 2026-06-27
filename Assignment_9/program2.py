#write a program which contains one function named as ChkGreater() that accepts two numbers and prints greater number.

def ChkGreater(No1, No2):

    if(No1 > No2):
        return True
    else:
        return False

def main():
    Value1 = 0
    Value2 = 0
    Ret = False
 
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = ChkGreater(Value1, Value2)

    if(Ret == True):
        print(Value1,"is Greater")
    else:
        print(Value2, "is Greater")
    
if __name__ == "__main__":
    main()