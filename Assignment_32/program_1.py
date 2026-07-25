import schedule
import time
import datetime

def CreatLog():
    now = datetime.datetime.now()
    date = now.strftime("%Y_%m_%d_%I_%M_%S")
    filename = "File_"+date+".txt"
    f1 = open(filename, "w")
    f1.write("File name: "+str(filename)+"\n")
    f1.write("Creation date: "+str(now.strftime("%Y-%m-%d"))+"\n")
    f1.write("File name: "+str(now.strftime("%I:%M:%S %p"))+"\n\n")
    print("New log file is created..!")
    f1.close()

def main():
    schedule.every(1).minutes.do(CreatLog)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()