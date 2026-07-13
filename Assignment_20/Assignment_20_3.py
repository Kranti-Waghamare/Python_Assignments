# create two threads which display sum of evenlist and oddlist from the list.

import threading

def EvenList(No):
    Sum = 0

    for i in No :
        if(i % 2 == 0):
            Sum = Sum + i
    
    print("summation of even list is : ", Sum)

def OddList(No):
    Sum = 0

    for i in No:
        if(i % 2 != 0):
            Sum = Sum + i
    
    print("summation of odd list is : ", Sum)

def main():
    Data = []

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target= EvenList, args= (Data,))
    t2 = threading.Thread(target= OddList, args= (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()