# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:09:05 2025

@author: julia
"""
#a)
import pandas as pd


z = pd.read_csv("US-unemployment-recession.csv")
y = pd.read_csv("yield-curve-rates-and-recession.csv")


T_yr = pd.crosstab(z["Year"], z["Recession"])
print(T_yr)

#tyr.index is all the years (what is being looped over)
#first part of comprehensive list is making tyr.index = year
 
years_with_recession = [year for year in T_yr.index if T_yr.loc[year, 1] > 0]

#tyr.loc[year, 1] > 0 means: [look at the years, in col 1] when the value is > 0
#end up with a list of the right years


#include only the right years from original table
T_yr1 = T_yr.loc[years_with_recession]
print(T_yr1)


#this table is the unemployment level and how many times the a recession happens when at a certain level

z["Unemployment_level"] = pd.qcut(z["Unemployment_Rate"], 
                                 q=4, 
                                 labels=["Very Low","Low","High","Very High"])

T_ur = pd.crosstab(z["Unemployment_level"], z["Recession"])
print(T_ur)


#This table shows what value of the 6 month yeild and how many times it is a recession at that value

T_yye = pd.crosstab(y["6 Mo"], y["recession"])
print(T_yye)





#b)
#same as above but with all tables "normalized"
import pandas as pd


z = pd.read_csv("US-unemployment-recession.csv")
y = pd.read_csv("yield-curve-rates-and-recession.csv")


tyr = pd.crosstab(z["Year"], z["Recession"], normalize=True)
print(tyr)

#tyr.index is all the years (what is being looped over)
#first part of comprehensive list is making tyr.index = year
 
years_with_recession = [year for year in tyr.index if tyr.loc[year, 1] > 0]

#tyr.loc[year, 1] > 0 means: [look at the years, in col 1] when the value is > 0
#end up with a list of the right years


#include only the right years from original table
tyr_only_r = tyr.loc[years_with_recession]
print(tyr_only_r)



z["Unemployment_level"] = pd.qcut(z["Unemployment_Rate"], 
                                 q=4, 
                                 labels=["Very Low", "Low", "High", "Very High"])

T_ur = pd.crosstab(z["Unemployment_level"], z["Recession"], normalize=True)
print(T_ur)


#This table shows what value of the 6 month yeild and how many times it is a recession at that value
T_ur = pd.crosstab(z["Unemployment_level"], z["Recession"], normalize=True)
print(T_ur)

T_yye = pd.crosstab(y["6 Mo"], y["recession"])
print(T_yye)




#c 
import pandas as pd


z = pd.read_csv("US-unemployment-recession.csv")
y = pd.read_csv("yield-curve-rates-and-recession.csv")


z["Unemployment_level"] = pd.qcut(z["Unemployment_Rate"], 
                                 q=4, 
                                 labels=["Very Low", "Low", "High", "Very High"])
date = pd.to_datetime(z["Date"])


z["Year"] = date.dt.year #col

[z["Unemployment_level"]] #row
[z["Recession"]] #row


T_3variable = pd.crosstab(index=[z["Year"]], 
                          columns=[z["Unemployment_level"], z["Recession"]])
print(T_3variable)





