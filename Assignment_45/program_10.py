import pandas as pd
import matplotlib.pyplot as plt

def DisplayInfo():
    df = pd.DataFrame({
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    })

    df['English'].plot(kind='box')
    plt.xlabel('English values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
def main():
    DisplayInfo()

if __name__ == "__main__":
    main()