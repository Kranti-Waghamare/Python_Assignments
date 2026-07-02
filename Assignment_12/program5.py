#write a program which accept one number and prints that many numbers in reverse order.
#Input : 5
#Output : 5 4 3 2 1

def PrintReverse(No):
    Count = 1
    
    while(Count <= No):
        print(No)

        No -= 1

def main():
    print("Enter the number : ")
    Value = int(input())

    PrintReverse(Value)

if __name__ == "__main__":
    main()