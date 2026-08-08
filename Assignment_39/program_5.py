import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv("student_performance_ml.csv")
# print(df.isnull().sum())

feature_Cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_Cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train, Y_train)

print("Model trained successfully.")

Y_train_pred = model.predict(X_train)
Y_test_pred = model.predict(X_test)

train_accuracy = accuracy_score(Y_train, Y_train_pred)
test_accuracy = accuracy_score(Y_test, Y_test_pred)

print(f"Train accuracy: {train_accuracy*100:.2f} %")
print(f"Test accuracy: {test_accuracy*100:.2f} %")

# Here we are getting 100% accuracy of train and test so it is good fit
