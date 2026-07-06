'''
write a program which accept one number and display below pattern.
Input : 5
Output :    *   *   *   *   *
            *   *   *   *
            *   *   *   
            *   *   
            *
'''

def DisplayPattern(Row, Col):

    for i in range(1, Row + 1):
        for j in range(1, Col + 1):
            if(j >= i):
                print("*", end = "  ")

        print()


def main():
    print("Enter number of Rows : ")
    Value1 = int(input())

    print("Enter the number of Columns : ")
    Value2 = int(input())

    DisplayPattern(Value1, Value2)

if __name__ == "__main__":
    main()