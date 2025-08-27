import pandas as pd

df = pd.read_csv('Coffee_sales.csv')

# print(df.to_string()) #Print whole dataset

# -------------------------------------------------------
# Understand the dataset

# Before: Lets see how many rows of data is in the dataset
#After: there are 3547 rows.
num_row = len(df)
print(num_row)

# what are the header columns? return only the headers
print(df.head(0))

# Drop any rows with NULL values.
# When counting the new datframe, the smae amount of rows came up, so we can understand that there are no rows with any NULL values
newdf = df.dropna()
new_num_row = len(newdf)
print(new_num_row)