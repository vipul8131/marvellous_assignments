import threading

def EvenList(data):
    sum = 0
    evens = []
    for i in data:
        if i % 2 == 0:
            evens.append(i)
            sum += i
    print(f"Even numbers: {evens}")
    print(f"Sum of Even numbers: {sum}")

def OddList(data):
    sum = 0
    odds = []
    for i in data:
        if i % 2 != 0:
            odds.append(i)
            sum += i
    print(f"Odd numbers: {odds}")
    print(f"Sum of Odd numbers: {sum}")

def main():
    data = (3,78,34,43,89,56,88,21,68,99,43)
    t1 = threading.Thread(target=EvenList, args=(data, ))
    t2 = threading.Thread(target=OddList, args=(data, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()