'''
Q. Compare two files
Write a program which accepts two file names through command line arguments and compares the contents of both files.

If both files contains the same contents, display sucess
otherwise display failure

Input: Demo.txt Hello.txt

output:
success or failure
'''

import sys

def main():
    try:
        fobj = open(sys.argv[1], "r")
        sobj = open(sys.argv[2], "r")

        data1 = fobj.read()
        data2 = sobj.read()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

        fobj.close()
        sobj.close()

    except FileNotFoundError:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()