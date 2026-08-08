import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
feature_Columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours","PerformanceIndex"]
X = df[feature_Columns]
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy*100:.2f} %")