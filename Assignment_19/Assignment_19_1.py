'''
write a program which contains one lambda function which accepts one parameter and return power of two.
Input : 4
Output : 14

'''

Square = lambda No : No * No

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Square(Value)

    print("Square of number is : ",Ret)

if __name__ == "__main__":
    main()