def main():
    myList = []
    i = 1
    while(len(myList) != 10):
        if i % 2 == 0:
            myList.append(i)
        i += 1

    print("First 10 Even numbers:", myList)

if __name__ == "__main__":
    main()