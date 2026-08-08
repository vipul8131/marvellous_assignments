import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

data = df["FinalResult"].value_counts()
print(data)
# Above data give you below answer.
# 1    18
# 0    12
# Based on this, this dataset is not a balanced because class-1 has more value than class 0
percentData = df["FinalResult"].value_counts(normalize=True) * 100
print("Percentage: ", percentData)
