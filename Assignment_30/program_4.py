import schedule
import time

def DisplayMsg():
    print("Namaskar..!")

def main():
    schedule.every().day.at("09:00").do(DisplayMsg)

    while True:
        schedule.run_pending()
        time.sleep(60)
    

if __name__ == "__main__":
    main()