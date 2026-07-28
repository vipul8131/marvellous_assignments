import psutil

def main():
    for dtaa in psutil.process_iter():
       info = dtaa.as_dict(attrs=["pid", "name", "username", "status"])
       if info["status"] == "running":
            print("Process ID: ", info["pid"])
            print("Process Name:", info["name"])
            print("User name: ", info["username"])
            print("Status: ", info["status"])
            print("---------------------------------------")


if __name__ == "__main__":
    main()