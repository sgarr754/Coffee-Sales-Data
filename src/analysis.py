import pandas as pd

def analysis(df):
    # what are the header columns? return only the headers
    # print(df.head())

    # What drinks do we have and their average prices
    drinks_and_price = df.groupby('coffee_name')['money'].mean().round(2)

    # What are the top-selling drinks and how much have they sold annually?
    top_drinks = df.groupby('coffee_name')['money'].agg(['sum','count']).sort_values(by='count', ascending=False)

    # How many drinks are bought in each month? How much is the monthly revenue?
    monthly_drinks = df.groupby(['Fiscalmonth', 'Month_name'])['money'].agg(['count','sum']).sort_index(level='Fiscalmonth')

    # Which drinks sell in each month?
    monthly_drink_type = df.groupby(['Fiscalmonth', 'Month_name'])['coffee_name'].value_counts().sort_index(level='Fiscalmonth')
    
    # Drinks sold per hour annually
    hourly_drinks = df.groupby('hour_of_day')['money'].agg(['count', 'sum']).sort_index(level='hour_of_day')

    # Drinks sold per hour monthly
    hourly_drinks_per_month = df.groupby(['Fiscalmonth', 'Month_name','hour_of_day'])['money'].agg(['count', 'sum']).sort_index(level='Fiscalmonth')
    
    # How many drinks are bought in each time of day in the year
    drinks_TOD = df.groupby("Time_of_Day")['money'].agg(['count', 'sum'])

    # How many drinks are bought in each time of day per month
    TOD_order = ["Morning", "Afternoon", "Night"] #Ordering TOD to the correct order

    drinks_TOD_per_month = (
        df.assign(Time_of_Day=pd.Categorical(df["Time_of_Day"],categories=TOD_order, ordered=True)) #Changing the order of the TOD to Morning, Afternoon, and Night
        .groupby(["Fiscalmonth", "Month_name", "Time_of_Day"],observed=True)['money'].agg(['count', 'sum']).sort_index(level=["Fiscalmonth", "Time_of_Day"])  
    )

    drinks_TOD_per_month = drinks_TOD_per_month[(drinks_TOD_per_month > 0).any(axis=1)]

    # Which drinks sell TOD per month
    drink_type_per_TOD = (
        df.assign(Time_of_Day=pd.Categorical(df["Time_of_Day"],categories=TOD_order, ordered=True)) #Changing the order of the TOD to Morning, Afternoon, and Night
        .groupby(["Fiscalmonth", "Month_name", "Time_of_Day", "coffee_name"], observed=True).size().sort_index(level=["Fiscalmonth", "Time_of_Day"])  
    )
    drink_type_per_TOD = drink_type_per_TOD[drink_type_per_TOD > 0]

    # How many drinks are bought in the days of the week annually?
    weekly_drinks = df.groupby(['Weekdaysort', 'Weekday'])['money'].agg(['count','sum']).sort_index(level='Weekdaysort')

    # What type of drinks are sold in the weekday?
    weekday_drink_types = df.groupby(['Weekdaysort', 'Weekday'])['coffee_name'].value_counts().sort_index(level='Weekdaysort')

    # How many transactions were through card vs. cash?
    payment_type = df['cash_type'].value_counts()

    # Daily sales
    daily_sales = df.groupby('Date')['money'].agg(['count','sum']).sort_index()

    return {"prices": drinks_and_price,
            "top_drinks": top_drinks,
            "monthly_drinks": monthly_drinks,
            "monthly_drink_type": monthly_drink_type,
            "hourly_drinks": hourly_drinks,
            "hourly_drinks_per_month": hourly_drinks_per_month,
            "drinks_TOD": drinks_TOD,
            "drinks_TOD_per_month": drinks_TOD_per_month,
            "drink_type_per_TOD": drink_type_per_TOD,
            "weekly_drinks": weekly_drinks,
            "weekday_drink_types": weekday_drink_types,
            "payment_type": payment_type,
            "daily_sales": daily_sales}
