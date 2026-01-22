import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Housing.csv")

# Inspect columns and missing values
print(df.columns)
print(df.isnull().sum())

# Only numeric columns for correlation
numeric_df = df.select_dtypes(include='number')

# Scatter plot: Area vs Price
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# Heatmap: correlation of numeric columns only
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numeric Columns)")
plt.show()