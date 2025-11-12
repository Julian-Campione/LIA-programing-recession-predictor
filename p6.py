#PART 6
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("US-unemployment-recession.csv")

#---------------------

    #6.1
    
        #a
        
# Faceted relational plot
p_1 = sns.relplot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    col = "Recession",
    height = 10,
    aspect = 1.2
)

p_1.fig.suptitle("Unemployment Rate Over Years: Recession vs Non-Recession", fontsize = 16)
p_1.fig.subplots_adjust(top=0.85)
p_1.set_axis_labels("Year", "Unemployment Rate (%)")


#---------------------

        #b
        
# Plot representing 5 variables at once
p_2 = sns.relplot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    hue = "Recession",
    size = "Unemployment_Rate",
    col = "Recession",
    kind = "scatter",
    height = 12,
    aspect = 1.2
    )

p_2.fig.suptitle("Unemployment Rate over Time, Highlighting Recession Periods")
p_2.fig.subplots_adjust(top=0.85)
p_2.set_axis_labels("Year", "Unemployment Rate (%)")
p_2.set_titles("Recession = {col_name}")

plt.show()

#---------------------

        #c
        
# Line plot
p_3 = sns.lineplot(
    data = data, 
    x = "Year", 
    y = "Unemployment_Rate"
    )

p_3.set_title("Unemployment Rate Over Time (Line Plot Showing Continuity)")
p_3.set_xlabel("Year")
p_3.set_ylabel("Unemployment Rate (%)")

plt.show()

#---------------------

        #d
        
# Line plot showing standard deviation
p_4 = sns.lineplot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    errorbar  = "sd"
    )

p_4.set_title("Unemployment Rate Over Time with Standard Devitation")
p_4.set_xlabel("Year")
p_4.set_ylabel("Unemployment Rate (%)")

plt.show()

#---------------------

        #e
    
# Linear regression plot

p_5 = sns.regplot(
    data = data, 
    x = "Year", 
    y = "Unemployment_Rate",
    scatter_kws = {'s':2.5, 'color': 'steelblue'},
    line_kws = {'color': 'indianred'}
    )

p_5.set_title("Linear Regression of Unemployment Rate Over Time")
p_5.set_xlabel("Year")
p_5.set_ylabel("Unemployment Rate (%)")

plt.show()

#---------------------

     #6.2
     
         #a
         
 # Categorical scatter plot with jitter 
 
p_6 = sns.stripplot(
     data = data,
     x = "Recession",
     y = "Unemployment_Rate",
     jitter = True,
     alpha = 0.5,
     size = 2
     )

p_6.set_title("Unemployment Rate by Recession Status")
p_6.set_xlabel("Recession (0 = No, 1 = Yes)")
p_6.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #b
    
 # Categorical scatter plot withou jitter 
 
p_7 = sns.stripplot(
     data = data,
     x = "Recession",
     y = "Unemployment_Rate",
     jitter = False,
     alpha = 0.5,
     size = 2
     )

p_7.set_title("Unemployment Rate by Recession Status")
p_7.set_xlabel("Recession (0 = No, 1 = Yes)")
p_7.set_ylabel("Unemployment (%)")

plt.show()

#we chose to use recession because there only two categories (yes/1 and no/0)
#therefore, when while disabling jitter slims the plot (reducing readability), it works well because there is a clear distinction between both groups -- showing that horizontal spread isn't necessary

#---------------------

        #c
    
 # Beeswarm plot
 
p_8 = sns.swarmplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Year",
    dodge = True,
    palette = "viridis",
    size = 2.5,
    alpha = 0.8
    )

p_8.set_title("Beeswarm Plot: Unemployment by Recession Period and Year")
p_8.set_xlabel("Recession (0 = No, 1 = Yes)")
p_8.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #d
    
 # Box plot

data["Decade"] = (data["Year"]//10) * 10 #this is to lower the amount of unique hues, increasing the readability by lowering the clutter

p_9 = sns.boxplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Decade",
    palette = "plasma"
    )

p_9.set_title("Box Plot: Unemployment by Recession and Decade")
p_9.set_xlabel("Recession (0 = No, 1 = Yes)")
p_9.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #e
    
 # Boxen plot
 
p_10 = sns.boxenplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Decade",
    palette = "mako"
    )

p_10.set_title("Distribution of Unemployment Rate by Recession Status")
p_10.set_xlabel("Recession (0 = No, 1 = Yes)")
p_10.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #f
    
 # Split Violin plot
 
p_11 = sns.violinplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Decade",
    split = True,
    bw_method = 0.9,
    palette = "rocket"
    )

p_11.set_title("Split Violin Plot of Unemployment Rate by Recession and Decade")
p_11.set_xlabel("Recession (0 = No, 1 = Yes)")
p_11.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #g
    
 # Violin plot

p_12 = sns.violinplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    palette = "turbo",
    inner = "point"
    )

p_12.set_title("Violin Plot of Unemployment Rate by Individual Data Point")
p_12.set_xlabel("Recession (0 = No, 1 = Yes)")
p_12.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #h
    
 # Bar plot with 97% confidence intervals

plt.figure(figsize=(8,6))
p_13 = sns.barplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Year",
    ci = 97,
    palette = "magma",
    )

p_13.set_title("Average Unemployment Rate by Recession Status (97% Confident)")
p_13.set_xlabel("Recession (0 = No, 1 = Yes)")
p_13.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #i

 # Point plot

subset = data[data["Year"].isin([1948, 1960, 1973, 1999, 2025])]
#using a subset to minimize clutter 

p_14 = sns.pointplot(
     data = subset,
     x = "Recession",
     y = "Unemployment_Rate",
     hue = "Year",
     ci = 90,
     linestyles = "--",
     palette = "magma",
     )

p_14.set_title(" Unemployment Rate by Recession Status (90% Confident)")
p_14.set_xlabel("Recession (0 = No, 1 = Yes)")
p_14.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #j

 # Simple bar plot

p_15 = sns.countplot(
    data = data,
    x = "Recession",
    palette = "cividis",
    )

p_15.set_title("Number of Observations by Recession Status")
p_15.set_xlabel("Recession (0 = No, 1 = Yes)")
p_15.set_ylabel("Counts of Observations")

plt.show()

#---------------------

    #6.3
    
        #a
        
# Heatmap of Year vs Unemployment Rate

p_16 = sns.histplot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    bins = 20,
    cbar = True,
    )

p_16.set_title("Heatmap of Year vs Unemployment Rate")
p_16.set_xlabel("Year")
p_16.set_ylabel("Unemployment (%)")

plt.show()

#---------------------
    
        #b
        
# Bivariate density plot

p_17 = sns.displot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    kind = "kde",
    fill = True,
    levels = 15,
    tresh = 0.05,
    cmap = "mako")

p_17.fig.suptitle("Bivariate Density of Unemployment Rate over Time")
p_17.set_axis_labels("Year", "Unemployment (%)")

plt.show()

#---------------------
        
        #c
        
# KDE "heatmap" plot with 3
p_18 = sns.kdeplot(
    data = data,
    x = "Year",
    y = "Unemployment_Rate",
    fill = True,
    thresh = 0.05,
    levels = 20,
    cmap= "coolwarm")

p_18.set_title("KDE Heatmap of Unemployment Rate Over Time By Recession Status")
p_18.set_xlabel("Year")
p_18.set_ylabel("Unemployment (%)")








    