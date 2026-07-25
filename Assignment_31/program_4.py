import schedule
import time
import datetime

def CreateLogFile():
    now = datetime.datetime.now()
    createdDate = now.strftime("%Y-%m-%d_%I_%M_%S_%p")
    logFileName = "MarvellousLog_"+createdDate+".txt"
    fobj = open(logFileName, "w")
    fobj.write("Log Created successfully.\n")
    fobj.write("Created Time: "+createdDate+"\n\n")
    print("Log file created successfull!")
    fobj.close()

def main():
    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(60)
    

if __name__ == "__main__":
    main()