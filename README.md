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
  1. Cappucino
  2. Hot Chocolate
  3. Cocoa
  4. Latte
<img width="700" height="500" alt="avg_drink_price" src="https://github.com/user-attachments/assets/7836e831-5ed4-445e-a994-e5d3a2e1250e" />

---
### Specific drinks, their annual sale, and the number of drinks bought
The two tables below display the types of coffee and their annual sales and number of drinks bought annually. 

Although less Latte's have been bought in comparison to Americano's with Milk, Latte's still bring in more sales throughout the year.
The previous table displaying beverages and their average prices also show that Latte's are one of the top most paid drink at above CAD$35.00, while Americano's with Milk are just above CAD$30.00

<img width="500" height="400" alt="drink_type_sales" src="https://github.com/user-attachments/assets/8f18bd33-76d1-4127-80f4-36917e21adff" /> <img width="500" height="400" alt="num_drinks_bought" src="https://github.com/user-attachments/assets/73ae2328-b952-4d5b-9741-7788a5d447de" />

---
<a name="Sales_Num_Drink"></a>
### Annual Sales and Number of drinks bought per Month 
The two tables below display the annual sales and the number of drinks bought per month.

We can see that October has the highest sales in the year followed by February. 

The sales graph shown for each month follow the bar graph of the number of drinks bought per month. Showing an increase in sales and number of drinks bought starting in June, peaking in October, declining the months after, and rising again with February having the second highest sales and number of drinks bought in the year.

<img width="500" height="400" alt="annual_sales" src="https://github.com/user-attachments/assets/700b0424-cc6b-4d63-b49b-b907d7338063" />
<img width="500" height="400" alt="num_drinks_per_month" src="https://github.com/user-attachments/assets/7ec4371f-6b5e-4213-a5d6-0fdf25e89625" />

---
### Annual number of drinks bought in the weekday
The table below displays the number of drinks bought in the week throughout the year. 

The weekdays are shown to have a higher number of drinks bought in comparison to the weekends.

<img width="700" height="500" alt="weekly_num_drinks" src="https://github.com/user-attachments/assets/f4cc4f01-ec53-4294-9781-93753d55275f" />

---
### Annual Number of drinks bought Time of Day (TOD) and per hour
The two tables below display peak hours in the year.

Time of Day (TOD) can be broken down into these hours:

- **Morning**: 6 - 11
- **Afternoon**: 12 - 16 (12 pm - 4 pm)
- **Night**: 17 - 22 (5 pm - 9 pm)

It is shown in the TOD graph that Night is the most popular TOD for drinks to be bought, despite 10 am being the busiest hour in the day during store hours. 

Despite Morning and Night having the same number of hours for the TOD (6 hours each), Night hours sell more per hour compared to the morning hours, with 7 am and 8 am showing a significant increase in drinks bought once the store is open.

<img width="500" height="400" alt="num_drink_TOD" src="https://github.com/user-attachments/assets/1a8c4483-8e02-4a8b-b03b-cdde1d94e405" />
<img width="500" height="400" alt="num_drink_per_hour" src="https://github.com/user-attachments/assets/f4224c3f-2449-44fa-828c-13aad5980374" />

---
### Types of drinks sold in the month
The three graphs below display the first two months that were previously shown to have the highest [sales and number of drinks bought](#Sales_Num_Drink) (October, February), and the month with the lowest sales and number of drinks bought (April). 

Each graph displayed will also show which are the top 3 most bought drinks that month.

### October
Most popular drinks:
1. Lattes
2. Americano with Milk
3. Hot Chocolate
<img width="700" height="400" alt="October" src="https://github.com/user-attachments/assets/b85651b2-ec77-4f61-8969-22049f3d516d" />

### February
Most popular drinks:
1. Americano
2. Americano with Milk
3. Cocoa
<img width="700" height="400" alt="February" src="https://github.com/user-attachments/assets/a4646c9b-34dd-4a6a-9825-f3dc63326653" />

### April
Most popular drinks:
1. Americano with Milk
2. Cappucino
3. Americano
<img width="700" height="400" alt="April" src="https://github.com/user-attachments/assets/5b22a138-a75b-47d1-8e24-3a839d8b7bac" />

---
### Daily Sales
The three graphs below display the first two months that were previously shown to have the highest [sales and number of drinks bought](#Sales_Num_Drink) (October, February), the month with the lowest sales and number of drinks bought (April), and the month of May.

Each graph shows the sales of each day in that month.

The month of May shows missing dates (2024-05-01, 2024-05-04, 2024-05-05). Reasons for no record of a transaction could be for a number of reasons (no transactions made that day, store closed, broken equipment, etc.), but was added to showcase missing dates.

### October
<img width="900" height="400" alt="October" src="https://github.com/user-attachments/assets/19691af6-93b8-465d-91c7-bf17e149556a" />

### February
<img width="900" height="400" alt="February" src="https://github.com/user-attachments/assets/d406997a-cd8a-4bd7-b69e-2d82afa88222" />

### April
<img width="900" height="400" alt="April" src="https://github.com/user-attachments/assets/a29b540e-a1af-453b-8abd-d66729282728" />

### May
<img width="900" height="400" alt="May" src="https://github.com/user-attachments/assets/67d06f47-f16c-49fd-b077-8a99eec7951e" />
