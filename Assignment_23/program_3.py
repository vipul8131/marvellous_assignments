import multiprocessing
import os

def CountEven(no):
    evenNoCnt = 0
    for i in range(1, no+1):
        if i % 2 == 0:
            evenNoCnt += 1
    
    print(f"Process ID: {os.getpid()}")
    print(f"Input Number: {no}")
    print(f"Even Number count: {evenNoCnt}")
    print("="*50)

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    pobj = multiprocessing.Pool()
    pobj.map(CountEven, data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()