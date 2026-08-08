import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")
df.plot(x="SleepHours", y="FinalResult", kind="hist", grid=True)
plt.show()