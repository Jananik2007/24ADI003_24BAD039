import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ML/data.csv", encoding="ISO-8859-1")

print(df.head())
print(df.info())
print(df.isnull().sum())

df["Sales"] = df["Quantity"] * df["UnitPrice"]

sales = df.groupby("Description", as_index=False)["Sales"].sum().head(5)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 10))
sns.barplot(data=sales, x="Description", y="Sales")
plt.title("Top 5 Products by Sales")
plt.show()

plt.figure(figsize=(12, 10))
sns.lineplot(data=sales, x="Description", y="Sales", marker="o")
plt.title("Sales Trend of Top 5 Products")
plt.show()
