import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    df = pd.DataFrame({
        "Experience": [1,2,3,4,5],
        "Salary": [20000,25000,30000,35000,40000]
    })

    X = df[["Experience"]]
    y = df["Salary"]

    model = LinearRegression()
    model = model.fit(X,y)

    y_pred = model.predict([[6]])

    print("Predicted salary for 6 yrs of Exp.:", y_pred[0])

    m = model.coef_
    c = model.intercept_
    n = len(X)
    x = np.linspace(1,6,n)
    Y = m * x + c

    plt.plot(x,Y, color='g', label="Regression Line")
    plt.scatter(X,y, color='r', label="Scatter Plot")
    plt.xlabel("X: Independant Variables")
    plt.ylabel("y: Dependant Variables")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()