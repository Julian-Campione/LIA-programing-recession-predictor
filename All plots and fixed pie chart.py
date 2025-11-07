#Scatter plot
import pandas as pd
import matplotlib.pyplot as mplt


a = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv")

# See the first few rows and column names
print(a.head())
print(a.columns)

#code for scatter plot
mplt.figure(figsize=(8, 5))
mplt.scatter(a["1 Yr"], a["10 Yr"])
mplt.title("Yield Curve: 1-Year vs 10-Year Rates")
mplt.xlabel("1-Year Treasury Yield %")
mplt.ylabel("10-Year Treasury Yield %")
mplt.grid(True)
mplt.show()






#Pie chart:
import pandas as pd
import matplotlib.pyplot as mplt

#there is no meaningful way to use a pie chart with the data sets
b = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv") 
b["Date"] = pd.to_datetime(b["Date"])
latestdate = b["Date"].max()
#This part of the code is to change the date into a format that pd knows
#max() looks at the largest number aka latest date 
# looking only for the first/latestdate
latestrow = b[b["Date"] == latestdate].iloc[0]
#b[b["Date"] == latestdate means to only look at the numbers from the latest date
#iloc 0 means the first row and iloc is so that the data is not in a table (can't plot/do when in a table)

#selecting the columns that are not the date column (actual data)
#this is a comprehensive list, basically applying a loop to a list then putting it in another list
maturity_columns = [col for col in b.columns if col != "Date"]
rates = latestrow[maturity_columns].dropna()

#code for pie chart
#go to https://matplotlib.org/ for everything matplot.
mplt.figure(figsize=(10,10))
mplt.pie(
 rates,
    labels=rates.index,
    autopct="%.1f%%",
    startangle=90,
    shadow=True)
mplt.title(f"U.S. Treasury Yield Curve Share by Maturity ({latestdate.date()})")
#autopct is to show the percentages
#in the title: f"bla bla bla {variable}" This is an f string. plt.title does not work like the print() function



#Histogram:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv")
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





#Sub plots (added arrays)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv")
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





#Grid and filtered data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv")
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




