import schedule
import os
import time
import pathlib
import datetime

def DisplayInfo():
    # print(pathlib.Path("../marvellous_assignments"))
    print("="*100)
    now = datetime.datetime.now()
    date_ = now.strftime("%Y-%m-%d %I:%M:%S %p")
    try:
        print("Directory Scanned: ", pathlib.Path("../../marvellous_assignments"))
        for folderName, subFolderName, fileNames in os.walk(pathlib.Path("../../marvellous_assignments")):
            print("Total Files:",len(fileNames))
            print("Total subdirectories: ", len(subFolderName))
            print("Scan Time: ", date_)
            
    except Exception as fExc:
        print(fExc)

def main():
    schedule.every(1).minutes.do(DisplayInfo)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()