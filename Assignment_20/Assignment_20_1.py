# print Even and Odd numbers using threading module.

import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i, end=" ")
    
    print( )

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i , end= " ")
    

    print( )

def main():

    t1 = threading.Thread(target=Even, name="Even Thread")
    t2 = threading.Thread(target=Odd, name="Odd Thread")

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()