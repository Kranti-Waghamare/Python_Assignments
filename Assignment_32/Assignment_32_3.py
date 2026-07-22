'''
Write a program that reads and displays the contents of a specified
text file every minute.

Handle the following conditions:

File does not exist
File is empty
Permission is denied
File cannot be opened
'''

import schedule
import time
import os

def DisplayContent(path):
    try:
        fobj = open(path, "r")

        data = fobj.read()
        fobj.close()

        if data == "":
            print("File is empty")
        else:
            print("File Contents:")
            print(data)

    except FileNotFoundError:
        print("File does not exist")

    except PermissionError:
        print("Permission denied")

    except OSError:
        print("File cannot be opened")

def main():
    path = input("Enter file path: ")

    DisplayContent(path)

    schedule.every(1).minutes.do(DisplayContent, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()