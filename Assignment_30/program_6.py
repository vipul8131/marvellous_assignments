import schedule
import time

def LunchTime():
    print("This is lunch time..!")

def WrapUp():
    print("Wrap up..!!!")

def main():
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()