import schedule
import time
import sys
import os
import pathlib
import datetime

def CountFiles(dir):
    path_ = pathlib.Path(dir).absolute()
    fobj = open("DirectoryCountLog.txt", "a")
    for folderNames, subfolderNames, fileNames in os.walk(dir):
        fobj.write("Directory Path: "+str(path_)+"\n")
        fobj.write("No. of files: "+str(len(fileNames))+"\n")
        fobj.write("Date and Time: "+ str(datetime.datetime.now())+"\n\n")

    print("Log file is updated!")
    fobj.close()


def main():
    fobj = open("DirectoryCountLog.txt", "w")
    fobj.close()
    schedule.every(5).minutes.do(CountFiles, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()