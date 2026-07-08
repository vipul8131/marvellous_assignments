import threading

def EvenFactor(no):
    facts = []
    sum = 0
    for i in range(1, no+1):
        if i % 2 == 0:
            facts.append(i)
            sum += i
    print(f"Even factors of {no} is {facts}")
    print(f"Sum of Even factor {no} is: {sum}")

def OddFactor(no):
    facts = []
    sum = 0
    for i in range(1, no+1):
        if i % 2 != 0:
            facts.append(i)
            sum += i
        
    print(f"Odd factors of {no} is {facts}")
    print(f"Sum of Odd factor {no} is: {sum}")

def main():
    no = int(input("Enter the number: "))
    t1 = threading.Thread(target=EvenFactor, args=(no,))
    t2 = threading.Thread(target=OddFactor, args=(no,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Exit from main!")

if __name__ == "__main__":
    main()