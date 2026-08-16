import pandas as pd

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    print("Shape: ", df.shape)
    print("Columns:")
    print(df.columns)
    print("Datatypes:")
    print(df.dtypes)

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()