import pandas as pd
import matplotlib.pyplot as plt

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    subjects = ['Math', 'Science', 'English']
    data = df[df['Name'] == 'Sagar'].iloc[0]

    marks = [data['Math'], data['Science'], data['English']]

    plt.pie(marks, labels=subjects, autopct="%1.1f%%", startangle=90)

    plt.title("Pie chart of marks of Sagar")
    plt.show()

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()