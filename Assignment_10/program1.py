# write a program which accepts one number and prints multiplication table of that number.
#Input : 4
#Output : 4 8 12 16 20 24 28 32 36 40

def NumberTable(No):
    Count = 1
    Ans = 1 
    
    while(Count <= 10):
        Ans = No * Count
        print(Ans)
        
        Count = Count + 1

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = NumberTable(Value)

if __name__ == "__main__":
    main()