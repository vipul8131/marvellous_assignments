import numpy as np
from sklearn.preprocessing import StandardScaler

def CalculateEucDistance(x, y):
    return np.sqrt(((x[0] - y[0])**2) + ((x[1]-y[1])**2))

def DataLoop(df,new_point):
    data = []
    for i in range(len(df)):
        data.append(CalculateEucDistance(df[i], new_point))

    return data


def main():
    df = np.array([[1,100],
                    [2,200],
                    [3,300],
                    [4,400],
                    [5,500]
                    ])
    new_point = [6,600]
    distances = DataLoop(df, new_point)

    print("Before scaling distance:")
    print(distances)

    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    print("Scaled dataset:", df)
    
    distances = DataLoop(df, new_point)
    print("After scaling distance:")
    print(distances)

if __name__ == "__main__":
    main()