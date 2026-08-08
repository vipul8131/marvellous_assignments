import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("student_performance_ml.csv")
feature_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
X = df[feature_cols]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

importance = model.feature_importances_

feature_importance = pd.DataFrame(
    {"Feature": X_train.columns, "Importance": importance}
).sort_values(by="Importance", ascending=False)

print("Importance by features:")
print(feature_importance)

most_importance = feature_importance.iloc[0]
print("Most importance: ")
print(most_importance)
print("-"*50)
least_importance = feature_importance.iloc[-1]
print("Least Importance:")
print(least_importance)

