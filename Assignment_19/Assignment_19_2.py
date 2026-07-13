'''
write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input : 4 3
Output : 12

'''

Mult = lambda No1, No2 : No1 * No2

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Mult(Value1, Value2)

    print("Multiplication is : ", Ret)

if __name__ == "__main__":
    main()