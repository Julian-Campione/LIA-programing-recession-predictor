import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

# arrays
dates_array = np.array(df['Date'])
m1 = np.array(df['1 Mo'])
m3 = np.array(df['3 Mo'])
m6 = np.array(df['6 Mo'])
y1 = np.array(df['1 Yr'])

y5 = np.array(df['5 Yr'])
y10 = np.array(df['10 Yr'])
y30 = np.array(df['30 Yr'])

#plot set up

plt.figure(figsize=(14,5))

    #left: short-term yield

plt.subplot(1,2,1) #1 row, 2 columns, plot 1L
plt.plot(dates_array, m1, label ='1 Mo')
plt.plot(dates_array, m3, label ='3 Mo')
plt.plot(dates_array, m6, label ='6 Mo')
plt.plot(dates_array, y1, label ='1 Yr')
plt.title("Short-Term US Treasury Yields")
plt.xlabel("Date")
plt.ylabel("Yield %")
plt.legend()
plt.grid(True)

    #right: long-term yield
    
plt.subplot(1,2,2) #1 row, 2 columns, plot 2R
plt.plot(dates_array, y5, label ='5 Yr')
plt.plot(dates_array, y10, label ='10 Yr')
plt.plot(dates_array, y30, label ='30 Yr')
plt.title("Long-Term US Treasury Yields")
plt.xlabel("Date")
plt.ylabel("Yield %")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
    