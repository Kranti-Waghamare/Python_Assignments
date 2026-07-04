#write a lambda fumction using map() which accepts of list of numbers and return list of squares of each number.

Square = lambda No : No * No

def main():
    Data = [2, 8, 19, 6, 15,]

    print("Input Data is ", Data)

    MData = list(map(Square, Data))

    print("Data after map : ", MData)

if __name__ == "__main__":
    main()