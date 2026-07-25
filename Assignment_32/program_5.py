import schedule
import time
import os
from datetime import datetime
import sys
from pathlib import Path

def DeleteEmptyFiles(src):
    now = datetime.now()
    date_ = now.strftime("%Y-%m-%d_%I_%M_%S_%p")
    try:
        fobj = open("DeleteFileLogs.txt", "w")
        if os.path.isdir(src):
            for f, fsub, fls in os.walk(src):
                for fl in fls:
                    
                    filePath = os.path.join(f, fl)
                    
                    if os.path.exists(filePath) and os.path.getsize(filePath) == 0:
                        print(str(filePath)+" file is deleting")
                        os.remove(filePath)
                        fobj.write(fl+" file is deleted at "+str(date_)+"\n")
            
            fobj.close()
    except Exception as fExp:
        print(fExp)


def main():
    args = sys.argv

    schedule.every().hours.do(DeleteEmptyFiles, args[1])

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()