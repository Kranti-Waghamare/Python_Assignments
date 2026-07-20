'''
Write a program that accepts a directory name from the user and
counts the number of files inside it every five minutes.

Write the result into:
DirectoryCountLog.txt

Each entry should contain:
Directory path
Number of files
Date and time
'''

import os
import schedule
import time
import datetime

def CountFiles(path):
    try:
        count = 0

        for item in os.listdir(path):
            fullpath = os.path.join(path, item)

            if os.path.isfile(fullpath):
                count = count + 1

        dt = datetime.datetime.now()
        data = dt.strftime("%d-%m-%Y %I:%M:%S %p")

        fobj = open("DirectoryCountLog.txt", "a")

        fobj.write("Directory Path: " + path + "\n")
        fobj.write("Number of Files: " + str(count) + "\n")
        fobj.write("Date and Time: " + data + "\n")
        fobj.write("-----------------------------\n")

        fobj.close()

        print("Directory count recorded successfully")

    except FileNotFoundError:
        print("Directory does not exist")

    except PermissionError:
        print("Permission denied")

def main():
    path = input("Enter directory path: ")

    if not os.path.isdir(path):
        print("Invalid directory path")
        return

    CountFiles(path)

    schedule.every(5).minutes.do(CountFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()