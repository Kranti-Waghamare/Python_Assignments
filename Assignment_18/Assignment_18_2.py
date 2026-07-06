'''
write a program which accept N numbers from user and store it into list. Return maximum number from that list.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34 
Output : 56
'''

def MaxElement(data):
    No = data[0]

    for Value in data:
        if(Value > No):
            No = Value
        
    return No
           
def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    Ret = MaxElement(Data)

    print("Maximum element is : ",Ret)

if __name__ == "__main__":
    main()