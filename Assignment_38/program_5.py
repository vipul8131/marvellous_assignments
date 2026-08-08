import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print(df.groupby("FinalResult")["StudyHours"].mean())
# Result
# 0    2.550000
# 1    6.372222

print(df.groupby("FinalResult")["Attendance"].mean())
# Result
# 0    67.750000
# 1    86.611111
