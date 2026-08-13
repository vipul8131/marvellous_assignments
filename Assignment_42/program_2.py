import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

def GetKneighborsClassifier():
    df = pd.DataFrame([
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'},
        {'point':'E', 'X': 6, 'Y': 6, 'label': 'Blue'},
        {'point':'F', 'X': 3, 'Y': 4, 'label': 'Red'},
        {'point':'G', 'X': 3, 'Y': 2, 'label': 'Red'}
    ])

    X = df[["X", "Y"]]
    # Dependant
    y = df["label"]
    
    # Split the variables
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training and Testing model
    predicted_result = []
    k_neighbors = [1,3,5]
    for i in k_neighbors:
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print("Actual result of the model:", y_test)
        print("Predicted Result of the model: ",y_pred)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy of the model: {accuracy*100:.2f} %")

        y_pred = model.predict([[2,2]])

        print(f"Predicted result for K={i} is: {y_pred}")
    # Result is changing because of changing n_neighbors. n_neighbors is hyperparameter which is decide how many neighbors need to consider near by new_point



def main():
    GetKneighborsClassifier()

if __name__ == "__main__":
    main()