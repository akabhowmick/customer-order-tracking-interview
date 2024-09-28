import pandas as pd

# Calculate the total expenditure for each customer across all their orders. Output the result as a list of dictionaries or a DataFrame containing customer_id and total_spent.

# Read data
orders_df = pd.read_csv("orders.csv")

# Calculate total expenditure for each customer and add a new column "total_spent" to the DataFrame
orders_df["total_expenditure"] = orders_df["quantity"] * orders_df["price_per_unit"]

# Convert DataFrame to list of dictionaries
customer_expenditure = (
    orders_df.groupby("customer_id")["total_expenditure"].sum().reset_index()
)
customer_expenditure.rename(columns={"total_expenditure": "total_spent"}, inplace=True)

# Output the result of all customers
print(customer_expenditure)
