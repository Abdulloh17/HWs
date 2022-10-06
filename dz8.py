import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)

    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)



create_productss_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

def create_products(conn, product):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_products_quantity_id(conn, update_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, update_quantity)
        conn.commit()
    except Error:
        print(Error)


def update_products_price_id(conn, new_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, new_price)
        conn.commit()
    except Error:
        print(Error)


def delete_products(conn, delete_product):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (delete_product,))
        conn.commit()
    except Error:
        print(Error)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error:
        print(Error)


connection = create_connection("hw.db")
if connection is not None:
    print("Connected!")
    # create_table(connection, create_productss_table)
    create_products(connection, ('Sugar', 160.00, 50))
    create_products(connection, ('Coke', 95.00, 105))
    create_products(connection, ('Choco-Pie', 75.00, 205))
    create_products(connection, ('Ice-Cream', 45.00, 95))
    create_products(connection, ('Note-Book', 50.00, 400))
    create_products(connection, ('Energy-drinks', 78.00, 355))
    create_products(connection, ('Snacks', 95.00, 85))
    create_products(connection, ('Milk', 50.00, 20))
    create_products(connection, ('Dunuts', 35.00, 8))
    create_products(connection, ('Soap', 50.00, 74))
    create_products(connection, ('Wet-wipes', 15.00, 200))
    create_products(connection, ('Socks', 75.00, 15))
    create_products(connection, ('Cigaretts', 101.00, 500))
    create_products(connection, ('Oil', 150.00, 50))
    create_products(connection, ('Tapes', 68.00, 458))
