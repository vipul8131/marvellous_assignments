import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    scaler = MinMaxScaler()
    df['Normalized_math'] = scaler.fit_transform(df[['Math']])
    print(df.value_counts())

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()