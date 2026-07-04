#write a lambda function using filter() which accepts of list of numbers and return list of numbers divisible by both 3 and 5.

Divisible = lambda No : ((No % 3 == 0 )and (No % 5 == 0) )

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is ", Data)

    FData = list(filter(Divisible, Data))

    print("Data after map : ", FData)

if __name__ == "__main__":
    main()