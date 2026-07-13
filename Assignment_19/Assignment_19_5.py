'''
write a program which contains filter(), map() and reduce() in it. python application which contains one list of numbers. List contains the numbers
which are accepted from user. filter should filter out all prime numbers. 
map function will multiply each number by 2 . Reduce will return maximum number from that numbers .

Input : [2, 70, 11, 10, 17, 23, 31, 77]
List after filter : [2, 11, 17, 23, 31]
List after map : [4, 22, 34, 46, 62]
output after reduce : 62
'''
from functools import reduce

def Prime(No):
    if(No < 2):
        return False
    
    for i in range(2, No):
        if(No % i == 0):
            return False
        
    return True

Mult = lambda No: No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2


def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is : ",Data)

    FData = list(filter(Prime, Data))

    print("list after filter : ", FData)

    MData = list(map(Mult, FData))

    print("list after map : ",MData)

    RData = reduce(Maximum, MData)

    print("list after reduce : ", RData)

if __name__ == "__main__":
    main()