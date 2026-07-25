import schedule
import datetime
import time

def DisplayTime():
    now = datetime.datetime.now()

    date_ = now.strftime("%Y-%m-%d %I:%M:%S %p")

    print(date_)

def main():
    schedule.every(1).minute.do(DisplayTime)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()