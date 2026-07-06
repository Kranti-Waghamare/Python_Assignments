'''
write a program which accept one number from user and return its factorial.
Input : 5
Output : 120

'''

def Factorial(No):
    Count = 1

    for i in range(1, No+1):
        Count = Count * i

    return Count 

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print(Ret)

if __name__ == "__main__":
    main()