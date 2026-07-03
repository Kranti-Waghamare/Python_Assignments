#write a program which accepts one number and return true if number is divisible by 5

Divisible = lambda No : (No % 5 == 0)

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Divisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()