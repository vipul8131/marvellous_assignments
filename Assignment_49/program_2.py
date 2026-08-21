import numpy as np

def main():
    df = np.array([6,7,8,9,10,11,12])

    variance = np.var(df)
    std = np.std(df)

    print("Variance:", variance)
    print("Standard deviation:", std)

if __name__ == "__main__":
    main()