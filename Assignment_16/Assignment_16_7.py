#write a program which contains one fuction that accept one number from user and return true if number is divisible by 5 otherwise return false.

def ChkDivisible(No):
    if((No % 5) == 0):
        return True
    else:
        return False
    
def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = ChkDivisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()