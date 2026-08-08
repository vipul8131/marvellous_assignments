import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(f"Average Study hours:{df["StudyHours"].mean():.2f} %")

print(f"Average Attendance: {df["Attendance"].mean():.2f} %")

print(f"Maximum Previous score: {df["PreviousScore"].max()}")

print(f"Maximum Sleep Hours: {df["SleepHours"].max()}")