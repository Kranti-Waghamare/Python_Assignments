'''
Write a program that creates a new text file every minute.
The filename should contain the current timestamp.

Example:
File_25_07_2026_16_30_00.txt

Write the following information into the file:
Filename
Creation date
Creation time
'''

import schedule
import time
import datetime

def CreateFile():
    dt = datetime.datetime.now()

    filename = "File_" + dt.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(filename, "w")

    fobj.write("Filename: " + filename + "\n")
    fobj.write("Creation date: " + dt.strftime("%d-%m-%Y") + "\n")
    fobj.write("Creation time: " + dt.strftime("%I:%M:%S %p") + "\n")

    fobj.close()

    print("File created:", filename)

def main():
    CreateFile()

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()