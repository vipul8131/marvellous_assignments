import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def ModelExecution(file_path):
    df = pd.read_csv(file_path)

    print(df.head())

    # EDA
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # spliting independant and dependant variables
    X = df.drop(columns=['sales'])
    y = df['sales']
    print(X.shape)
    print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training the model
    model = LinearRegression()
    model = model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)

    print("Expected result:")
    print(y_test)
    print("-------------------------")
    print("Predicted result:")
    print(y_pred)

    print("Coefficient: ", model.coef_)
    print("Y intercept:", model.intercept_)

    MSE = mean_absolute_error(y_test, y_pred)
    print("Mean Squared Error:", MSE)

    R2 = r2_score(y_test, y_pred)
    print(f"R2: {R2*100:.2f} %")




def main():
    ModelExecution("Advertising.csv")

if __name__ == "__main__":
    main()