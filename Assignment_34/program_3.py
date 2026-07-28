import sys
import psutil
import os
import time

def LogRunningProcess(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    fobj = open(os.path.join(dir, "running_process.log"), "w")
    fobj.write("Running Processes:\n")
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name", "pid", "username", "status"])
        if info["status"] == "running":
            fobj.write("Process ID:"+str(info["pid"])+"\n")
            fobj.write("Process Name:"+str(info["name"])+"\n")
            fobj.write("User name:"+str(info["username"])+"\n")
            fobj.write("---------------------------------------------\n")
    
    fobj.close()
    print(f"All processes are logged into {dir}/running_process.log file.")
        

def main():
    LogRunningProcess(sys.argv[1])

if __name__ == "__main__":
    main()