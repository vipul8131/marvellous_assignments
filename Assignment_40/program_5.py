import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")
feature_Columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
X = df[feature_Columns]
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.7, random_state=42)
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"sklearn Accuracy: {accuracy*100:.2f} %")
# Checking accuracy Mannually 
count = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test.iloc[i]:
        count += 1

avg = count/len(y_pred)
print(f"Mannual Accuracy: {avg*100:.2f} %")