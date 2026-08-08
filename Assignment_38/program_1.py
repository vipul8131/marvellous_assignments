import pandas as pd

csv_file = "student_performance_ml.csv"

df = pd.read_csv(csv_file)

print("First 5 records: ")
print(df.head())

print("Last 5 records: ")
print(df.tail())

print("Total Number Rows and Columns:")
print(df.shape)

print("List of column names:")
print(df.columns)

print("Data type of each columns:")
print(df.dtypes)


