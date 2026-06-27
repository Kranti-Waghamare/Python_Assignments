#write a program which accepts one number form user and checks whether it is divisible by 3 and 5

def ChkDivisible(No):

    if(((No % 3) == 0) and ((No % 5) == 0)):
        return True
    else:
        return False
    
def main():
    value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = ChkDivisible(Value)
    
    if(Ret == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

if __name__ == "__main__":
    main()