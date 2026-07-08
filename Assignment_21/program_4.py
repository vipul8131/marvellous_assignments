import threading
import queue

def SumList(data, q):
    sum = 0
    for i in data:
        sum += i
    
    q.put(sum)

def ProductList(data, q):
    product = 1
    for i in data:
        product *= i
    
    q.put(product)

def main():
    q = queue.Queue()
    data = [2,4,8,3,5,7,8,4,9,15,31]
    t1 = threading.Thread(target=SumList, args=(data, q))
    t2 = threading.Thread(target=ProductList, args=(data, q))

    t1.start()
    t2.start()

    print("Sum of list: ", q.get())
    print("Product of list: ", q.get())

if __name__ == "__main__":
    main()