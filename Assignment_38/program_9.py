import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance_ml.csv")

plt.figure(figsize=(8,5))
sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)

plt.title("Final Result vs Assignments Completed")
plt.xlabel("Final Result")
plt.ylabel("Assignments Completed")
plt.show()
