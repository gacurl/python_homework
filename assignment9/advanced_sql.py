import sqlite3

DB_PATH = "../db/lesson.db"

def test_connection():
     # AM I connected????
    try:
        conn = sqlite3.connect(DB_PATH)
        print("Connected to database:", DB_PATH)
        # quick sanity check — list the tables
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        print("Tables found:", tables)
        conn.close()
    except Exception as e:
        print("ALERT: TRY AGAIN - Connection failed:", e)

# --- Task 1: Complex JOINs with Aggregation ---
def task1(conn):
    print("—---- Task 1: Complex JOINs with Aggregation —----")
    sql = """
    SELECT o.order_id,
            SUM(li.quantity * price) AS total_price
    FROM orders AS o
    JOIN line_items AS li on li.order_id = o.order_id
    JOIN products AS p on p.product_id = li.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row[0], f"{row[1]:.2f}")



# # --- Task 2: Understanding Subqueries (avg per customer) ---
# def task2(conn: sqlite3.Connection):
#     """
#     Problem: average order price per customer using a subquery.
#     Subquery returns (customer_id_b, total_price) per order.
#     Main query LEFT JOIN customers c ON c.customer_id = sub.customer_id_b
#     GROUP BY customer_id -> AVG(total_price)
#     Return: customer_name, average_total_price
#     Tip: alias in subquery to avoid name collisions.
#     """
#     sql = """
#     -- TODO: write the WITH/inline subquery you validated
#     -- WITH order_totals AS (
#     --   SELECT o.customer_id AS customer_id_b,
#     --          SUM(p.price * li.quantity) AS total_price
#     --   FROM ...
#     --   GROUP BY o.order_id
#     -- )
#     -- SELECT c.name AS customer_name,
#     --        AVG(order_totals.total_price) AS average_total_price
#     -- FROM customers c
#     -- LEFT JOIN order_totals ON c.customer_id = order_totals.customer_id_b
#     -- GROUP BY c.customer_id
#     -- ORDER BY customer_name;
#     """
#     cur = conn.execute(sql)
#     rows = cur.fetchall()
#     print("— Task 2 —")
#     print_rows(rows, headers=["customer_name", "average_total_price"])

# # --- Task 3: Insert Transaction Based on Data ---
# def task3(conn: sqlite3.Connection):
#     """
#     Problem: create an order for 'Perez and Sons' by 'Miranda Harris'.
#     Steps:
#       1) SELECT customer_id for 'Perez and Sons'
#       2) SELECT employee_id for Miranda Harris
#       3) SELECT product_id of 5 least expensive products
#       4) BEGIN transaction
#          - INSERT INTO orders (...) VALUES (...) RETURNING order_id
#            (or fallback to lastrowid)
#          - For each product_id → INSERT into line_items(order_id, product_id, quantity=10)
#          - COMMIT
#       5) SELECT JOIN to verify: list (line_item_id, quantity, product_name) for the new order

#     Pseudocode:
#       cust_id = conn.execute("SELECT ... WHERE name=?", ("Perez and Sons",)).fetchone()[0]
#       emp_id  = conn.execute("SELECT ... WHERE first_name=? AND last_name=?", ("Miranda","Harris")).fetchone()[0]
#       pids    = [r["product_id"] for r in conn.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")]
#       conn.execute("BEGIN")
#       try:
#           row = conn.execute("INSERT ... RETURNING order_id").fetchone()  # or do insert then lastrowid
#           order_id = row["order_id"] or cur.lastrowid
#           for pid in pids:
#               conn.execute("INSERT INTO line_items(order_id, product_id, quantity) VALUES (?,?,?)", (order_id, pid, 10))
#           conn.commit()
#       except:
#           conn.rollback(); raise

#       # verify with a SELECT JOIN and print_rows
#     """
#     # TODO: implement per your validated SQL from sqlcommand.py
#     # Keep your real SQL statements below once they work.
#     pass

# # --- Task 4: Aggregation with HAVING ---
# def task4(conn: sqlite3.Connection):
#     """
#     Problem: employees with > 5 orders
#     Steps:
#       - JOIN employees e -> orders o on employee_id
#       - GROUP BY e.employee_id
#       - SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
#       - HAVING COUNT(o.order_id) > 5
#       - ORDER BY order_count DESC, last_name, first_name
#     """
#     sql = """
#     -- TODO: write the final SQL you proved in sqlcommand.py here
#     """
#     cur = conn.execute(sql)
#     rows = cur.fetchall()
#     print("— Task 4 —")
#     print_rows(rows, headers=["employee_id","first_name","last_name","order_count"])

def main():
    test_connection()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = 1")
    task1(conn)
#         # task2(conn)
#         # task3(conn)
#         # task4(conn)
#         pass

if __name__ == "__main__":
    main()
