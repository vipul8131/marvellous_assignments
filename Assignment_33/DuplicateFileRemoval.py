import schedule
import sys
import os
import datetime
import time
from pathlib import Path
from commands import Help, Usage
from validations import ValidateDir, ValidateEmail, ValidateInterval
from checkDuplicateFiles import CheckSum
import emailDelivery

folderCnt = 0
subFolderCnt = 0
# totalFiles = 0
receiverEmail = ""
def FindDuplicateFiles(dir):
    path_ = Path(dir).absolute()
    
    for fd, subf, fls in os.walk(path_):
        totalFiles = len(fls)
        duplicate = {}
        for fl in fls:
            flPath = os.path.join(fd, fl)
            checkSum = CheckSum(flPath)
            
            if checkSum in duplicate:
                duplicate[checkSum].append(flPath)
            else:
                duplicate[checkSum] = [flPath]

    return duplicate, totalFiles


def RemoveDuplicateFiles(dir, receiverEmail):
    startTime = time.strftime("%Y-%m-%d %H:%M:%S %p")
    data, totalFiles = FindDuplicateFiles(dir)
    # print(data)
    DuplicateData = list(filter(lambda x: len(x) > 1, data.values()))

    count = 0
    totalDuplicateFiles = 0
    totalDeletedFiles = 0
    deletedFiles = []
    for files in DuplicateData:
        for subFile in files:
            totalDuplicateFiles += 1
            count += 1
            if count > 1:
                deletedFiles.append(subFile)
                os.remove(subFile)
                totalDeletedFiles += 1
        count = 0

    endTime = time.strftime("%Y-%m-%d %H:%M:%S %p")
    # Creating log file 
    now = datetime.datetime.now()
    date_ = now.strftime("%Y_%m_%d_%I_%M_%S")
    logFileName = "DuplicateRemovalLog_"+str(date_)+".log"
    fobj = open(os.path.join("Marvellous", logFileName), "w")
    fobj.write("Deriectory Scan start time: "+str(startTime)+"\n")
    fobj.write("Directory Scan end time: "+str(endTime)+"\n")
    fobj.write("Directory Name: "+dir+"\n")
    fobj.write("Total Number of file scanned: "+str(totalFiles)+"\n")
    fobj.write("Total no. of duplicate files found: "+str(totalDuplicateFiles)+"\n")
    fobj.write("Total no. of duplicate files deleted: "+str(totalDeletedFiles)+"\n")
    fobj.write("Complete path of all deleted files: \n")
    for files_ in deletedFiles:
        fobj.write(files_+"\n")

    fobj.close()

    print("Log file is created successfully..!")

    mailBody = """Jay Ganesh,
                The Duplicate-files removal operation has been completed successfully.\n\nOperation Statistics:
                Directory Scan start time: %s
                Total Number of file scanned: %s
                Total Number of duplicate files count: %s
                Total Number of duplicate files deleted: %s
                Directory Scan end time: %s
                Name of scanned directory: %s

                Please find the detailed log file attached to this email.

                Regards,
                Vipul Bhagwat
                """ %(startTime, totalFiles, totalDuplicateFiles, totalDeletedFiles, endTime, dir)

    emailDelivery.SendEmail(receiverEmail, os.path.join("Marvellous", logFileName), mailBody)


def main():
    args = sys.argv

    if len(args) < 2:
        Help()
        return

    if args[1].lower() == "-h" or args[1].lower() == "--help":
        Help()
        return
    
    elif args[1].lower() == "-u" or args[1].lower() == "--usage":
        Usage()
        return
    else:
        if len(args) == 4:
            dirName = args[1]
            intervals = args[2]
            email = args[3]
            dirVald = ValidateDir(dirName)
            emailVld = ValidateEmail(email)
            intervalsVld = ValidateInterval(int(intervals))
            # validate directory
            if not dirVald:
                print(dirVald)
                return
            
            # validate interval
            if not emailVld:
                print(emailVld)
                return
            
            # validate interval
            if not intervalsVld:
                print(intervalsVld)
                return
            
            receiverEmail = args[3]
                    
            os.makedirs("Marvellous", exist_ok=True)
            schedule.every(int(intervals)).minutes.do(RemoveDuplicateFiles, dirName, receiverEmail)

            while True:
                schedule.run_pending()
                time.sleep(10)
            # RemoveDuplicateFiles(dirName, receiverEmail)
        else:
            print("Invalid no. of arguments passed.")
            print("Please use -h or --help for more information.")
            print("Please use -u or --usage for usage of the script.")


if __name__ == "__main__":
    main()