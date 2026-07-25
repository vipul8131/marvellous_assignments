import schedule
import time
import os
import sys
import shutil
from datetime import datetime
from pathlib import Path

def CopyFiles(src, dest):
    now = datetime.now()
    date_ = now.strftime("%Y-%m-%d_%I_%M_%S_%p")

    srcDir = Path(src).absolute()
    destDir = Path(dest).absolute()

    fobj = open("CopiedFilesLog.txt", "w")
    for file_path in srcDir.glob("*.txt"):
        if file_path.is_file():
            shutil.copy(file_path, destDir)
            fobj.write("File copied at: "+str(date_)+str(file_path))
            print("File copied at: "+str(date_)+str(file_path))
    
    fobj.close()

def main():
    
    args = sys.argv
    if os.path.exists(args[1]) and os.path.exists(args[2]):
        if os.path.isdir(args[2]):
            schedule.every(1).minutes.do(CopyFiles, args[1], args[2])

            while True:
                schedule.run_pending()
                time.sleep(10)
        else:
            print(f"{args[2]} is not directories.")
    else:
        print("Source and destination directories are not exists.")



if __name__ == "__main__":
    main()