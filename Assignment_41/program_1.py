import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def GetKneighborsClassifier():
    df = pd.read_csv("WinePredictor.csv")
    # Analysis EDA and clean the data
    print(df.shape)
    df.dropna(inplace=True)
    # set independant and dependant variables
    X = df.drop(columns=['Class'])
    y = df['Class']

    # print(X.columns)
    # Split the variables
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # scaling columns
    scaler = StandardScaler()
    X_scaled_test = scaler.fit_transform(X_test)
    X_scaled_train = scaler.fit_transform(X_train)

    # Traing and Testing model
    model = KNeighborsClassifier()
    model.fit(X_scaled_train, y_train)
    y_pred = model.predict(X_scaled_test)

    print("Actual result of the model:", y_test)
    print("Predicted Result of the model: ",y_pred)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the model: {accuracy*100:.2f} %")


def main():
    GetKneighborsClassifier()

if __name__ == "__main__":
    main()