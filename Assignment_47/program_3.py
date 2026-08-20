import pandas as pd
from sklearn.linear_model import LinearRegression

def ModelOps(df):
    X = df[["StudyHrs", "SleepHrs"]]
    y = df["Marks"]

    model = LinearRegression()
    model = model.fit(X,y)

    print("Coefficients: ", model.coef_)

    print("Intercept: ", model.intercept_)

def main():

    df = pd.DataFrame({
        "StudyHrs": [1,2,3,4,5],
        "SleepHrs": [7,6,7,6,8],
        "Marks": [50,55,60,65,70]
    })
    ModelOps(df)

if __name__ == "__main__":
    main()