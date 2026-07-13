# create two threads which prints evenfactors and oddfactors.

import threading

def SumEvenFactor(No):
    Sum = 0

    if(No < 0):
        No = -No

    for i in range(2, No+1, 1):
        if((No % i == 0) and (i % 2 == 0)):
            Sum = Sum + i

    print("Summation of even factors is :",Sum)

def SumOddFactor(No):
    Sum = 0

    if(No < 0):
        No = -No

    for i in range(2, No+1, 1):
        if((No % i == 0) and (i % 2 != 0)):
            Sum = Sum + i

    print("Summation of odd factors is :",Sum)


def main():
    print("Enter the number : ")
    Value = int(input())

    t1 = threading.Thread(target= SumEvenFactor, args= (Value,))
    t2 = threading.Thread(target= SumOddFactor, args= (Value,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()