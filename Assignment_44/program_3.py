import pandas as pd

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    print(df.value_counts())

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()