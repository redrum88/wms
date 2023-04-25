# Create class for data insert in database tables. We use db_config.py to connect to database.

import sys
import os
import time
import datetime


# Add path to db directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import psycopg2
import psycopg2.extras
from db_config import Database

HOST = "localhost"
DATABASE = "wms"
USER = "postgres"
PASSWORD = "Naujas293"
log = open("log.txt", "a")

class Insert:
    '''Class for inserting data into database tables'''

    def __init__(self, host=HOST, database=DATABASE, user=USER, password=PASSWORD):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
        
    def category(self, name, description):
        self.cursor.execute("INSERT INTO Categories (name, description) VALUES (%s, %s)", (name, description))
        self.connection.commit()
        print(f"Category with name {name} added to database")
        log.write(f"{datetime.datetime.now()} Category with name {name} added to database\n")

    def usergroup(self, name, access_level):
        self.cursor.execute("INSERT INTO UserGroups (name, access_level) VALUES (%s, %s)", (name, access_level))
        self.connection.commit()
        print(f"Usergroup with name {name} and access level {access_level} added to database")
        log.write(f"{datetime.datetime.now()} Usergroup with name {name} and access level {access_level} added to database\n")

    def client(self, firstname, lastname, company, email, phone, address, post_code, note):
        self.cursor.execute("INSERT INTO Clients (firstname, lastname, company, email, phone, address, post_code, note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, company, email, phone, address, post_code, note))
        self.connection.commit()
        print(f"Client with name {firstname} {lastname} added to database")
        log.write(f"{datetime.datetime.now()} Client with name {firstname} {lastname} added to database\n")

    def supplier(self, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("INSERT INTO Suppliers (company, contact_name, email, phone, address, post_code, note) VALUES (%s, %s, %s, %s, %s, %s, %s)", (company, contact_name, email, phone, address, post_code, note))
        self.connection.commit()
        print(f"Supplier with name {company} added to database")
        log.write(f"{datetime.datetime.now()} Supplier with name {company} added to database\n")

    def user(self, username, password, usergroup_id):
        self.cursor.execute("INSERT INTO Users (username, password, usergroup_id) VALUES (%s, %s, %s)", (username, password, usergroup_id))
        self.connection.commit()
        print(f"User with name {username} added to database")
        log.write(f"{datetime.datetime.now()} User with name {username} added to database\n")

    def empoyee(self, firstname, lastname, job_title, phone, address, employee_id):
        self.cursor.execute("INSERT INTO Employers (firstname, lastname, job_title, phone, address, employee_id) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, lastname, job_title, phone, address, employee_id))
        self.connection.commit()
        print(f"Employee with name {firstname} {lastname} added to database")
        log.write(f"{datetime.datetime.now()} Employee with name {firstname} {lastname} added to database\n")

    def product(self, name, description, category_id, quantity, price, supplier_id, note):
        self.cursor.execute("INSERT INTO Products (name, description, category_id, quantity, price, supplier_id, note) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, description, category_id, quantity, price, supplier_id, note))
        self.connection.commit()
        print(f"Product with name {name} added to database")
        log.write(f"{datetime.datetime.now()} Product with name {name} added to database\n")

    def sale(self, product_id, quantity, price, sale_date):
        self.cursor.execute("INSERT INTO Sales (product_id, quantity, price, sale_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, price, sale_date))
        self.connection.commit()
        print(f"Sale with product id {product_id} added to database")
        log.write(f"{datetime.datetime.now()} Sale with product id {product_id} added to database\n")

    def purchase(self, product_id, quantity, price, purchase_date):
        self.cursor.execute("INSERT INTO Purchases (product_id, quantity, price, purchase_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, price, purchase_date))
        self.connection.commit()
        print(f"Purchase with product id {product_id} added to database")
        log.write(f"{datetime.datetime.now()} Purchase with product id {product_id} added to database\n")

    def order(self, product_id, quantity, order_date, delivery_date):
        self.cursor.execute("INSERT INTO Orders (product_id, quantity, order_date, delivery_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, order_date, delivery_date))
        self.connection.commit()
        print(f"Order with product id {product_id} added to database")
        log.write(f"{datetime.datetime.now()} Order with product id {product_id} added to database\n")

    def transaction(self, product_id, quantity, transaction_date, transaction_type):
        self.cursor.execute("INSERT INTO Transactions (product_id, quantity, transaction_date, transaction_type) VALUES (%s, %s, %s, %s)", (product_id, quantity, transaction_date, transaction_type))
        self.connection.commit()
        print(f"Transaction with product id {product_id} added to database")
        log.write(f"{datetime.datetime.now()} Transaction with product id {product_id} added to database\n")

    def invoice(self, client_id, total_amount, invoice_date):
        self.cursor.execute("INSERT INTO Invoices (client_id, total_amount, invoice_date) VALUES (%s, %s, %s)", (client_id, total_amount, invoice_date))
        self.connection.commit()
        print(f"Invoice with client id {client_id} added to database")
        log.write(f"{datetime.datetime.now()} Invoice with client id {client_id} added to database\n")

    def payment(self, invoice_id, amount, payment_date):
        self.cursor.execute("INSERT INTO Payments (invoice_id, amount, payment_date) VALUES (%s, %s, %s)", (invoice_id, amount, payment_date))
        self.connection.commit()
        print(f"Payment with invoice id {invoice_id} added to database")
        log.write(f"{datetime.datetime.now()} Payment with invoice id {invoice_id} added to database\n")

class Update:
    '''Class for updating data in database'''

    def __init__(self, host=HOST, database=DATABASE, user=USER, password=PASSWORD):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
        
    def category(self, id, name, description):
        self.cursor.execute("UPDATE Categories SET name = %s, description = %s WHERE id = %s", (name, description, id))
        self.connection.commit()
        print(f"Category with id {id} name {name} updated")
        log.write(f"{datetime.datetime.now()} Category with id {id} name {name} updated\n")

    def client(self, id, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("UPDATE Clients SET company = %s, contact_name = %s, email = %s, phone = %s, address = %s, post_code = %s, note = %s WHERE id = %s", (company, contact_name, email, phone, address, post_code, note, id))
        self.connection.commit()
        print(f"Client with id {id} company {company} updated")
        log.write(f"{datetime.datetime.now()} Client with id {id} company {company} updated\n")

    def supplier(self, id, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("UPDATE Suppliers SET company = %s, contact_name = %s, email = %s, phone = %s, address = %s, post_code = %s, note = %s WHERE id = %s", (company, contact_name, email, phone, address, post_code, note, id))
        self.connection.commit()
        print(f"Supplier with id {id} company {company} updated")
        log.write(f"{datetime.datetime.now()} Supplier with id {id} company {company} updated\n")

    def user(self, id, username, password, usergroup_id):
        self.cursor.execute("UPDATE Users SET username = %s, password = %s, usergroup_id = %s WHERE id = %s", (username, password, usergroup_id, id))
        self.connection.commit()
        print(f"User with id {id} username {username} updated")
        log.write(f"{datetime.datetime.now()} User with id {id} username {username} updated\n")

    def employee(self, id, firstname, lastname, job_title, phone, address, employee_id):
        self.cursor.execute("UPDATE Employers SET firstname = %s, lastname = %s, job_title = %s, phone = %s, address = %s, employee_id = %s WHERE id = %s", (firstname, lastname, job_title, phone, address, employee_id, id))
        self.connection.commit()
        print(f"Employee with id {id} firstname {firstname} updated")
        log.write(f"{datetime.datetime.now()} Employee with id {id} firstname {firstname} updated\n")

    def product(self, id, name, description, category_id, quantity, price, supplier_id, note):
        self.cursor.execute("UPDATE Products SET name = %s, description = %s, category_id = %s, quantity = %s, price = %s, supplier_id = %s, note = %s WHERE id = %s", (name, description, category_id, quantity, price, supplier_id, note, id))
        self.connection.commit()
        print(f"Product with id {id} name {name} updated")
        log.write(f"{datetime.datetime.now()} Product with id {id} name {name} updated\n")

    def sale(self, id, product_id, quantity, price, sale_date):
        self.cursor.execute("UPDATE Sales SET product_id = %s, quantity = %s, price = %s, sale_date = %s WHERE id = %s", (product_id, quantity, price, sale_date, id))
        self.connection.commit()
        print(f"Sale with id {id} product_id {product_id} updated")
        log.write(f"{datetime.datetime.now()} Sale with id {id} product_id {product_id} updated\n")

    def purchase(self, id, product_id, quantity, price, purchase_date):
        self.cursor.execute("UPDATE Purchases SET product_id = %s, quantity = %s, price = %s, purchase_date = %s WHERE id = %s", (product_id, quantity, price, purchase_date, id))
        self.connection.commit()
        print(f"Purchase with id {id} product_id {product_id} updated")
        log.write(f"{datetime.datetime.now()} Purchase with id {id} product_id {product_id} updated\n")

    def order(self, id, product_id, quantity, order_date, delivery_date):
        self.cursor.execute("UPDATE Orders SET product_id = %s, quantity = %s, order_date = %s, delivery_date = %s WHERE id = %s", (product_id, quantity, order_date, delivery_date, id))
        self.connection.commit()
        print(f"Order with id {id} product_id {product_id} updated")
        log.write(f"{datetime.datetime.now()} Order with id {id} product_id {product_id} updated\n")

    def transaction(self, id, product_id, quantity, transaction_date, transaction_type):
        self.cursor.execute("UPDATE Transactions SET product_id = %s, quantity = %s, transaction_date = %s, transaction_type = %s WHERE id = %s", (product_id, quantity, transaction_date, transaction_type, id))
        self.connection.commit()
        print(f"Transaction with id {id} product_id {product_id} updated")
        log.write(f"{datetime.datetime.now()} Transaction with id {id} product_id {product_id} updated\n")

    def invoice(self, id, client_id, total_amount, invoice_date):
        self.cursor.execute("UPDATE Invoices SET client_id = %s, total_amount = %s, invoice_date = %s WHERE id = %s", (client_id, total_amount, invoice_date, id))
        self.connection.commit()
        print(f"Invoice with id {id} client_id {client_id} updated")
        log.write(f"{datetime.datetime.now()} Invoice with id {id} client_id {client_id} updated\n")

    def payment(self, id, invoice_id, amount, payment_date):
        self.cursor.execute("UPDATE Payments SET invoice_id = %s, amount = %s, payment_date = %s WHERE id = %s", (invoice_id, amount, payment_date, id))
        self.connection.commit()
        print(f"Payment with id {id} invoice_id {invoice_id} updated")
        log.write(f"{datetime.datetime.now()} Payment with id {id} invoice_id {invoice_id} updated\n")


class Delete:
    '''Class for deleting data from database'''

    def __init__(self, host=HOST, database=DATABASE, user=USER, password=PASSWORD):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
            
    def category(self, id):
        self.cursor.execute("DELETE FROM Categories WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Category with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Category with id {id} deleted\n")

    def client(self, id):
        self.cursor.execute("DELETE FROM Clients WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Client with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Client with id {id} deleted\n")

    def supplier(self, id):
        self.cursor.execute("DELETE FROM Suppliers WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Supplier with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Supplier with id {id} deleted\n")

    def user(self, id):
        self.cursor.execute("DELETE FROM Users WHERE id = %s", (id,))
        self.connection.commit()
        print(f"User with id {id} deleted")
        log.write(f"{datetime.datetime.now()} User with id {id} deleted\n")

    def employee(self, id):
        self.cursor.execute("DELETE FROM Employers WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Employee with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Employee with id {id} deleted\n")

    def product(self, id):
        self.cursor.execute("DELETE FROM Products WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Product with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Product with id {id} deleted\n")

    def sale(self, id):
        self.cursor.execute("DELETE FROM Sales WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Sale with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Sale with id {id} deleted\n")

    def purchase(self, id):
        self.cursor.execute("DELETE FROM Purchases WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Purchase with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Purchase with id {id} deleted\n")

    def order(self, id):
        self.cursor.execute("DELETE FROM Orders WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Order with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Order with id {id} deleted\n")

    def transaction(self, id):
        self.cursor.execute("DELETE FROM Transactions WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Transaction with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Transaction with id {id} deleted\n")

    def invoice(self, id):
        self.cursor.execute("DELETE FROM Invoices WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Invoice with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Invoice with id {id} deleted\n")

    def payment(self, id):
        self.cursor.execute("DELETE FROM Payments WHERE id = %s", (id,))
        self.connection.commit()
        print(f"Payment with id {id} deleted")
        log.write(f"{datetime.datetime.now()} Payment with id {id} deleted\n")


class Select:
    '''Class for selecting data from database'''

    def __init__(self, host=HOST, database=DATABASE, user=USER, password=PASSWORD):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    def categories(self):
        self.cursor.execute("SELECT * FROM Categories")
        return self.cursor.fetchall()
    
    def clients(self):
        self.cursor.execute("SELECT * FROM Clients")
        return self.cursor.fetchall()
    
    def suppliers(self):
        self.cursor.execute("SELECT * FROM Suppliers")
        return self.cursor.fetchall()
    
    def users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()
    
    def employees(self):
        self.cursor.execute("SELECT * FROM Employers")
        return self.cursor.fetchall()
    
    def products(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()
    
    def sales(self):
        self.cursor.execute("SELECT * FROM Sales")
        return self.cursor.fetchall()
    
    def purchases(self):
        self.cursor.execute("SELECT * FROM Purchases")
        return self.cursor.fetchall()
    
    def orders(self):
        self.cursor.execute("SELECT * FROM Orders")
        return self.cursor.fetchall()
    
    def transactions(self):
        self.cursor.execute("SELECT * FROM Transactions")
        return self.cursor.fetchall()
    
    def invoices(self):
        self.cursor.execute("SELECT * FROM Invoices")
        return self.cursor.fetchall()
    
    def payments(self):
        self.cursor.execute("SELECT * FROM Payments")
        return self.cursor.fetchall()
    

    def category(self, id):
        self.cursor.execute("SELECT * FROM Categories WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def client(self, id):
        self.cursor.execute("SELECT * FROM Clients WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def supplier(self, id):
        self.cursor.execute("SELECT * FROM Suppliers WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def user(self, id):
        self.cursor.execute("SELECT * FROM Users WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def employee(self, id):
        self.cursor.execute("SELECT * FROM Employers WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def product(self, id):
        self.cursor.execute("SELECT * FROM Products WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def sale(self, id):
        self.cursor.execute("SELECT * FROM Sales WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def purchase(self, id):
        self.cursor.execute("SELECT * FROM Purchases WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def order(self, id):
        self.cursor.execute("SELECT * FROM Orders WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def transaction(self, id):
        self.cursor.execute("SELECT * FROM Transactions WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def invoice(self, id):
        self.cursor.execute("SELECT * FROM Invoices WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
    def payment(self, id):
        self.cursor.execute("SELECT * FROM Payments WHERE id = %s", (id,))
        return self.cursor.fetchone()
    

    def category_by(self, column, value):
        self.cursor.execute("SELECT * FROM Categories WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def client_by(self, column, value):
        self.cursor.execute("SELECT * FROM Clients WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def supplier_by(self, column, value):
        self.cursor.execute("SELECT * FROM Suppliers WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def user_by(self, column, value):
        self.cursor.execute("SELECT * FROM Users WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def employee_by(self, column, value):
        self.cursor.execute("SELECT * FROM Employers WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def product_by(self, column, value):
        self.cursor.execute("SELECT * FROM Products WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def sale_by(self, column, value):
        self.cursor.execute("SELECT * FROM Sales WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def purchase_by(self, column, value):
        self.cursor.execute("SELECT * FROM Purchases WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def order_by(self, column, value):
        self.cursor.execute("SELECT * FROM Orders WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def transaction_by(self, column, value):
        self.cursor.execute("SELECT * FROM Transactions WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def invoice_by(self, column, value):
        self.cursor.execute("SELECT * FROM Invoices WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    
    def payment_by(self, column, value):
        self.cursor.execute("SELECT * FROM Payments WHERE %s = %s", (column, value))
        return self.cursor.fetchone()
    

    def categories_by(self, column, value):
        self.cursor.execute("SELECT * FROM Categories WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def clients_by(self, column, value):
        self.cursor.execute("SELECT * FROM Clients WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def suppliers_by(self, column, value):
        self.cursor.execute("SELECT * FROM Suppliers WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def users_by(self, column, value):
        self.cursor.execute("SELECT * FROM Users WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def employees_by(self, column, value):
        self.cursor.execute("SELECT * FROM Employers WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def products_by(self, column, value):
        self.cursor.execute("SELECT * FROM Products WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def sales_by(self, column, value):
        self.cursor.execute("SELECT * FROM Sales WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def purchases_by(self, column, value):
        self.cursor.execute("SELECT * FROM Purchases WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def orders_by(self, column, value):
        self.cursor.execute("SELECT * FROM Orders WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def transactions_by(self, column, value):
        self.cursor.execute("SELECT * FROM Transactions WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def invoices_by(self, column, value):
        self.cursor.execute("SELECT * FROM Invoices WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    
    def payments_by(self, column, value):
        self.cursor.execute("SELECT * FROM Payments WHERE %s = %s", (column, value))
        return self.cursor.fetchall()
    

insert = Insert()
insert.category("Test2", "Food")