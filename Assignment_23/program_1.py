import multiprocessing
import os

def SumEvenNo(no):
    sum = 0
    for i in range(1, no+1):
        if i % 2 == 0:
            sum += i
    
    print(f"Process ID: {os.getpid()}")
    print(f"Input Number: {no}")
    print(f"Sum of Even Numbers: {sum}")
    print("="*50)

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    pobj = multiprocessing.Pool()
    pobj.map(SumEvenNo, data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()