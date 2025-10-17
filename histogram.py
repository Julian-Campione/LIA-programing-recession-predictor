import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

yr10 = np.array(df['10 Yr'])

# plot 

plt.figure(figsize=(10,5))
plt.hist(yr10, bins=15, color='aliceblue', edgecolor='black')
plt.title("Distribution of Year 10 US Treasury Yields (1990-2024)")
plt.xlabel("Yield %")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()


