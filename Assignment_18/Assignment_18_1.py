'''
write a program which accept N numbers from user and store it into list. Return addition of all elements from that list.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
'''

def AddElements(data):
    Sum = 0

    for no in data:
        Sum = Sum + no

    return Sum

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = AddElements(Data)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()