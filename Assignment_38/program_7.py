import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_performance_ml.csv")
# print(df["FinalResult"].unique())
for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    # print(temp)
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = sp)


plt.title("Student Performance Study")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid()
plt.show()