import schedule
import time

def DisplayMessage(msg):
    print(msg)

def main():
    schedule.every().monday.at("09:00").do(DisplayMessage, "Start your weekly goals.")
    schedule.every().wednesday.at("17:00").do(DisplayMessage, "Review your weekly progress.")
    schedule.every().friday.at("18:00").do(DisplayMessage, "Weekly work completed.")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()