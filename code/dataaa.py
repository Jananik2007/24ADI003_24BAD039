import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

print(df.head())
print(df.info())
print(df.isnull().sum())

df["Sales"] = df["Quantity"] * df["UnitPrice"]
sales = df.groupby("Description")["Sales"].sum().head(5)
plt.figure(figsize=(12,10))
sales.plot(kind="bar")
plt.show()

sales.plot(kind="line")
plt.show()