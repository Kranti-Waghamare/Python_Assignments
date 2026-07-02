#write a program which accept one number form use and check whether it is palindrome or not.
#Input : 121
#Output : Palindrom 

def ChkPalindrome(No):
    Digit = 0
    Count = 0
    Temp = No

    if(No < 0):
        No = -No

    while(No > 0):
        Digit = No % 10

        Count = (Count * 10) + Digit

        No = No // 10

    if(Count == Temp):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPalindrome(Value)

    if(Ret == True):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")
    

if __name__ == "__main__":
    main()