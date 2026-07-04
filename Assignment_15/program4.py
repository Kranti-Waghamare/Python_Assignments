#write a lambda fumction using reduce() which accepts of list of numbers and return Addition of all elements.

from functools import reduce

Add = lambda No1, No2 : No1 + No2

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    RData = reduce(Add, Data)

    print("Data after map : ", RData)

if __name__ == "__main__":
    main()