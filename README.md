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
From the table below we can see the average price people pay for each beverage type, and which drinks are over CAD$35.00 (As prices are in local currency, CAD is used here). 

The top 4 most expensive drinks on average:
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

The weekdays are shown to have a higher number of drinks bought in comparison to the weekends. Tuesdays and Mondays are the highest respectively as they indicate the start of the working week (Tuesday's being higher as 'Work from Home' days are either Monday or Friday).

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

Each graph shows the sales of each day in that month, with a circle marker indicating the sale made that day. A day with no circle marker indicates no sales made that day.

The month of May shows missing dates (2024-05-01, 2024-05-04, 2024-05-05). Reasons for no record of a transaction could be for a number of reasons (no transactions made that day, store closed, broken equipment, etc.), but was added to showcase missing dates.

### October
<img width="900" height="400" alt="October" src="https://github.com/user-attachments/assets/19691af6-93b8-465d-91c7-bf17e149556a" />

### February
<img width="900" height="400" alt="February" src="https://github.com/user-attachments/assets/d406997a-cd8a-4bd7-b69e-2d82afa88222" />

### April
<img width="900" height="400" alt="April" src="https://github.com/user-attachments/assets/a29b540e-a1af-453b-8abd-d66729282728" />

### May
<img width="900" height="400" alt="May" src="https://github.com/user-attachments/assets/67d06f47-f16c-49fd-b077-8a99eec7951e" />

## Improvements and Solutions

Improvement of sales would only apply for beverages and would not include food or company merchandise.

### 1. Increasing sales in the Spring and Summer Seasons
The graphs below are from [Annual Sales and Number of drinks bought per Month](#Sales_Num_Drink). Starting from March to August are the Spring and Summer seasons. From the graphs below, those months have low to average sales and the number of drinks bought in comparison to the colder seasons. A way to increase sales during those months would be to include the following options:

1. Seasonal Summer Drinks (fruit, iced teas, iced coffee)
2. Seasonal/Monthly/Weekly Spring and Summer promotions highlighting seasonal fruits or teas popular within those seasons (BOGO, Sale prices)

<img width="500" height="400" alt="annual_sales" src="https://github.com/user-attachments/assets/700b0424-cc6b-4d63-b49b-b907d7338063" />
<img width="500" height="400" alt="num_drinks_per_month" src="https://github.com/user-attachments/assets/7ec4371f-6b5e-4213-a5d6-0fdf25e89625" />

### 2. Increasing sales in November and December
As per from the previous graph of the Annual Sales and Number of drinks bought per Month, November and December display a decrease in sales after the month of October. October is known to be the most popular Fall month in the year, with its popularity in pumpkin spice seasoned beverages.

A way to increase sales for the month of November and December would be to have seasonal promotions during the Christmas and New Years holiday. Similar to the improvements mentioned from the Spring and Summer months, the following improvements for November and December can include:
1. Christmas-themed Drinks (white and peppermint hot chocolate, peppermint tea, gingerbread seasoning)
2. Christmas and New Year's promotions highlighting seasonal flavours and seasonings (BOGO, Sale prices)

### 3. Introducing a points/reward system
A new points/reward system where customers can receive a free beverage of any size, type, and with add-ons. These free beverages can be claimed either by buying 5 beverages, or by gaining points. 

These rewards would be claimed by claiming a physical card from a store in-person, or by creating an account under the company app (customers may be able to link their physical card when making an account under the app). 

## Conclusion
### Top 4 most expensive drinks on average: 
  1. Cappuccino
  2. Hot Chocolate
  3. Cocoa
  4. Latte

### Top 4 most popular drinks bought (sales vs number of drinks bought):
| **Sales**            | **Number of drinks bought** |
|----------------------|------------------|
| Latte                | Americano with Milk |
| Americano with Milk  | Latte |
| Cappucino            | Americano |
| Americano            | Cappucino|

### Weekday sales
Tuesday has the highest activity followed by Monday as they indicate the start of the working week. Tuesdays being higher than Monday can indicate 'Work from Home' days are still in effect and are either Mondays or Fridays.

### Drinks bought during peak hours or TOD
Peak hours are shown to be at 10 am, with a significant increase in numbers starting from 7 am - 8 am. 

Although indicated in the TOD graph, Night is shown to have higher number of drinks bought in comparison to the Morning despite having the peak hour (10 am) within its TOD, Night has higher TOD activity as there are more customers buying within the 6 hours compared to the Morning 6 hours, where the first two hours of store operations are less than 100 total in the year.

### Types of Drinks bought in the month
October and February are the months with the highest sales and number of drinks bought. 

Latte's being the most popular beverage in October can indicate the new Fall season and weather changes coming and hot beverages being more popular during the colder seasons. 

Americano being the most popular beverage in February followed by Americano's with Milk.

April is the month with the lowest sales and number of drinks bought in the year. Americano's with Milk is the most popular beverage in the month, but shows that only 37 Americano's with Milk have been bought that month, while October and February are shown to sell more than 115 of their most popular beverage that month.

### Daily Sales
Daily sales show each day of the month and the sales made that month. Each graph shows a circle marker indicating the sale made that day. A day with no circle marker indicates no sales made that day.

The month of May has shown days missing as there is no circle marker indicating its sales day and its date missing from the x axis of the table.

The missing dates can be due to multiple reasons: 
1. no transactions made that day
2. store closed
3. broken equipment

There maybe other reasons for missing dates that have not been mentioned before.

### Improvements 
Ways to increase beverage sales include:
1. Seasonal beverages (colder beverages in Spring and Summer, and festive drinks in November and December)
2. Seasonal/Monthly/Weekly Promotions
3. Points/Reward system

## Additional Notes
The dataset used does not disclose where this information was collected. It does not indicate the location of where the data is collected and anything mentioned in the findings and report are solely based on local information for those using the dataset.
