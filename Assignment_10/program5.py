#write a program which accepts one number and prints all odd numbers till that number.
#Input : 10
#Output : 1 3 5 7 9 

def printOdd(No):
    Count = 0

    while(Count <= No):
        if((Count % 2) != 0):
            print(Count)
        
        Count += 1

def main():
    print("Enter the number : ")
    Value = int(input())

    printOdd(Value)

if __name__ == "__main__":
    main()