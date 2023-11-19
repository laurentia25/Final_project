"""
Setarea functionalitatilor pentru crearea bazei de date si a tabelelor
"""
import sqlite3
DB_PATH = "LebiZoux.db"


# Stabilirea conexiunii cu baza de date
def get_db_connection(db_path=DB_PATH):
    connection = sqlite3.connect(db_path)
    return connection


def create_tables(connection):
    create_users_table(connection)
    create_products_table(connection)
    create_orders_table(connection)
    create_order_items_table(connection)


# Crearea bazei de date si a tabelelor
def create_database(db_path=DB_PATH):
    # creare baza de date
    connection = sqlite3.connect(db_path)
    # creare tabele
    create_tables(connection)


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users(
        id TEXT NOT NULL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL        
        );
        """
    )
    connection.commit()


def create_products_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        available_quantity INTEGER NOT NULL DEFAULT 0,
        image TEXT        
        );
        """
    )
    connection.commit()


def create_orders_table(connection):
    pass


def create_order_items_table(connection):
    pass
