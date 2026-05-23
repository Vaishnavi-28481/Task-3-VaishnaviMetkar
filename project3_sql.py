import pandas as pd
import sqlite3

# Load Excel dataset
df = pd.read_csv("Cleaned_Dataset.csv")

# Create SQLite database
conn = sqlite3.connect("sales.db")

# Store dataframe as SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")

query = """
SELECT * FROM sales
"""

result = pd.read_sql(query, conn)

print(result.head())

query = """
SELECT *
FROM sales
WHERE order_status = 'Delivered'
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT product, total_price
FROM sales
ORDER BY total_price DESC
"""

result = pd.read_sql(query, conn)

print(result.head())

query = """
SELECT product,
SUM(total_price) AS total_sales
FROM sales
GROUP BY product
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT payment_method,
COUNT(*) AS total_orders
FROM sales
GROUP BY payment_method
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT product,
AVG(total_price) AS average_sales
FROM sales
GROUP BY product
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT *
FROM sales
WHERE payment_method = 'Credit Card'
AND total_price > 500
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT *
FROM sales
WHERE product LIKE '%Laptop%'
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT product,
SUM(total_price) AS total_sales
FROM sales
GROUP BY product
HAVING total_sales > 10000
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT customer_id,
SUM(total_price) AS customer_spending
FROM sales
GROUP BY customer_id
ORDER BY customer_spending DESC
LIMIT 5
"""

result = pd.read_sql(query, conn)

print(result)

