import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)


recent = df.iloc[0]
yields = recent[['1 Mo', '3 Mo', '6 Mo', '1 Yr', '10 Yr', '30 Yr']]
labels = yields.index
values = yields.values

plt.figure(figsize=(10,5))
plt.bar(labels, values, color='thistle')
plt.title("US Treasury Yields on " + recent['Date'])
plt.xlabel("Lending Period")
plt. ylabel("Yield %")
plt.grid(axis='y')
plt.show()