import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

feature_columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

def TrainAndAccuracy(feature_columns):
    X = df[feature_columns]
    y = df["FinalResult"]
    print("X shape: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accurancy = accuracy_score(y_test, y_pred)
    return accurancy

accuracy1 = TrainAndAccuracy(feature_columns)
df["SleepHours"].dropna()
feature_columns = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]
accuracy2 = TrainAndAccuracy(feature_columns)

print(f"Accuracy Before: {accuracy1*100:.2f}")
print(f"Accuracy After: {accuracy2*100:.2f}")

# After removing the SleepHours column, not affecting performance.
# It is getting 100% for previous and after deleting column accuracy.




