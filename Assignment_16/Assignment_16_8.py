#write a program which accept number from user and print that number of * on screen.
#Input : 5
#Output : * * * * * 

def Display(No):
    Count = 0

    while(Count < No):
        print("*", end = " ")

        Count += 1

def main():
    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()