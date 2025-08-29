import pandas as pd
from src.data_cleaning import clean_data
from src.analysis import analysis

df = pd.read_csv('Coffee_sales.csv')
pd.set_option('display.max_rows', None)

df = clean_data(df)
stats = analysis(df)

print("\nDrink types and average prices")
print(stats["prices"])

print("\nDrinks, annual revenue, and number of drinks sold")
print(stats["top_drinks"])

print("\nNumber of drinks sold per month")
print(stats["monthly_drinks"])

print("\nHow much each drink sells per month")
print(stats["monthly_drink_type"])

print("\nDrinks sold per hour annually")
print(stats["hourly_drinks"])

print("\nDrinks sold per hour in each month")
print(stats["hourly_drinks_per_month"])

print("\nNumber of Drinks sold Time of Day annually")
print(stats["drinks_TOD"])

print("\nNumber of drinks sold Time of Day per month")
print(stats["drinks_TOD_per_month"])

print("\nTypes of drinks sold per TOD each month")
print(stats["drink_type_per_TOD"])

print("\nDrinks sold during the week annully")
print(stats["weekly_drinks"])

print("\nType of rinks sold during the week annually")
print(stats["weekday_drink_types"])

print(stats["payment_type"])

print(stats["daily_sales"])