#write a lambda fumction using map() which accepts of list of numbers and return list of squares of each number.

Square = lambda No : No * No

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    MData = list(map(Square, Data))

    print("Data after map : ", MData)

if __name__ == "__main__":
    main()