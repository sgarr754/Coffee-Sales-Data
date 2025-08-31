import pandas as pd

df = pd.read_csv('Coffee_sales.csv')
def clean_data(df):

# ------------------------------------------------------
# Understand the dataset and clean

# Count how many rows we have in the dataset
    print(num_row = len(df))

# what are the header columns? return only the headers
    print(df.columns)

# Are there any Na values?
    print(is_na = df.isna().sum())

# Checking the data types of each column
    print(df.dtypes)

# Converting data types
    df["Date"] = pd.to_datetime(df["Date"])

# Dropping the milliseconds as some values do not have milliseconds and provides little to no value
    df["Time"] = pd.to_datetime(df["Time"].str.split(".").str[0], format="%H:%M:%S").dt.time

    print(df.dtypes)    #Checking datatypes again to see if ms was dropped

# Fiscal year starts March 1. Arranging the Monthsort column to start in March and dropping any dates after March 1, 2025
    df["Fiscalmonth"] = ((df["Monthsort"] - 3) % 12) + 1

    df = df[df['Date'] < '2025-03-01']

# Finding duplicates
    print(df.duplicated().sum())

    return df