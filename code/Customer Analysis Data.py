import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ML/marketing_campaign.csv", sep="\t")

print(df.info())
print(df.isnull().sum())
print(df.head())

df["Age"] = 2026 - df["Year_Birth"]

df["Total_Spending"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Age")
plt.title("Age Distribution of Customers")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Age"])
plt.title("Age Distribution (Box Plot)")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Income"])
plt.title("Income Distribution")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Total_Spending"])
plt.title("Customer Spending Pattern")
plt.show()
