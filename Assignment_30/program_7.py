import schedule
import time
import sys
import os
import datetime
import shutil
import pathlib

def CopyData(src, dest):
    
    try:
        newFileName = "Data_"+ str(datetime.datetime.now())+".txt"
        newFileName = newFileName.replace(" ", "_")
        newFileName = newFileName.replace(":", "_")

        fobj = open(src, "r")
        fobj2 = open(newFileName, "w")
        fobj2.write(fobj.read())
        fobj.close()
        fobj2.close()

        if os.path.isdir(dest):
            destFolder = pathlib.Path(dest)
            shutil.copy(newFileName, destFolder)
            print("Back up file copied into Destfolder.")
            os.remove(newFileName)
        else:
            print("Give folder name is not exist in your current directory.")

    except Exception as fileExc:
        print("File not found: ", fileExc)


def main():
    
    if len(sys.argv) == 3:
        srcFile = sys.argv[1]
        Dest = sys.argv[2]

        schedule.every().hours.do(CopyData, srcFile, Dest)

        while True:
            schedule.run_pending()
            time.sleep(60)

    else:
        print("Invalid number of arguments.")


if __name__ == "__main__":
    main()