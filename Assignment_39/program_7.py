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

answer = model.predict(X_test)

print("Actual values are:")
print(Y_test)

print("Predicted answer is: ", answer)

#test new records

new_test_records = pd.DataFrame({
    "StudyHours":[6],"Attendance":[85],"PreviousScore":[66],"AssignmentsCompleted":[7],"SleepHours":[7]
})

new_answer = model.predict(new_test_records)

print("New predicted result", new_answer)