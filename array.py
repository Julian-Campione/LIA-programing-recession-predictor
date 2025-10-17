import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(df.head())
print(df.columns)

#pulling specific columns

dates = df["Date"]
yr1 = df["1 Yr"]
yr10 = df["10 Yr"]

#plot set up

plt.figure(figsize=(10,5))
plt.plot(dates, yr1, 'r-', label="Year 1") #red line for year 1
plt.plot(dates, yr10, 'b--', label="Year 10") #blue dash for year 10

#labels
plt.title("US Treasuries Over Time")
plt.xlabel("Date")
plt.ylabel("Yield %")

#legend & grid stuff
plt.legend()
plt.grid(True)

plt.show()