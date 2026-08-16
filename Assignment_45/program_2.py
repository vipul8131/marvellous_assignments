import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })
    df['Gender'] = ['Male', 'Male', 'Female']
    encoder = OneHotEncoder(sparse_output=False)
    encoded_gender = encoder.fit_transform(df[['Gender']])
    print(encoded_gender)
    

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()