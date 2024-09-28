# Calculate the total revenue generated for each month. Your output should display the year-month (e.g., 2023-07) and the corresponding total_revenue.

import pandas as pd

orders_df = pd.read_csv('orders.csv')
orders_df = orders_df[orders_df['customer_id'] != 'INVALID_ID']
orders_df['order_date'] = orders_df['order_date'].astype(str)

date_pattern = r'^\d{4}-\d{2}-\d{2}$'
valid_dates = orders_df['order_date'].str.match(date_pattern)
orders_df = orders_df[valid_dates]
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'], format='%Y-%m-%d', errors='coerce')
orders_df = orders_df.dropna(subset=['order_date'])

orders_df['revenue'] = orders_df['quantity'] * orders_df['price_per_unit']
orders_df['year_month'] = orders_df['order_date'].dt.to_period('M')

monthly_revenue = orders_df.groupby('year_month')['revenue'].sum().reset_index()
monthly_revenue['year_month'] = monthly_revenue['year_month'].astype(str)

print("\nTotal Revenue by Month:")
print(monthly_revenue)
