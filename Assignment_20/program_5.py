import threading

def DisplayNo1():
    for i in range(1, 51):
        print(i, end=" ")
    print("")

def DisplayNo2():
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("")

def main():
    t1 = threading.Thread(target=DisplayNo1)
    t2 = threading.Thread(target=DisplayNo2)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
