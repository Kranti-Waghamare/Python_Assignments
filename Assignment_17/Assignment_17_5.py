'''
write a program which accept one number from user and check wheter number is prime or not.
Input : 5
Output : It is prime

'''

def ChkPrime(No):
    for i in range(2, No):
        if((No % i) == 0):
            return False
        
    return True

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is prime")
    else:
        print("It is not prime")

if __name__ == "__main__":
    main()