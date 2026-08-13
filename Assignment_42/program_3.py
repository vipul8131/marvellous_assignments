import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def KnnClassifier(data, studyHrs, attdnc):
    new_point = pd.DataFrame([
        {"studyHrs":studyHrs, "Attendance":attdnc}
    ])
    df = pd.DataFrame(data)

    X = df[["studyHrs", "Attendance"]]
    y = df["Result"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # print("X_scaled:",X_scaled)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_scaled, y)

    X_scaled_test = scaler.transform(new_point)
    # print("X_scaled_test:", X_scaled_test)
    y_pred = model.predict(X_scaled_test)

    print("Predictes result is: ", y_pred)


def main():
    data = [
        {"studyHrs": 2, "Attendance":60, "Result": "Fail"},
        {"studyHrs": 5, "Attendance":80, "Result": "Pass"},
        {"studyHrs": 6, "Attendance":85, "Result": "Pass"},
        {"studyHrs": 1, "Attendance":50, "Result": "Fail"},
    ]
    studyHrs = int(input("Enter the study hours:"))
    attdnc = int(input("Enter the percentage of Attendance:"))
    KnnClassifier(data, studyHrs, attdnc)

if __name__ == "__main__":
    main()