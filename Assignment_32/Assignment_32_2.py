'''
Write a Python program that monitors the size of a specified file
every 30 seconds.

Write the following details into:
FileSizeLog.txt
File path
File size in bytes
Date and time

Handle the situation where the file does not exist.
'''

import os
import schedule
import time
import datetime

def CheckFileSize(path):
    try:
        size = os.path.getsize(path)

        dt = datetime.datetime.now()
        data = dt.strftime("%d-%m-%Y %I:%M:%S %p")

        fobj = open("FileSizeLog.txt", "a")

        fobj.write("File Path: " + path + "\n")
        fobj.write("File Size: " + str(size) + " bytes\n")
        fobj.write("Date and Time: " + data + "\n")
        fobj.write("-----------------------------\n")

        fobj.close()

        print("File size recorded successfully")

    except FileNotFoundError:
        print("File does not exist:", path)

def main():
    path = input("Enter file path: ")

    CheckFileSize(path)

    schedule.every(30).seconds.do(CheckFileSize, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()