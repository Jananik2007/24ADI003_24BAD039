import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ML/Housing.csv")

print(df.columns)
print(df.isnull().sum())

numeric_df = df.select_dtypes(include='number')

plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numeric Columns)")
plt.show()