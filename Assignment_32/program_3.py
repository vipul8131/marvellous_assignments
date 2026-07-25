import schedule
import time
import os
from pathlib import Path
import datetime

def DisplayData():
    fileName = "Demo.txt"
    try:
        if os.path.getsize(fileName) == 0:
            print("Demo.txt is empty file")
        else:
            try:
                fobj = open(fileName, "r")
                print(fobj.read())
                fobj.close
            except PermissionError:
                print(PermissionError)
                
    except FileNotFoundError as fnotFound:
        print(fnotFound)

def main():
    schedule.every(1).minutes.do(DisplayData)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()