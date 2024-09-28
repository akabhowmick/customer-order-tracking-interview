import pandas as pd

# Calculate the total expenditure for each customer across all their orders. Output the result as a list of dictionaries or a DataFrame containing customer_id and total_spent.

# Read data
orders_df = pd.read_csv("orders.csv")

# Calculate total expenditure for each order
orders_df["total_expenditure"] = orders_df["quantity"] * orders_df["price_per_unit"]

# Group by customer_id and calculate total expenditure per customer
customer_expenditure = (
    orders_df.groupby("customer_id")["total_expenditure"].sum().reset_index()
)
customer_expenditure.rename(columns={"total_expenditure": "total_spent"}, inplace=True)

# Output the result of all customers
print(customer_expenditure)

# Sort customers by total_spent in descending order and get the top 5 customers
top_customers = customer_expenditure.sort_values(by='total_spent', ascending=False).head(5)
print(top_customers)
