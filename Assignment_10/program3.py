#write a program which acepts one number and prints factorial of that number.
#Input : 5
#Output : 120

def PrintFactorial(No):
    Ans = 1
    Count = 1

    if(No == 0):
        return -1
    
    if(No < 0):
        No = -No
    
    while(Count <= No):
        Ans = Ans * Count

        Count = Count + 1

    print(Ans)

def main():
    print("Enter the number : ")
    Value = int(input())

    PrintFactorial(Value)

if __name__ == "__main__":
    main()