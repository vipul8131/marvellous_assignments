import schedule
import time
import os
from pathlib import Path
import datetime

def CheckFileSize():
    try:
        filePath = Path("Demo.txt").absolute()
        fileSize = os.path.getsize("Demo.txt")
        now = datetime.datetime.now()
        dateAndTime = now.strftime("%Y-%m-%d %I:%M:%S %p")

        fobj1 = open("FileSizeLog.txt", "a")
        fobj1.write("File path: "+str(filePath)+"\n")
        fobj1.write("File Size: "+str(fileSize)+" bytes\n")
        fobj1.write("Date and Time: "+str(dateAndTime)+"\n\n")
        print("Log file is updated..!")
    except Exception as fExc:
        print(fExc)
    finally:   
        fobj1.close()

def main():
    fobj1 = open("FileSizeLog.txt", "w")
    fobj1.close()

    schedule.every(30).seconds.do(CheckFileSize)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()