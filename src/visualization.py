import matplotlib.pyplot as plt
import matplotlib.ticker as tck

from src.analysis import analysis

def visual (df):
    stats = analysis(df)

    # Average price of drinks
    plt.figure(figsize=(8,6))
    plt.title("Average price of Beverages")
    stats["prices"].plot(kind="barh", color="lightskyblue")
    plt.xlabel("Coffee Name")
    plt.ylabel("Average Price")
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Type of drinks bought anually 
    plt.figure(figsize=(8, 6))
    stats["top_drinks"]['count'].plot(kind="barh", color="lightskyblue")
    plt.title("Number of Drinks bought")
    plt.xlabel("Drinks bought")
    plt.ylabel("Coffee Type")
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # # Sales of type of drinks bought anually 
    plt.figure(figsize=(8, 6))
    stats["top_drinks"]['sum'].plot(kind='barh', color='lightskyblue')
    plt.title("Revenue of drinks bought")
    plt.xlabel("Revenue")
    plt.ylabel("Coffee Type")
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # How many drinks are bought each month
    plt.figure(figsize=(8, 6))
    stats["monthly_drinks"]['count'].plot(kind="bar", color='lightskyblue')
    plt.title("Number of Drinks bought per month")
    plt.xlabel("Month")
    plt.ylabel("Number of drinks bought")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Annual revenue
    plt.figure(figsize=(10, 8))
    month = stats["monthly_drinks"]['sum']
    month.index = month.index.droplevel(0)
    month.plot(kind='line')
    plt.title("Annual Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Types of drinks sold each month
    # Creating a forloop to loop through each month and create separate charts
    for (fiscal_month, month_name), data in stats['monthly_drink_type'].groupby(level=[0,1], sort =False):
        plt.figure(figsize=(8,5))
        data.index = data.index.droplevel([0,1]) #Dropping the fiscal order and month name to create a cleaner graph
        data.plot(kind='bar', color='lightskyblue')
        
        plt.title(f"Drinks sold in {month_name}")
        plt.xlabel("Coffee type")
        plt.ylabel("Number of drinks sold")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Average drinks sold per hour annually
    plt.figure(figsize=(8, 6))
    stats["hourly_drinks"]['count'].plot(kind="barh", color="lightskyblue")
    plt.title("Number of Drinks bought per hour")
    plt.xlabel("Drinks bought")
    plt.ylabel("Hour")
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Number of drinks sold Time of Day annually
    plt.figure(figsize=(8, 6))
    stats["drinks_TOD"]['count'].plot(kind="bar", color='lightskyblue')
    plt.title("Number of Drinks bought per hour")
    plt.xlabel("Time of day")
    plt.ylabel("Drinks bought")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Payment types
    plt.figure(figsize=(8, 6))
    stats["payment_type"].plot(kind="pie")
    plt.title("Cash versus Card")
    plt.tight_layout()
    plt.show()

    # Monthly sales
    # Creating a forloop to loop through each month and create separate charts
    for (fiscal_month, month_name), data in stats['daily_sales'].groupby(level=[0,1], sort=False):
        plt.figure(figsize=(10,5))
        data = data.reset_index(level=[0,1]) # this will reset index to get the Date as x-axis
        
        plt.plot(data.index, data['money'], marker='o')
        plt.title(f"Daily Revenue for {month_name}")
        plt.xlabel("Date")
        plt.ylabel("Revenue")
        plt.xticks(data.index[::1], rotation=90) 
        plt.gca().yaxis.set_major_locator(tck.MultipleLocator(50))
        plt.grid(True)
        plt.tight_layout()
        plt.show()