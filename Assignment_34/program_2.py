import psutil
import sys

def GetProcess():
    processList = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name", "status"])
        if info["status"] == "running":
            processList.append(info)

    return processList

def FindProcess(processName):
    data = GetProcess()
    for i in data:
        if i['name'] == processName:
            return i

def main():
    print("Process name", FindProcess(sys.argv[1]))


if __name__ == "__main__":
    main()