import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_campaign.csv", sep="\t")

df.info()
df.isnull().sum()
df.head()

df["Age"] = 2026 - df["Year_Birth"]

df["Total_Spending"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

sns.set(style="whitegrid")

sns.countplot(x="Age", data=df)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.xticks(rotation=90)  
plt.show()

sns.boxplot(y=df["Income"])
plt.title("Income Distribution")
plt.ylabel("Income")
plt.show()

sns.boxplot(y=df["Total_Spending"])
plt.title("Customer Spending Pattern")
plt.ylabel("Total Spending")
plt.show()


