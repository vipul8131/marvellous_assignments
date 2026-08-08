import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_performance_ml.csv")

X_cols = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
y_col = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X_cols, y_col, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Full featured prediction: ")
print(y_pred)

df2 = pd.DataFrame([
    {
    "StudyHours": 5.0,
    "Attendance": 45,
    "PreviousScore": 55,
    "AssignmentsCompleted": 5,
    "SleepHours": 6
    },
    {
    "StudyHours": 9.0,
    "Attendance": 65,
    "PreviousScore": 75,
    "AssignmentsCompleted": 7,
    "SleepHours": 8
    },
    {
    "StudyHours": 8.0,
    "Attendance": 75,
    "PreviousScore": 65,
    "AssignmentsCompleted": 8,
    "SleepHours": 8
    },
    {
    "StudyHours": 6.0,
    "Attendance": 42,
    "PreviousScore": 35,
    "AssignmentsCompleted": 3,
    "SleepHours": 8
    },
    {
    "StudyHours": 4.0,
    "Attendance": 32,
    "PreviousScore": 45,
    "AssignmentsCompleted": 4,
    "SleepHours": 7
    }
])

y_pred = model.predict(df2)

print("New 5 students predicted result:")
print(y_pred)