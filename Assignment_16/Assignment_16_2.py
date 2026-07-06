#write a program which contains one function named as ChkNum() which accept one parameter as number. 
#if number is even should display Even number otherwise display odd number on console.
#input : 11
#Output : Odd Number

def ChkNum(No):
    if((No % 2) == 0):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()