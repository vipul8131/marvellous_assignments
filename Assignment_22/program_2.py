import multiprocessing
import os

def Factorial(no):
    print("Process ID:", os.getpid())
    print("Input Number:", no)
    facts = 1
    for i in range(1, no+1):
        facts *= i
    
    print(f"Facrorial of {no}: {facts}")
    print("="*100)

def main():
    data = [10,15,20,25]
    p = multiprocessing.Pool()
    p.map(Factorial, data)
    p.close()
    p.join()

if __name__ == "__main__":
    main()