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

model1 = DecisionTreeClassifier(max_depth=None)
model2 = DecisionTreeClassifier(max_depth=1)
model3 = DecisionTreeClassifier(max_depth=3)

model1.fit(X_train, Y_train)
model2.fit(X_train, Y_train)
model3.fit(X_train, Y_train)

print("Model trained successfully.")

Y_test_pred1 = model1.predict(X_test)
Y_test_pred2 = model2.predict(X_test)
Y_test_pred3 = model3.predict(X_test)

test_accuracy_model1 = accuracy_score(Y_test, Y_test_pred1)
test_accuracy_model2 = accuracy_score(Y_test, Y_test_pred2)
test_accuracy_model3 = accuracy_score(Y_test, Y_test_pred3)

print(f"Test accuracy of max_depth=None: {test_accuracy_model1*100:.2f} %")
print(f"Test accuracy of max_depth=1: {test_accuracy_model2*100:.2f} %")
print(f"Test accuracy of max_depth=3: {test_accuracy_model3*100:.2f} %")

# Here we are getting 100% accuracy of all 3 models which is having max_depth=None, and 3.
