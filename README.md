# Coffee Sales Dataset

## Project Overview
This project explores a coffee shop dataset that covers transaction records, beverage sales, payment type, and date/time of purchase. This project uses **Python** and the **Visual Studios IDE**. The goal is to  demonstrate data analysis using **Pandas**, and visualization using **Matplotlib** libraries.

## Dataset and Project Details

The dataset used is specifically made for data visualization, dashboard building, and business analytics projects in tools like Power BI, Tableau, and Python visualization libraries (Coffee Sales Dataset, Kaggle). 

- **Dataset Source**: Kaggle [Coffee Sales Dataset](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset).
- **Langauge**: Python
- **Libraries**: Pandas and Matplotlib

## Data Dictionary
Copied via [Coffee Sales Dataset (Kaggle)](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset).

| **Variable** | **Explanation** |
|--------------|------------------|
| `hour_of_day`| Hour of purchase (0–23) |
| `cash_type`  | Mode of payment (cash / card) |
| `money`      | Transaction amount (in local currency) |
| `coffee_name`| Type of coffee purchased (e.g., Latte, Americano, Hot Chocolate) |
| `Time_of_Day`| Categorized time of purchase (Morning, Afternoon, Night) |
| `Weekday`    | Day of the week (e.g., Mon, Tue, …) |
| `Month_name` | Month of purchase (e.g., Jan, Feb, Mar) |
| `Weekdaysort`| Numeric representation for weekday ordering (1 = Mon, 7 = Sun) |
| `Monthsort`  | Numeric representation for month ordering (1 = Jan, 12 = Dec) |
| `Date`       | Date of transaction (YYYY-MM-DD) |
| `Time`       | Exact time of transaction (HH:MM:SS) |

## Exploratory Data Analysis (EDA)
### Average Drink Prices
From the table below we can see the average price people pay, and which drinks are over CAD$35.00 (As prices are in local currency, CAD is used here): 
  1. Cappacino
  2. Hot Chocolate
  3. Cocoa
  4. Latte
<img width="800" height="600" alt="avg_drink_price" src="https://github.com/user-attachments/assets/7836e831-5ed4-445e-a994-e5d3a2e1250e" />

### Specific drinks, their annual sale, and the number of drinks bought
The two tables below display the types of coffee and their annual sales and number of drinks bought annually. 

Although less Latte's have been bought in comparison to Americano's with Milk, Latte's still bring in more sales throughout the year.
The previous table displaying beverages and their average prices also show that Latte's are one of the top most paid drink at above CAD$35.00, while Americano's with Milk are just above CAD$30.00

<img width="500" height="400" alt="drink_type_sales" src="https://github.com/user-attachments/assets/8f18bd33-76d1-4127-80f4-36917e21adff" /> <img width="500" height="400" alt="num_drinks_bought" src="https://github.com/user-attachments/assets/73ae2328-b952-4d5b-9741-7788a5d447de" />
