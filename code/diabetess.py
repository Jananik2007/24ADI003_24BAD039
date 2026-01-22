import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("diabetes.csv")

# Explore structure and missing values
df.info()
df.isnull().sum()

# Treat zero values as missing for health metrics
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols] = df[cols].replace(0, pd.NA)

# Visualize Glucose distribution
sns.histplot(df["Glucose"], kde=True)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.show()

# Glucose boxplot
sns.boxplot(y=df["Glucose"])
plt.title("Glucose Boxplot")
plt.show()

# Age distribution
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()