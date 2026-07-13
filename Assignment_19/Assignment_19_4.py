'''
write a program which contains filter(), map() and reduce() in it. python application which contains one list of numbers. List contains the numbers
which are accepted from user. filter should filter out all such number which are Even. 
map function will calculate its square . Reduce will return addition of all that numbers.

Input : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter : [2, 4, 4, 2, 8, 10]
List after map : [4, 16, 16, 4, 64, 100]
output after reduce : 204
'''
from functools import reduce

Even = lambda No : No % 2 == 0

Square = lambda No : No * No

Addition = lambda No1, No2 : No1 + No2

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is : ",Data)

    FData = list(filter(Even, Data))

    print("Data after filter : ", FData)

    MData = list(map(Square, FData))

    print("Data after map : ", MData)

    RData = reduce(Addition, MData)

    print("Product of all numbers are : ",RData)


if __name__ == "__main__":
    main()