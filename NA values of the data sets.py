
import pandas as pd


#a is the unemployment data set
a = pd.read_csv("C:/Users/julia/OneDrive/Documents/US-unemployment-rate.csv")
print(a.isnull().sum())

#b is the % yeild/bond maturities 
b = pd.read_csv("C:/Users/julia/OneDrive/Documents/yield-curve-rates-1990-2024.csv")
print(b.isnull().sum())

#c is the data set of expansion and 
c = pd.read_csv("C:/Users/julia/OneDrive/Documents/USREC.csv")
print(a.isnull().sum())


print(a.info())
print(b.info())
print(c.info())


#the reason there are so many missing values on some month yeilds are because
#the bonds simply did not exist (the government was not issuing them at ther time)
#best to just use 3m,6m,and 1yr for short term yeilds.
#there is also 1 missing value for all of them. 
#This is not going to end up mattering because there is so much data
#when using /working with the yeilds dataset just add b.dropna to the end
