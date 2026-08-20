import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def ModelOps(df):
    # split the independant and dependant variables
    X = df[["Studyhrs"]]
    y = df["Marks"]

    # train the model
    model = LinearRegression()
    model = model.fit(X, y)

    # Evaluate the model
    y_pred = model.predict([[6]])

    print("Preditcted marks: ", y_pred)


def main():
    df = pd.DataFrame({
        "Studyhrs": [1,2,3,4,5],
        "Marks": [50,55,60,65,70]
    })

    ModelOps(df)

if __name__ == "__main__":
    main()