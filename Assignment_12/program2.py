#write a program which accepts one number and prints its factors.
#Input : 12
#Output : 1 2 3 4 6 12

def PrintFactor(No):
    Count = 1

    if(No < 0):
        No = -No

    while(Count <= No):
        if((No % Count) == 0):
            print(Count)
            
    
        Count += 1

def main():
    print("Enter the number ")
    Value = int(input())

    PrintFactor(Value)

if __name__ == "__main__":
    main()