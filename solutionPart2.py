# Part 2: Order Frequency and Product Popularity
# 1. Determine the customer who placed the highest number of orders. If there is a tie, list all tied customers.


import pandas as pd

# Load the CSV file into a DataFrame
orders_df = pd.read_csv('orders.csv')

# Clean the data
orders_df = orders_df[orders_df['customer_id'] != 'INVALID_ID']

# Group by customer_id and count the number of orders
customer_order_count = orders_df.groupby('customer_id')['order_id'].count().reset_index()
customer_order_count.rename(columns={'order_id': 'order_count'}, inplace=True)

# Find the maximum number of orders
if not customer_order_count.empty:
    max_orders = customer_order_count['order_count'].max()
    top_customers = customer_order_count[customer_order_count['order_count'] == max_orders]

    print("\nCustomers who placed the highest number of orders:")
    print(top_customers)
else:
    print("No valid customer data available.")





# 2. Calculate the most popular product (by number of units sold). Output the product_id and the total units sold.
# Group by product_id and sum the units sold
product_sales = orders_df.groupby('product_id')['quantity'].sum().reset_index()
product_sales.rename(columns={'quantity': 'total_units_sold'}, inplace=True)

# Find the product with the maximum units sold
if not product_sales.empty:
    most_popular_product = product_sales[product_sales['total_units_sold'] == product_sales['total_units_sold'].max()]

    print("\nMost popular product(s) by units sold:")
    print(most_popular_product)
else:
    print("No valid product data available.")