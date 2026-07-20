'''
Write a Python program that displays the current date and time
after every one minute.

Use the datetime module.

output:
Current Date and Time: 20-07-2026 04:30:00 PM
'''

import datetime
import time

def Display():
    dt = datetime.datetime.now()
    print("Current Date and Time:", dt.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    while True:
        Display()
        time.sleep(60)

if __name__ == "__main__":
    main()