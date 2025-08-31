# Task 2: Define Database Structure
# Think for a minute.
# There is a one-to-many relationship between publishers and magazines.
# Which table has a foreign key? magazine
# Where does the foreign key point? points to publisher
# How about the subscriptions table: What foreign keys does it have? name of magazine

import sqlite3

try:
    # Connect to a new SQLite database
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1") # Task 3: confirms foreign keys are valid

        cursor = conn.cursor() # get a cursor object to run SQL commands
        # create publishers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (     -- creates the table
                publisher_id INTEGER PRIMARY KEY,       -- surrogate key
                name TEXT NOT NULL UNIQUE               -- required + unique
            );
        """)
        # CREATE magazines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (      -- creates the table
                magazine_id INTEGER PRIMARY KEY,        -- surrogate key
                name TEXT NOT NULL UNIQUE,              -- required + unique
                publisher_id INTEGER NOT NULL,          -- points to publishers
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            );
        """)
        # CREATE subscribers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,      -- surrogate key
                name TEXT NOT NULL,                     -- required
                address TEXT NOT NULL,                  -- required
                UNIQUE(name, address)                   -- prevent duplicate person+address
            );
        """)
        # CREATE subscriptions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (  -- creates the table
                subscription_id INTEGER PRIMARY KEY,    -- surrogate key
                subscriber_id INTEGER NOT NULL,         -- foreign key (subscriber)
                magazine_id INTEGER NOT NULL,           -- foreign key (magazine)
                expiration_date TEXT NOT NULL,          -- required
                UNIQUE(subscriber_id, magazine_id),     -- no dupe pairs
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            );
        """)

except sqlite3.Error as e:
    print(f"***** SQLite error is: {e}")

# Task 3: Populate Tables with Data
def add_publisher(conn, name):      # define the function
    cursor = conn.cursor()          # talk to DB
    cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,)) #run SQLite with name filled in
    conn.commit()                   # save the change

def add_magazine(conn, name, publisher_id):      # define the function
    cursor = conn.cursor()          # talk to DB
    cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id,)) #run SQLite with both values
    conn.commit()                   # save the change

def add_subscriber(conn, name, address):      # define the function
    cursor = conn.cursor()          # talk to DB
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address,)) #run SQLite with both values
    conn.commit()                   # save the change

def add_subscriptions(conn, subscriber_id, magazine_id, expiration_date):      # define the function
    cursor = conn.cursor()          # talk to DB
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date,)) #run SQLite with all values
    conn.commit()                   # save the change

with sqlite3.connect("../db/magazines.db") as conn:
    # populate publishers
    add_publisher(conn, "Penguin Books")
    add_publisher(conn, "HarperCollins")
    add_publisher(conn, "Oxford Press")

    # populate magazines
    add_magazine(conn, "National Geographic", 1)    # belongs to Penguin
    add_magazine(conn, "History Today", 2)          # belongs to HarperCollins
    add_magazine(conn, "Data is COOL!", 2)           # belongs to Oxford Press

    # populate subscribers
    add_subscriber(conn, "John Smith", "123 Main Street")
    add_subscriber(conn, "LEERoy Jenkins", "456 Druid Cove")
    add_subscriber(conn, "Milburn Pennybags", "789 Park Place")

    # populate subscriptions
    add_subscriptions(conn, 1, 1, "2025-12-31")     # John -> Science Monthly
    add_subscriptions(conn, 2, 2, "2026-03-14")     # LEERoy -> History Today
    add_subscriptions(conn, 3, 3, "2030-10-31")     # Milburn -> Data is COOL!