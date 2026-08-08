import pandas as pd

csv_file = "student_performance_ml.csv"

df = pd.read_csv(csv_file)
print("Total number of students in the dataset:", df.shape[0])

print("Number of students who passed:")
passedStudents = len(df[df["FinalResult"] == 1])
print(passedStudents)


print("Number of students who failed:")
failedStudents = len(df[df["FinalResult"] == 0])
print(failedStudents)





