'''
write a program which accepts N numbers from user and store it into list. 
and return addition of all prime numbers from that list. Main python files 
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 8
Output : 54 (13 + 5 + 7 + 2 + 5)

'''
from MarvellousNum import * 

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = ListPrime(Data)

    print("Summation is : ",Ret)

if __name__ == "__main__":
    main()