import pandas as pd

# Load the sales data from the CSV file
file_path = 'sales_data.csv'  # Replace with the actual path to the CSV file if different
sales_data = pd.read_csv(file_path)

# Calculate "Total Sales" for each record
sales_data['Total Sales'] = sales_data['Units Sold'] * sales_data['Price Per Unit']

# 1. Total Sales Calculation
total_sales = sales_data['Total Sales'].sum()
print("Total Sales for the entire period:", total_sales)

# 2. Sales by Product
sales_by_product = sales_data.groupby('Product ID')['Total Sales'].sum().reset_index()
print("\nSales by Product:")
print(sales_by_product)

# 3. Daily Sales Report
daily_sales_report = sales_data.groupby('Date')['Total Sales'].sum().reset_index()
print("\nDaily Sales Report:")
print(daily_sales_report)

# 4. Highest Selling Product
highest_selling_product = sales_by_product[sales_by_product['Total Sales'] == sales_by_product['Total Sales'].max()]
print("\nHighest Selling Product:")
print(highest_selling_product)