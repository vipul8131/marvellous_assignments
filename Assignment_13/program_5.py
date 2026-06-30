# Write a program which accepts marks and prints grades
def ShowGrades(no):
    if no < 50:
        print("You are Fail!")
    elif no >= 50 and no < 60:
        print("You have got Second Class!")
    elif no >= 60 and no < 75:
        print("You have got First Class!")
    elif no >= 75:
        print("Congrats!, You've got Distinction!")

def main():
    no = int(input("Enter the mark: "))
    ShowGrades(no)

if __name__ == "__main__":
    main()