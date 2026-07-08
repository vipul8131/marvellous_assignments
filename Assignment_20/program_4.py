import threading

def Small(strs):
    count = 0
    for i in strs:
        if i.islower() == True:
            count += 1
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Small letters in {strs} is {count}")
    print("="*30)

def Capitals(strs):
    count = 0
    for i in strs:
        if i.isupper() == True:
            count += 1

    print(f"Thread ID: {threading.get_ident()}")
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Capital letters in {strs} is {count}")
    print("="*30)

def Digits(strs):
    count = 0
    for i in strs:
        if i.isdigit() == True:
            count += 1
    
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Digits in {strs} is {count}")
    print("="*30)

def main():
    myStr = input("Enter the string: ")
    t1 = threading.Thread(target=Small, args=(myStr, ))
    t2 = threading.Thread(target=Capitals, args=(myStr, ))
    t3 = threading.Thread(target=Digits, args=(myStr, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main!")

if __name__ == "__main__":
    main()