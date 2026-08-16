import pandas as pd
import numpy as np

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df.to_csv('studetns.csv')
    
def main():
    DisplayInfo()

if __name__ == "__main__":
    main()