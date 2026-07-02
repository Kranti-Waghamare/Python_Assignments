#write a program which accepts number from user and prints sum of N natural numbers.
#Input : 5
#Output : 15

def SumNatural(No):
    Ans = 0
    Count = 1

    while(Count <= No):
        Ans = Ans + Count
        
        Count = Count + 1

    print(Ans)

def main():
    print("Enter the number : ")
    Value = int(input())

    SumNatural(Value)

if __name__ == "__main__":
    main()