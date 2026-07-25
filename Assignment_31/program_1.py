import schedule
import time

def DisplayMsg(msg):
    print(msg)

def main():
    message = input("Enter your message: ")
    interval = int(input("Enter the time interval: "))

    if interval > 0:
        schedule.every(interval).seconds.do(DisplayMsg, message)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Time interval should be > 0")

if __name__ == "__main__":
    main()