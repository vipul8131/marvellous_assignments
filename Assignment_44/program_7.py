import pandas as pd
import matplotlib.pyplot as plt

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    df.plot(x='Name', y='Total', kind='bar', width=0.5)
    plt.title("Students vs Total marks")
    plt.xlabel('Students')
    plt.ylabel('Total Marks')
    plt.grid(True)
    plt.legend()
    plt.show()
    

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()