import pandas as pd
from src.data_cleaning import clean_data
from src.analysis import analysis

df = pd.read_csv('Coffee_sales.csv')
df = clean_data(df)
stats = analysis(df)
print(stats["prices"])
print(stats["time_counts"])
print(stats["monthly_drinks"])