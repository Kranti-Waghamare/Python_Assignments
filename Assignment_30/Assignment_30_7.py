'''
Write a Python program that performs a file backup every hour.

The program should:
1. Accept the source file path.
2. Accept the destination directory path.
3. Copy the source file to the destination directory.
4. Add the current date and time to the backup filename.
5. Write the backup operation details into:
backup_log.txt

Example backup filename:
Data_25_07_2026_16_30_00.txt

Example log entry:
Backup completed successfully at 25-07-2026 04:30:00 PM
Use the shutil module for file copying.
'''

import schedule
import time
import datetime
import shutil
import os

def Backup():
    try:
        source = input("Enter source file path: ")
        destination = input("Enter destination directory path: ")

        dt = datetime.datetime.now()
        timestamp = dt.strftime("%d_%m_%Y_%H_%M_%S")

        filename = os.path.basename(source)
        name, ext = os.path.splitext(filename)

        backup_name = name + "_" + timestamp + ext
        backup_path = os.path.join(destination, backup_name)

        shutil.copy2(source, backup_path)

        log = open("backup_log.txt", "a")
        log.write("Backup completed successfully at: ")
        log.write(dt.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        log.close()

        print("Backup completed successfully!")

    except FileNotFoundError:
        print("Source file or destination directory not found")

    except PermissionError:
        print("Permission denied")

def main():
    source = input("Enter source file path: ")
    destination = input("Enter destination directory path: ")

    def PerformBackup():
        try:
            dt = datetime.datetime.now()
            timestamp = dt.strftime("%d_%m_%Y_%H_%M_%S")

            filename = os.path.basename(source)
            name, ext = os.path.splitext(filename)

            backup_name = name + "_" + timestamp + ext
            backup_path = os.path.join(destination, backup_name)

            shutil.copy2(source, backup_path)

            log = open("backup_log.txt", "a")
            log.write(
                "Backup completed successfully at: "
                + dt.strftime("%d-%m-%Y %I:%M:%S %p")
                + "\n"
            )
            log.close()

            print("Backup completed successfully!")

        except FileNotFoundError:
            print("Source file or destination directory not found")

        except PermissionError:
            print("Permission denied")

    PerformBackup()
    schedule.every(1).hour.do(PerformBackup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()