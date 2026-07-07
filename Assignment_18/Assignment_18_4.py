'''
write a program which accepts N numbers from user and store it into list. 
accept one another number from user and return frequency of that number from list.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3

'''

def ElementFrequency(data,search):
    Frequency = 0

    for no in data:
        if(no == search):
            Frequency += 1
        
    return Frequency


def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Element to search : ")
    Search = int(input())

    Ret = ElementFrequency(Data, Search)

    print(Ret)

if __name__ == "__main__":
    main()