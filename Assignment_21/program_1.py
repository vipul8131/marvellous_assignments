
import threading
def IsPrime(no):
    facts = []
    for i in range(2, no+1):
        if no % i == 0:
            facts.append(i)

    if len(facts) == 1:
        return True
    else:
        return False

def ShowPrime(data):
    primeNo = list(filter(IsPrime, data))
    print(f"Prime Numbers are: {primeNo}")

def ShowNonPrime(data):
    primeNo = list(filter(IsPrime, data))
    nonPrime = list(set(data) - set(primeNo))
    print(f"Non Prime Numbers are: {nonPrime}")

def main():
    data = [2,43,88,3,76,5,7,22,11,90,87,13,54,102,17,19,12,20,23,8,4,29,15,31]
    t1 = threading.Thread(target=ShowPrime, args=(data, ))
    t2 = threading.Thread(target=ShowNonPrime, args=(data, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()