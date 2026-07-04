#write a lambda fumction using filter() which accepts of list of numbers and return list of even number.

Even = lambda No : (No % 2 == 0)

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    FData = list(filter(Even, Data))

    print("Data after map : ", FData)

if __name__ == "__main__":
    main()