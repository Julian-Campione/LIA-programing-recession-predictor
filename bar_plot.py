import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

recent = df.iloc[0]

# array

yields_array = np.array([recent['1 Mo'], recent['3 Mo'], recent['6 Mo'], recent['1 Yr'], recent['10 Yr'], recent['30 Yr']])
labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '10 Yr', '30 Yr']

plt.figure(figsize=(10,5))
plt.bar(labels, yields_array, color='thistle')
plt.title("US Treasury Yields on " + recent['Date'])
plt.xlabel("Lending Period")
plt. ylabel("Yield %")
plt.grid(axis='y')
plt.show()