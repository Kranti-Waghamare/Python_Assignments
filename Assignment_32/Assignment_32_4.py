'''
Write a program that copies all .txt files from one directory to
another every ten minutes.

The program should:
Accept source and destination directories
Validate both directories
Copy only .txt files
Maintain a log of copied files
Avoid terminating if one file cannot be copied
'''

import os
import shutil
import schedule
import time
import datetime

def CopyFiles(source, destination):
    try:
        for filename in os.listdir(source):
            if filename.endswith(".txt"):
                srcpath = os.path.join(source, filename)
                destpath = os.path.join(destination, filename)

                if os.path.isfile(srcpath):
                    try:
                        shutil.copy2(srcpath, destpath)

                        dt = datetime.datetime.now()
                        log = open("CopyLog.txt", "a")

                        log.write("File copied: " + filename + "\n")
                        log.write("Date and Time: " +
                                  dt.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                        log.write("--------------------------\n")

                        log.close()

                        print("File copied:", filename)

                    except Exception as e:
                        print("Unable to copy", filename, ":", e)

    except OSError as e:
        print("Unable to access source directory:", e)


def main():
    source = input("Enter source directory: ")
    destination = input("Enter destination directory: ")

    if not os.path.isdir(source):
        print("Invalid source directory")
        return

    if not os.path.isdir(destination):
        print("Invalid destination directory")
        return

    CopyFiles(source, destination)

    schedule.every(10).minutes.do(CopyFiles, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()