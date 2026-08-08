import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

###########################################
# Step-1: Load the dataset
###########################################
df = pd.read_csv("student_performance_ml.csv")

print("dataset loaded successfully")

###########################################
# Step-2: Data Analysis (EDA)
###########################################

print("Shape of dataset: ", df.shape)
print("Columns names:", list(df.columns))
print("Missing values per columns: ")
print(df.isnull().sum())

print("Class distribution (FinalResult count):")
print(df["FinalResult"].value_counts())

print("Statistical report of dataset: ")
print(df.describe())

###########################################
# Step-3: Decide Independat and Dependant variables
###########################################

# X = Independant variable / Feature
# Y = Dependant Variable / labels

feature_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape: ", X.shape)
print("Y shape: ", Y.shape)

###########################################
# Step-4: Visualization of dataset
###########################################

# scatter plot
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = sp)


plt.title("Student Performance Case Study")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid()
plt.show()

###########################################
# Step-5: Split the dataset for training and testing
###########################################

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("X: ", X.shape)
print("Y: ", Y.shape)

print("Dataset spliting activity done.")
print("X_train: ", X_train.shape) # (75, 4)
print("X_test: ", X_test.shape) # (75, 4)
print("Y_test: ", Y_test.shape) # (75,)
print("Y_train: ", Y_train.shape) # (75,)

###########################################
# Step-6: Build the model
###########################################

model = DecisionTreeClassifier(max_depth=5)
print("Model gets created successfully.")

###########################################
# Step-7: Train the model
###########################################

model.fit(X_train, Y_train)

print("Model trained successfully.")

###########################################
# Step-8: Evaluate the model/Testing
###########################################

Y_pred = model.predict(X_test)

print("Model testing is completed.")

print("Excepted answers: ")
print(Y_test)

print("Predicted answer:")
print(Y_pred)

###########################################
# Step-9: Evaluate the model performance
###########################################

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of model is: ", accuracy * 100, "%")

print("Confusion metrix:")
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

print("classification Report")
print(classification_report(Y_test, Y_pred))
