import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    df = pd.DataFrame([[25,20000], [30,40000], [35,80000]])

    scaler = StandardScaler()
    df = scaler.fit_transform(df)

    print("Scaled dataset: ", df)

if __name__ == "__main__":
    main()