import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

df["Attendance"].plot(kind="box", title="Box Plot")
plt.show()