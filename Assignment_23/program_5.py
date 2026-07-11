import multiprocessing
import os

def GetFactorial(no):
    facts = 1
    for i in range(1, no+1):
        facts *= i
    
    print(f"Process ID: {os.getpid()}")
    print(f"Input Number: {no}")
    print(f"Factorial of {no}: {facts}")
    print("="*50)

def main():
    data = [10, 15, 20, 25]
    pobj = multiprocessing.Pool()
    pobj.map(GetFactorial, data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()