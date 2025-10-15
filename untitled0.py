import pandas as pd
import matplotlib.pyplot as mplt



a = pd.read_csv("yield-curve-rates-1990-2024.csv")

# See the first few rows and column names
print(a.head())
print(a.columns)


mplt.figure(figsize=(8, 5))
mplt.scatter(a["1 Yr"], a["10 Yr"])
mplt.title("Yield Curve: 1-Year vs 10-Year Rates")
mplt.xlabel("1-Year Treasury Yield %")
mplt.ylabel("10-Year Treasury Yield %")
mplt.grid(True)
mplt.show()