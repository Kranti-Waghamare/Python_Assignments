#write a program which accepts one number and prints all even numbers till that number.
#Input : 10
#Output : 2 4 6 8 10

def PrintEven(No):
    Count = 1

    while(Count <= No):
        if((Count % 2) == 0):
            print(Count)

        Count = Count + 1

def main():
    print("Enter the number : ")
    Value = int(input())

    PrintEven(Value)

if __name__ == "__main__":
    main()