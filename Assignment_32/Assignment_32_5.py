'''
Write a program that deletes all empty files from a specified
directory every hour.

The program should:
Scan the directory recursively
Detect files whose size is zero bytes
Delete the empty files
Store deleted file paths in a log file
Handle permission errors

Test the program only on a sample directory.
'''

import os
import schedule
import time
import datetime

def DeleteEmptyFiles(path):
    try:
        for root, dirs, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)

                try:
                    if os.path.getsize(filepath) == 0:
                        os.remove(filepath)

                        dt = datetime.datetime.now()
                        log = open("DeletedFilesLog.txt", "a")

                        log.write("Deleted File: " + filepath + "\n")
                        log.write(
                            "Date and Time: "
                            + dt.strftime("%d-%m-%Y %I:%M:%S %p")
                            + "\n"
                        )
                        log.write("--------------------------\n")

                        log.close()

                        print("Deleted:", filepath)

                except PermissionError:
                    print("Permission denied:", filepath)

                except OSError as e:
                    print("Unable to process file:", filepath, e)

    except PermissionError:
        print("Permission denied for directory:", path)

    except OSError as e:
        print("Unable to scan directory:", e)


def main():
    path = input("Enter sample directory path: ")

    if not os.path.isdir(path):
        print("Invalid directory path")
        return

    confirm = input(
        "This program deletes empty files. Continue? (yes/no): "
    )

    if confirm.lower() != "yes":
        print("Operation cancelled")
        return

    DeleteEmptyFiles(path)

    schedule.every(1).hour.do(DeleteEmptyFiles, path)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()