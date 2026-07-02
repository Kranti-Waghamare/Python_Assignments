#write a program which accepts one number and checks whether it is perfect number or not.
#Input : 6 
#Output : It is perfect number

def ChkPerfect(No):
    Count = 1
    Sum = 0

    if(No < 0):
        No = -No

    while(Count <= (No // 2)):
        if((No % Count) == 0):
            Sum = Sum + Count
        
        Count += 1

    if(Sum == No):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPerfect(Value)

    if(Ret == True):
        print("Its perfect number")
    else:
        print("Its not perfect number")

if __name__ == "__main__":
    main()