#PART 3
import pandas as pd

data = pd.read_csv("US-unemployment-recession.csv")

# Defining each column

numerical_cols = ["Year", "Unemployment_Rate"]
categorical_cols = ["Recession", "Date" ] #recession counts as categorical because 0/1 defines it as yes or no

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
        
        