#write a lambda fumction using reduce() which accepts of list of numbers and return Minimum elements.

from functools import reduce

Min = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    RData = reduce(Min, Data)

    print("Data after map : ", RData)

if __name__ == "__main__":
    main()