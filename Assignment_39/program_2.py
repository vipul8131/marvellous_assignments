import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")
# print(df.isnull().sum())

feature_Cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_Cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

model = DecisionTreeClassifier(max_depth=5)

model.fit(X_train, Y_train)

print("Model trained successfully.")

answer = model.predict(X_test)

print("Actual values are:")
print(Y_test)

print("Predicted answer is: ", answer)

