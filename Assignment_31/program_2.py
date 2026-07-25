import schedule
import time

def DisplayMsg(msg):
    print(msg)

def main():
    message = input("Enter your message: ")

    schedule.every(5).seconds.do(DisplayMsg, message)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()