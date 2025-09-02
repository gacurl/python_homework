# Task 5: Read Data into a DataFrame
import os
import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    df = pd.read_sql_query("""
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_id,
            products.product_name,
            products.price
        FROM line_items JOIN products
            ON line_items.product_id = products.product_id
    """, conn,)

print(df.head(),"\n")       # step 3 - print first 5 lines

df['total'] = df['quantity'] * df['price']      # step 4 add total column
print("----- ----- ----- ----- ----- ----- with total ----- ----- ----- ----- ----- ----- \n")      
print(df.head(),"\n")

# step 5 group by product_id

summary = (
    df.groupby("product_id")
        .agg(
            line_item_count=("line_item_id", "count"),  # how many times the product was ordered (count)
            total_revenue=("total", "sum"),             # total dollars spent
            product_name=("product_name", "first")      # that product's name
        )
    .reset_index()
)

print("----- ----- ----- ----- by product_id with count ----- ----- ----- ----- ----- ----- \n") 
print(summary.head(),"\n")


print("----- ----- ----- ----- sorted by product_name ----- ----- ----- ----- ----- ----- \n")
summary = summary.sort_values("product_name")       # could tack this on above, but want to break out step
print(summary.head(),"\n")

# write the file
summary.to_csv("order_summary", index=False)

print("order_summary located at:\t")
print(os.path.abspath("order_summary.csv"))
