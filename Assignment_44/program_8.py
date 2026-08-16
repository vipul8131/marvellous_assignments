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
    data = df[df['Name'] == 'Amit'].iloc[0]
    marks = [data['Math'], data['Science'], data['English']]

    plt.plot(subjects, marks, marker='o')
    plt.title("Amit's Marks across all subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()