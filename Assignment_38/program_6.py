import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

df["StudyHours"].plot(kind="hist", bins=10, edgecolor="black")

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Study hours")
plt.show()