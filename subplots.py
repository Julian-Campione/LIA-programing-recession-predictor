import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

short_term = df[['1 Mo', '3 Mo', '6 Mo', '1 Yr']]
long_term = df[['5 Yr', '10 Yr', '30 Yr']]

#plot set up

    #left: short-term yield

plt.figure(figsize=(14,5))
plt.subplot(1,2,1) #1 row, 2 columns, plot 1L
for col in short_term.columns:
    plt.plot(df['Date'], short_term[col], label=col)
    
plt.title("Short-Term US Treasury Yields")
plt.xlabel("Date")
plt.ylabel("Yield %")
plt.legend()
plt.grid(True)

    #right: long-term yield
    
plt.subplot(1,2,2) #1 row, 2 columns, plot 2R
for col in long_term.columns:
    plt.plot(df['Date'], long_term[col], label=col)
    
plt.title("Long-Term US Treasury Yields")
plt.xlabel("Date")
plt.ylabel("Yield %")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
    