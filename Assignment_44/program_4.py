import pandas as pd

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    data = df[df['Science'] > 85]
    print("Students who scored marks greater than 85 in Science:")
    print(data)

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()