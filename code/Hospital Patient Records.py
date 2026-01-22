import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ML/diabetes.csv")

df.info()
df.isnull().sum()

cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols] = df[cols].replace(0, pd.NA)

sns.histplot(df["Glucose"], kde=True)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.show()

sns.boxplot(y=df["Glucose"])
plt.title("Glucose Boxplot")
plt.show()

sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()