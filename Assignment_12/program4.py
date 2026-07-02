#write a program which accepts one number and prints that many numbers starting from 1.
#Input : 5
#Output : 1 2 3 4 5

def PrintNumbers(No):
    Count = 1

    while(Count <= No):
        print(Count)

        Count += 1

def main():
    print("Enter the number : ")
    Value = int(input())

    PrintNumbers(Value)

if __name__ == "__main__":
    main()