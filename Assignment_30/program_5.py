import schedule
import time
import datetime

def LogData():
    now = datetime.datetime.now()
    date_ = now.strftime("%Y-%m-%d %I:%M:%S %p")

    try:
         fobj = open("Marvellous.txt", "a")
         fobj.write("Task executed at: "+date_+"\n")
         print("Task updated in Marvellous.txt file at", date_)

    except Exception as fexp:
        print("File not found:", fexp)

    finally:
        fobj.close()

def main():
    fobj = open("Marvellous.txt", "w")
    fobj.close()

    schedule.every(5).minutes.do(LogData)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()