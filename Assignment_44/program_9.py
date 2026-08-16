import pandas as pd
import numpy as np
def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan,76, 88],
        'Science': [91,np.nan,85]
    })
    
    math_mean = df['Math'].mean()
    sci_mean = df['Science'].mean()

    df.fillna({'Math': math_mean, 'Science': sci_mean}, inplace=True)
    print(df.value_counts())

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()