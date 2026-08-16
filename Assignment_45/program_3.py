import pandas as pd

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })
    df['Gender'] = ['Male', 'Male', 'Female']
    
    data = df.groupby('Gender').agg({
        'Math': 'mean',
        'Science': 'mean',
        'English': 'mean'
    })

    print("Group by Gender Average data:")
    print(data)
    

def main():
    DisplayInfo()

if __name__ == "__main__":
    main()