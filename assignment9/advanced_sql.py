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
    print("\n—---- Task 1: Complex JOINs with Aggregation —----")
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



# --- Task 2: Understanding Subqueries (avg per customer) ---
def task2(conn):
    print("\n—------- Task 2: Understanding Subqueries —-------")
    # goal: for each customer, compute the average order total 
    # 1. What is the unit of the final result? Customer
        # tells me what to GROUP BY
    # 2. What math do I need (aggregate)? AVG of order totals
        # tells me what goes inside the SELECT
    # 3. Which tables have the columns I need? orders, line_items, products (build totals), customers (get names)
        # this is where I make the JOINs
    # 4. Do I need two layers of grouping? YES! SUM per order and then to AVG / customer
        # Am I stacking aggregates? as an example "give me an average of totals" or "give me the max of counts"
        # if yes, I need an inner (the subquery) for the first grouping and an outer for the second.
    # Which columns do I need?
        # o.order_id, o.customer_id
        # li.order_id, li.product_id, li.quantity
        # p.product_id, p.price
        # c.customer_id, c.name
    sql = """
    SELECT
        c.customer_name AS customer_name,
        AVG(t.total_price) AS average_total_price
    FROM customers AS c
    LEFT JOIN (
        SELECT
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM orders AS o
        JOIN line_items AS li ON li.order_id = o.order_id
        JOIN products   AS p  ON p.product_id = li.product_id
        GROUP BY o.order_id
    ) AS t
        ON c.customer_id = t.customer_id_b
        GROUP BY c.customer_id
        ORDER BY customer_name
        LIMIT 10;
    """
    cur = conn.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        avg_val = row[1]
        print(row[0], "0.00" if avg_val is None else f"{avg_val:.2f}")

# # --- Task 3: Insert Transaction Based on Data ---


def main():
    test_connection()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = 1")
    task1(conn)
    task2(conn)
#         # task3(conn)
#         # task4(conn)
#         pass

if __name__ == "__main__":
    main()
