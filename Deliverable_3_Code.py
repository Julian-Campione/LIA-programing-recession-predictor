# Initial set up

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("US-unemployment-recession.csv")


# PART 2


#------------------------
# a 

print("First 5 rows:")
print(data.head())

print("Shape of dataset:")
print(data.shape)

print("Information about dataset columns:")
print(data.describe())

# b

clean_data = data.drop_duplicates()
print("Duplicates filtered and removed. New shape:", clean_data.shape)

# c
print("Missing values in each column:")
print(clean_data.isnull().sum())

# defining each column

numerical_cols = ["Year", "Unemployment_Rate"]
categorical_cols = ["Recession" ] #recession counts as categorical because 0/1 defines it as yes or no
datetime_cols = ["Date"]

# filling missing numerical values with mean
# we choose mean because it represnts and keeps the overall average of the data unchanged. Median might lean into extreme categories

# working with missing numerical values

for col in numerical_cols:
    if clean_data[col].isnull().sum() > 0: #checks for missing values
        mean_value = clean_data[col].mean()
        for i in range(clean_data.shape[0]):
            if clean_data[col][i] != clean_data[col][i]:
                clean_data[col][i] = mean_value
                
# working with missing categorical values

for col in categorical_cols:
    if clean_data[col].isnull().sum() > 0: #checks for missing values
        mode_value = clean_data[col].mode()[0] #calculates mode, most frequent category
        # loop through each columns to replace missing values with mean
        for i in range(clean_data.shape[0]):
            if clean_data[col][i] != clean_data[col][i]:
                clean_data[col][i] = mode_value 

# No missing datatime values to handle

# it should be noted that using the duplicate function reports 0 duplicates in all areas
# therefore, the raw data from the dataset = clean data
# ***to avoid confusion, the rest of the code will be reported using data and not clean_data


#PART 3


# Defining each column

for col in datetime_cols:
    data[col] = pd.to_datetime(data[col]) #conversion to proper type
# Numerical Variables

print("Numerical Variables:")
for col in numerical_cols:
        print("Variable:", col)
        print("Mean:", data[col].mean())
        print("Median:", data[col].median())
        print("Mode:", data[col].mode()[0])
        print("Standard Deviation:", data[col].std())
        print("Variance:", data[col].var())
        print("Skewness", data[col].skew())
        print("Kurtosis", data[col].kurt())
        print("Quartiles 25%, 50%, 75%:", data[col].quantile(0.25), data[col].quantile(0.50), data[col].quantile(0.75))
        print("------------------------")
        
# Categorical Variables

print("Categorical Variables:")
for col in categorical_cols:
        print("Variable:", col)
        print("Frequency Counts:")
        print(data[col].value_counts())
        print("Proportions:")
        print(data[col].value_counts(normalize=True))
        print("Mode:", data[col].mode()[0])
        print("Number of Unique Categories:", data[col].nunique())
        print("------------------------")
        
# Datetime Variables

print("Datetime Variables:")
for col in datetime_cols:
    print("Variable:", col)
    print("Earliest Date:", data[col].min())
    print("Latest Date:", data[col].max())
    print("Range:", data[col].max()-data[col].min())
    print("Number of Unique Dates:", data[col].nunique())
    print("------------------------")


#PART 4


        #a)
        
# Numerical variable = Unemployment_Rate 
# histogram
sns.histplot(data["Unemployment_Rate"], bins=20)
plt.title("Unemployment Rate Distribution")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Count")
plt.show()

# Numerical variable = Year
# histogram
sns.histplot(data["Year"], bins=20)
plt.title("Year Distribution")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()


        #b) 
        
# Numerical variable = Unemployment_Rate
# histogram with recession conditioning 
sns.histplot(data=data, x="Unemployment_Rate", hue="Recession", element="step", bins=20)
plt.title("Unemployment Rate Distribution Varying by Recession")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Count")
plt.show()

# Numerical variable = Year 
# histogram with recession conditioning
sns.histplot(data=data, x="Year", hue="Recession", element="step", bins=20)
plt.title("Year Distribution Varying by Recession")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()


        #c)
        
# Numerical variable = Unemployment_Rate
# stacked histogram
sns.histplot(data=data, x="Unemployment_Rate", hue="Recession", bins=20, multiple="stack")
plt.title("Unemployment Rate Distribution Varying by Recession")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Count")
plt.show()

# Numerical variable = Year
# stacked histogram 
sns.histplot(data=data, x="Year", hue="Recession", bins=20, multiple="stack")
plt.title("Year Distribution Varying by Recession")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()


        #d)
        
# Numerical variable = Unemployment_Rate
# histogram with bar spaces
sns.histplot(data=data, x="Unemployment_Rate", hue="Recession", bins=20, multiple="dodge")
plt.title("Unemployment Rate Distribution Varying by Recession")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Count")
plt.show()

# Numerical variable = Year
# histogram with bar spaces
sns.histplot(data=data, x="Year", hue="Recession", bins=20, multiple="dodge")
plt.title("Year Distribution Varying by Recession")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()


    #e)
    
# Numerical variable = Unemployment_Rate 
# normalized histogram
sns.histplot(data["Unemployment_Rate"], bins=20, stat="density")
plt.title("Normalized Unemployment Rate Distribution")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Density")
plt.show()

# Numerical variable = Year
# normalized histogram
sns.histplot(data["Year"], bins=20, stat="density")
plt.title("Normalized Year Distribution")
plt.xlabel("Year")
plt.ylabel("Density")
plt.show()


        #f)

# Numerical variable = Unemployment_Rate
# kernel density estimation with smoothing and color filling
sns.kdeplot(data=data, x="Unemployment_Rate", bw_adjust=0.5, fill=True)
plt.title("Kernel Density Estimation of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Density")
plt.show()

# Numerical variable = Year 
# kernel density estimation with smoothing and color filling
sns.kdeplot(data=data, x="Year", bw_adjust=0.5, fill=True)
plt.title("Kernel Density Estimation of Year")
plt.xlabel("Year")
plt.ylabel("Density")
plt.show()


        #g)
# Numerical variable = Unemployment_Rate
# empirical cumulative distribution
sns.displot(data=data, x="Unemployment_Rate", kind="ecdf")
plt.title("Empirical Cumulative Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("ECDF")
plt.show()

# Numerical variable = Year 
# empirical cumulative distribution
sns.displot(data=data, x="Year", kind="ecdf")
plt.title("Empirical Cumulative Distribution of Year")
plt.xlabel("Year")
plt.ylabel("ECDF")
plt.show()    
    

# PART 5


    # a) Crosstabs between two categorical variables

# example one: by decade (using a new subset)

data["Decade"] = (data["Year"] // 10) * 10

ct1 = pd.crosstab(data["Recession"], data["Decade"])
print("Crosstab : Recession by Decade:")
print(ct1)
print("------------------------")

# example two: recession by year category (early/mid/late)

data["Period"] = pd.qcut(data["Year"],q = 3, labels = ["Early", "Middle", "Late"])
ct2 = pd.crosstab(data["Recession"], data["Period"])
print(ct2)
print("------------------------")

# example three: unemployment level by recession

data["Unemployment_level"] = pd.qcut(data["Unemployment_Rate"], q=4, labels=["Very Low","Low","High","Very High"])
ct3 = pd.crosstab(data["Unemployment_level"], data["Recession"])
print(ct3)
print("------------------------")

# four: decade by period

ct4 = pd.crosstab(data["Decade"], data["Period"])
print("Crosstab : Decade by Period:")
print(ct4)
print("------------------------")

    # b) Crosstabs with proportions / percentages
    
ct1_norm = pd.crosstab(data["Recession"], data["Decade"], normalize = 'index')
print("Crosstab with proportions : Recession by Decade:")
print(ct1_norm)
print("------------------------")

ct2_norm = pd.crosstab(data["Recession"], data["Period"], normalize = "columns")
print("Crosstabs with proportions : Recession by Period (normalized by columns):")
print(ct2_norm)
print("------------------------")

  # b) Three-way frequency table (Recession, Decade and Period)

ct3way = pd.crosstab(index=[data["Recession"], data["Decade"]], columns=data["Period"])
print("Three-way Crosstab : Recession, Decade, Period:")
print(ct3way)
print("------------------------")


#PART 6


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

plt.show()


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

p_4.set_title("Unemployment Rate Over Time with Standard Deviation")
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

p_6.set_title("Strip Plot (with Jitter): Unemployment by Recession")
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

p_7.set_title("Strip Plot (No Jitter): Unemployment by Recession")
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

#we use decades here. This is to lower the amount of unique hues, increasing the readability by lowering the clutter

p_9 = sns.boxplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Decade",
    palette = "viridis"
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
    palette = "viridis"
)

p_10.set_title("Boxen Plot: Distribution of Unemployment Rate by Recession Status")
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
    palette = "viridis"
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
    palette = "viridis",
    inner = "point"
    )

p_12.set_title("Violin Plot: Unemployment Rate by Individual Data Point")
p_12.set_xlabel("Recession (0 = No, 1 = Yes)")
p_12.set_ylabel("Unemployment (%)")

plt.show()

#---------------------

        #h
    
 # Bar plot with 97% confidence intervals (CI)

plt.figure(figsize=(8,6))
p_13 = sns.barplot(
    data = data,
    x = "Recession",
    y = "Unemployment_Rate",
    hue = "Year",
    ci = 97,
    palette = "viridis",
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
     palette = "viridis",
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
    palette = "viridis",
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
    cmap = "viridis"
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
    thresh = 0.05,
    cmap = "viridis")

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
    hue = "Recession",
    fill = True,
    thresh = 0.05,
    levels = 20,
    cmap= "viridis")

p_18.set_title("KDE Heatmap of Unemployment Rate Over Time By Recession Status")
p_18.set_xlabel("Year")
p_18.set_ylabel("Unemployment (%)")

plt.show()





    
        
