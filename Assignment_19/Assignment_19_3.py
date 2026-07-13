'''
write a program which contains filter(), map() and reduce() in it. python application which contains one list of numbers. List contains the numbers
which are accepted from user. filter should filter out all such number which are greater than or equal to 70 and less than or equal to 90. 
map function will increase each number by 10. Reduce will return product of all that numbers.

Input : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter : [76, 89,86, 90, 70]
List after map : [86, 99, 96, 100, 80]
output after reduce : 6538752000
'''
from functools import reduce

Greater = lambda No : No >= 70 and No <= 90

Increment = lambda No : No + 10

Product = lambda No1, No2 : No1 * No2

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is : ",Data)

    FData = list(filter(Greater, Data))

    print("Data after filter : ", FData)

    MData = list(map(Increment, FData))

    print("Data after map : ", MData)

    RData = reduce(Product, MData)

    print("Product of all numbers are : ",RData)


if __name__ == "__main__":
    main()