#write a program which accepts one number and checks whether it is prime or not.
#Input : 11
#Output : Prime Number

def ChkPrime(No):
    Count = 2

    while(Count <= No/2):
        if((No % Count) == 0):
            break

        Count += 1
    
    if(Count < No/2):
        return False
    else:
        return True

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = False

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()