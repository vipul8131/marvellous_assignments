import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv", index_col=0)


    X = df[["Wether", "Temperature"]]
    y = df["Play"]

    print(X.shape)
    print(y.shape)

    one_hotencoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    X_encoded = one_hotencoder.fit_transform(X)

    print("X_encoded: ", X_encoded)

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    print("y_encoded:", y_encoded)

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.3, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"Accuracy: {accuracy*100:.2f} %")

    new_point = pd.DataFrame([{"Wether": "Sunny", "Temperature": "Cool"}])

    new_point_encod = one_hotencoder.transform(new_point)

    y_pred = model.predict(new_point_encod)

    print("Predicted result: ")
    print(y_pred)

if __name__ == "__main__":
    main()