import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


con = create_connection("app_sq.sqlite3")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_categories_table = """
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  category_name TEXT NOT NULL,
  category_description TEXT
);
"""

execute_query(con, create_categories_table)

create_units_table = """
CREATE TABLE IF NOT EXISTS units(
  id INTEGER NOT NULL PRIMARY KEY DEFAULT 1
);
"""

execute_query(con, create_units_table)

create_positions_table = """
CREATE TABLE IF NOT EXISTS positions(
  id INTEGER NOT NULL PRIMARY KEY DEFAULT 1
);
"""

execute_query(con, create_positions_table)

create_goods_table = """
CREATE TABLE IF NOT EXISTS goods(
  good_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  good_name TEXT NOT NULL, 
  good_unit TEXT NOT NULL, 
  good_cat INTEGER NOT NULL, 
  FOREIGN KEY (good_id) REFERENCES units (id)
  FOREIGN KEY (good_cat) REFERENCES categories (id)
);
"""
execute_query(con, create_goods_table)

create_employees_table = """
CREATE TABLE IF NOT EXISTS employees(
  employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  employee_fio TEXT NOT NULL, 
  employee_position TEXT NOT NULL, 
  FOREIGN KEY (employee_position) REFERENCES positions (id)
);
"""
execute_query(con, create_employees_table)

create_vendors_table = """
CREATE TABLE IF NOT EXISTS vendors(
  vendor_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  vendor_name TEXT NOT NULL, 
  vendor_ownerchipform TEXT NOT NULL, 
  vendor_address TEXT NOT NULL,
  vendor_phone TEXT NOT NULL,
  vendor_email TEXT NOT NULL
);
"""
execute_query(con, create_vendors_table)
