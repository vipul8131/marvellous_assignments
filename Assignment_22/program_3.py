import multiprocessing
import os

def PrimeNo(no):
    facts = []
    primeCnt = []
    for i in range(2, no+1):
        for j in range(2,i+1):
            if i % j == 0:
                facts.append(j)

        if(len(facts) == 1):
            primeCnt.append(i)
        facts = []
    
    print(f"Factorials of {no}: {len(primeCnt)}")

def main():
    data = [10000, 20000, 30000, 40000]
    p = multiprocessing.Pool()
    p.map(PrimeNo, data)
    p.close()
    p.join()

if __name__ == "__main__":
    main()