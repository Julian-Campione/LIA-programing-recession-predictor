import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

# arrays

dates = np.array(df["Date"])
m1 = np.array(df["1 Mo"])
m3 = np.array(df["3 Mo"])
m6 = np.array(df["6 Mo"])

# filter out rows where yield is below 1%

f_dates = []
f_m1 = []
f_m3 = []
f_m6 = []

for i in range(len(dates)):
    if m1[i] > 4.0 or m3[i] > 4.0 or m6[i] > 4.0:
        f_dates.append(dates[i])
        f_m1.append(m1[i])
        f_m3.append(m3[i])
        f_m6.append(m6[i])

f_dates = np.array(f_dates)
f_m1 = np.array(f_m1)
f_m3 = np.array(f_m3)
f_m6 = np.array(f_m6)

# plot

plt.figure(figsize=(10,5))
plt.plot(f_dates, f_m1, 'r', label='1 Month')
plt.plot(f_dates, f_m3, 'g', label='3 Month')
plt.plot(f_dates, f_m6, 'b', label='6 Month')

plt.grid(True)
plt.title("Short Term US Treasury Yields Over Time (Filtered)")
plt.xlabel("Date")
plt.ylabel("Yield %")
plt.legend()
plt.show()