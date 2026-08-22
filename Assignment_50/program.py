import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def main():
    # Step-1: Load the data
    df = load_breast_cancer()
    X = df.data
    y = df.target

    print(X.shape)
    print(y.shape)

    # Step-2: Scaling the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # print("Scaled X:")
    # print(X_scaled)

    # Spliting the data for training dataset
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.5, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train, y_train)

    # Evaluate the data
    y_pred = model.predict(X_test)

    print("Predicted Values:")
    print(y_pred)

    print("Actual Values:")
    print(y_test)

    # Model accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Model accuracy: ", accuracy*100)

    print("Confusion matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    print("Classification report:")
    reports = classification_report(y_test, y_pred)
    print(reports)


if __name__ == "__main__":
    main()