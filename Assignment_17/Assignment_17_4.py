'''
write a program accept number from user and return addition of its factors.
Input : 12
Output : 16   ( 1 + 2 + 3 + 4 + 6)
'''

def AddFactors(No):
    Sum = 0
    Count = 1

    while(Count <= (No / 2)):
        if((No % Count) == 0):
            Sum = Sum + Count

        Count += 1
    
    return Sum

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = AddFactors(Value)

    print(Ret)

if __name__ == "__main__":
    main()