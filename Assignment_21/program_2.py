import threading
from functools import reduce

def MaxNo(data):
    max = 0
    for i in range(len(data)):
        if max < data[i]:
            max = data[i]
        
    print(f"Max number: {max}")

def MinNo(data):
    min = data[0]
    for i in range(len(data)):
        if min > data[i]:
            min = data[i]

    print(f"Max number: {min}")

def main():
    data = [2,43,88,3,76,5,7,22,11,90,87,1,13,54,102,17,19,12,20,23,8,4,29,15,31]
    t1 = threading.Thread(target=MaxNo, args=(data,))
    t2 = threading.Thread(target=MinNo, args=(data,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()