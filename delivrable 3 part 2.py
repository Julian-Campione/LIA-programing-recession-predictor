
import pandas as pd

# b) d)
#a is the unemployment data set
a = pd.read_csv("US-unemployment-rate.csv")
print(a.isnull().sum())
a_ = pd.to_datetime(a["Date"])

#b is the % yeild/bond maturities 
b = pd.read_csv("yield-curve-rates-1990-2024.csv")
print(b.isnull().sum())
b_ = pd.to_datetime(b["Date"])

#c is the data set of expansion and recession
c = pd.read_csv("USREC.csv")
print(a.isnull().sum())
c_ = pd.to_datetime(c["observation_date"])

#a) 
print(a.info())
print(b.info())
print(c.info())


#c)
#the reason there are so many missing values on some month yeilds are because
#the bonds simply did not exist (the government was not issuing them at the time)
#best to just use 3m,6m,and 1yr for short term yeilds.
#there is also 1 missing value for all of them. 
#This is not going to end up mattering because there is so much data
#when using /working with the yeilds dataset just add b.dropna to the end


#This is how to find duplicates (don't do this in for final project it will screw up the whole data set)
#we need the duplicates because they do actually mean something
###print(b["6 Mo"].duplicated()) 
#same with droping duplicates
###print(b.drop_duplicates(subset=["6 Mo",]))

