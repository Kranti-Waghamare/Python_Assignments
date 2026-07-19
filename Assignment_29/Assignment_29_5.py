'''
Q. Frequency of file in a string
Write a program which accepts two file name one string from user and returns the frequency(Count of occurance) of that string in the file

If both files contains the same contents, display sucess
otherwise display failure

Input: Demo.txt Marvellous

output:
Count how many times "Marvellous" appears in Demo.txt
'''

import sys

def main():
    try:
        fobj = open(sys.argv[1], "r")

        data = fobj.read()

        fobj.close()

        name = input("Enter the string to search: ")

        count = data.count(name)

        print("Frequency is:", count)

    except FileNotFoundError:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()