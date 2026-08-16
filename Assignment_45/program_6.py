import pandas as pd
import numpy as np

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    df['Status'] = np.where(df['Total'] > 250, 'Pass', 'Fail')

    pass_count = df.value_counts(df['Status'] == 'Pass')
    print(pass_count)

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()