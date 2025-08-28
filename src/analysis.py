def analysis(df):
    # what are the header columns? return only the headers
    print(df.head())

    # What drinks do we have and their average prices
    drinks_and_price = df.groupby('coffee_name')['money'].mean().round(2)

    # How many drinks are bought in each time of day in the year
    drinks_TOD = df["Time_of_Day"].value_counts()

    # What months show up in the dataset?
    # Months = (df[["Month_name", 'Monthsort']].drop_duplicates().sort_values('Monthsort'))
    # print(Months)

    # How many drinks are bought in each month
    monthly_drinks = df.groupby(['Monthsort', 'Month_name']).size().sort_index(level='Monthsort')

    return {"prices": drinks_and_price, "time_counts": drinks_TOD, "monthly_drinks": monthly_drinks}
