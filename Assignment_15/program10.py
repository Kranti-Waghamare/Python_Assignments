#write a lambda fumction using filter() which accepts of list of numbers and return count of even number.

CountEven = lambda No : (No % 2 == 0) 

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    FData = list(filter(CountEven, Data))

    print("Data after map : ", len(FData))

if __name__ == "__main__":
    main()