import pandas as pd
import matplotlib.pyplot as plt

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df['Mathematics'] = df['Math']
    df = df.drop(columns=['Math'])

    print(df.value_counts())
    
def main():
    DisplayInfo()

if __name__ == "__main__":
    main()