import threading
def ShowEven():
    data = []
    for i in range(2, 21, 2):
        data.append(i)
    print(f"1st 10 Even numbers are: {data}")
    
def ShowOdd():
    data = []
    for i in range(1, 21, 2):
        data.append(i)
    
    print(f"1st 10 Odd numbers are: {data}")

def main():
    t1 = threading.Thread(target=ShowEven)
    t2 = threading.Thread(target=ShowOdd)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()