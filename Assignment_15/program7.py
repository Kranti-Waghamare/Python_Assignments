#write a lambda fumction using filter() which accepts of list of strings and return list of strings having length greater than 5.

StrLength = lambda Str : len(Str) > 5 

def main():
    Data = []

    print("Enter the number of strings : ")
    Size = int(input())

    print("Enter the strings : ")

    for ch in range(Size) :
        str = input()
        Data.append(str)

    print("Input Data is ", Data)

    FData = list(filter(StrLength, Data))

    print("Data after map : ", FData)

if __name__ == "__main__":
    main()