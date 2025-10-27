import pandas as pd
import matplotlib.pyplot as mplt

#there is no meaningful way to use a pie chart with the data sets
b = pd.read_csv("yield-curve-rates-1990-2024.csv") 
b["Date"] = pd.to_datetime(b["Date"])
latestdate = b["Date"].max()
#This part of the code is to change the date into a format that pd knows
#max() looks at the largest number aka latest date 
# looking only for the first/latestdate
latest-row = b[b["Date"] == latestdate].iloc[0]
#b[b["Date"] == latestdate means to only look at the numebers from the latest date
#iloc 0 means the first row and iloc is so that the data is not in a table (can't plot/do when in a table)

#selecting the columns that are not the date colunm (actual data)
maturity_columns = [col for col in b.columns if col != "Date"]
rates = latest-row[maturity_columns].dropna()

#code for pie chart
mplt.figure(figsize=(10,10))
mplt.pie(
 rates,
    labels=rates.index,
    autopct="%.1f%%",
    startangle=90,
    shadow=True)
mplt.title(f"U.S. Treasury Yield Curve Share by Maturity ({latestdate.date()})")
