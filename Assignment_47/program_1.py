import pandas as pd
from sklearn.linear_model import LinearRegression

def DisplayInfo(df):
    X = df[["StudyHrs"]]
    y = df["Marks"]
    # train the model
    model = LinearRegression()
    model = model.fit(X, y)

    print("Coefficient: ", model.coef_)

    print("Intercept: ", model.intercept_)

def main():
    df = pd.DataFrame({
        "StudyHrs": [1,2,3,4,5],
        "Marks": [50,55,60,65,70]
    })

    DisplayInfo(df)

if __name__ == "__main__":
    main()