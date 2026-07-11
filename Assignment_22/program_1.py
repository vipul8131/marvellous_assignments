import multiprocessing

def SquareList(no):
    return no*no

def main():
    data = [1000000, 2000000, 3000000, 4000000, 5000000]
    p = multiprocessing.Pool()
    result = p.map(SquareList, data)
    p.close()
    p.join()
    print(f"Square List: {result}")

if __name__ == "__main__":
    main()