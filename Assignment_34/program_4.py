import sys
import psutil
import os
import time
import emailDelivery

def LogRunningProcess(dir, email):
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
    mailBody = """
                Jay Ganesh,
                This is mail is regarding all running processes information. Please find the attached file:
            

                Thanks,
                Vipul Bhagwat
            """
    emailDelivery.SendEmail(email, os.path.join(dir, "running_process.log"), mailBody)
    print(f"All processes are logged into {dir}/running_process.log file.")
        

def main():
    if len(sys.argv) == 3:
        LogRunningProcess(sys.argv[1], sys.argv[2])
    else:
        print("Invalid number of arguments.")

if __name__ == "__main__":
    main()