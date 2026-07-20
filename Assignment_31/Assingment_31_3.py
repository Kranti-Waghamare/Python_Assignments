'''
Write a program that scans a specified directory every minute.

The task should display:
Directory name
Number of files
Number of subdirectories
Date and time of scanning

Use the os module.

Example output:

Directory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4

Scan Time: 20-07-2026 04:30:00 PM
'''

import os
import schedule
import time
import datetime

def ScanDirectory(path):
    try:
        files = 0
        folders = 0

        for item in os.listdir(path):
            fullpath = os.path.join(path, item)

            if os.path.isfile(fullpath):
                files = files + 1
            elif os.path.isdir(fullpath):
                folders = folders + 1

        dt = datetime.datetime.now()

        print("Directory Scanned:", path)
        print("Total Files:", files)
        print("Total Subdirectories:", folders)
        print("Scan Time:", dt.strftime("%d-%m-%Y %I:%M:%S %p"))
        print()

    except FileNotFoundError:
        print("Directory does not exist")

    except PermissionError:
        print("Permission denied")

def main():
    path = input("Enter directory path: ")

    if not os.path.isdir(path):
        print("Invalid directory path")
        return

    ScanDirectory(path)

    schedule.every(1).minutes.do(ScanDirectory, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()