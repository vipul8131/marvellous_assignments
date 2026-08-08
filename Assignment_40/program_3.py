import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

feature_columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

def TrainAndAccuracy(feature_columns):
    X = df[feature_columns]
    y = df["FinalResult"]
    print("x.shape", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

full_Feature_acc = TrainAndAccuracy(feature_columns)
feature_columns = ["StudyHours","Attendance"]
only_two_feature_acc = TrainAndAccuracy(feature_columns)
print(f"Full Featured Accuracy: {full_Feature_acc*100:.2f} %")
print(f"StudyHours and Attendance Accuracy: {only_two_feature_acc*100:.2f} %")