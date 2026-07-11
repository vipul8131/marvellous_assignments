import multiprocessing
import time

def Multiply(no):
    sum = 0
    for i in range(1, no+1):
        sum += (i**5)
    
    print(f"5 Power of every element till {no}: {sum}")

def main():
    data = [1000000,2000000,3000000,4000000]
    p = multiprocessing.Pool()
    startTime = time.perf_counter()
    p.map(Multiply, data)
    p.close()
    p.join()
    endTime = time.perf_counter()
    print(f"Required time: {endTime - startTime:.4f} seconds")

if __name__ == "__main__":
    main()