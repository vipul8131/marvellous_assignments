import schedule
import time

def DisplayMsg():
    print("Coding Kar..!")

def main():
    schedule.every(30).minutes.do(DisplayMsg)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()