# Create class for data insert in database tables. We use db_config.py to connect to database.

import sys
import os

# Add path to db directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import psycopg2
from db.db_config import Database

class Insert(Database):
    def __init__(self):
        super().__init__()


    def insert_category(self, name, description):
        self.cursor.execute("INSERT INTO Categories (name, description) VALUES (%s, %s)", (name, description))
        self.connection.commit()

    def insert_usergroup(self, name, access_level):
        self.cursor.execute("INSERT INTO UserGroups (name, access_level) VALUES (%s, %s)", (name, access_level))
        self.connection.commit()

    def insert_client(self, firstname, lastname, company, email, phone, address, post_code, note):
        self.cursor.execute("INSERT INTO Clients (firstname, lastname, company, email, phone, address, post_code, note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, company, email, phone, address, post_code, note))
        self.connection.commit()

    def insert_supplier(self, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("INSERT INTO Suppliers (company, contact_name, email, phone, address, post_code, note) VALUES (%s, %s, %s, %s, %s, %s, %s)", (company, contact_name, email, phone, address, post_code, note))
        self.connection.commit()

    def insert_user(self, username, password, usergroup_id):
        self.cursor.execute("INSERT INTO Users (username, password, usergroup_id) VALUES (%s, %s, %s)", (username, password, usergroup_id))
        self.connection.commit()

    def insert_empoyee(self, firstname, lastname, job_title, phone, address, employee_id):
        self.cursor.execute("INSERT INTO Employers (firstname, lastname, job_title, phone, address, employee_id) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, lastname, job_title, phone, address, employee_id))
        self.connection.commit()

    def insert_product(self, name, description, category_id, quantity, price, supplier_id, note):
        self.cursor.execute("INSERT INTO Products (name, description, category_id, quantity, price, supplier_id, note) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, description, category_id, quantity, price, supplier_id, note))
        self.connection.commit()

    def insert_sale(self, product_id, quantity, price, sale_date):
        self.cursor.execute("INSERT INTO Sales (product_id, quantity, price, sale_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, price, sale_date))
        self.connection.commit()

    def insert_purchase(self, product_id, quantity, price, purchase_date):
        self.cursor.execute("INSERT INTO Purchases (product_id, quantity, price, purchase_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, price, purchase_date))
        self.connection.commit()

    def insert_order(self, product_id, quantity, order_date, delivery_date):
        self.cursor.execute("INSERT INTO Orders (product_id, quantity, order_date, delivery_date) VALUES (%s, %s, %s, %s)", (product_id, quantity, order_date, delivery_date))
        self.connection.commit()

    def insert_transaction(self, product_id, quantity, transaction_date, transaction_type):
        self.cursor.execute("INSERT INTO Transactions (product_id, quantity, transaction_date, transaction_type) VALUES (%s, %s, %s, %s)", (product_id, quantity, transaction_date, transaction_type))
        self.connection.commit()

    def insert_invoice(self, client_id, total_amount, invoice_date):
        self.cursor.execute("INSERT INTO Invoices (client_id, total_amount, invoice_date) VALUES (%s, %s, %s)", (client_id, total_amount, invoice_date))
        self.connection.commit()

    def insert_payment(self, invoice_id, amount, payment_date):
        self.cursor.execute("INSERT INTO Payments (invoice_id, amount, payment_date) VALUES (%s, %s, %s)", (invoice_id, amount, payment_date))
        self.connection.commit()

class Update(Database):
    def __init__(self):
        super().__init__()

    def category(self, id, name, description):
        self.cursor.execute("UPDATE Categories SET name = %s, description = %s WHERE id = %s", (name, description, id))
        self.connection.commit()

    def client(self, id, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("UPDATE Clients SET company = %s, contact_name = %s, email = %s, phone = %s, address = %s, post_code = %s, note = %s WHERE id = %s", (company, contact_name, email, phone, address, post_code, note, id))
        self.connection.commit()

    def supplier(self, id, company, contact_name, email, phone, address, post_code, note):
        self.cursor.execute("UPDATE Suppliers SET company = %s, contact_name = %s, email = %s, phone = %s, address = %s, post_code = %s, note = %s WHERE id = %s", (company, contact_name, email, phone, address, post_code, note, id))
        self.connection.commit()

    def user(self, id, username, password, usergroup_id):
        self.cursor.execute("UPDATE Users SET username = %s, password = %s, usergroup_id = %s WHERE id = %s", (username, password, usergroup_id, id))
        self.connection.commit()

    def employee(self, id, firstname, lastname, job_title, phone, address, employee_id):
        self.cursor.execute("UPDATE Employers SET firstname = %s, lastname = %s, job_title = %s, phone = %s, address = %s, employee_id = %s WHERE id = %s", (firstname, lastname, job_title, phone, address, employee_id, id))
        self.connection.commit()

    def product(self, id, name, description, category_id, quantity, price, supplier_id, note):
        self.cursor.execute("UPDATE Products SET name = %s, description = %s, category_id = %s, quantity = %s, price = %s, supplier_id = %s, note = %s WHERE id = %s", (name, description, category_id, quantity, price, supplier_id, note, id))
        self.connection.commit()

    def sale(self, id, product_id, quantity, price, sale_date):
        self.cursor.execute("UPDATE Sales SET product_id = %s, quantity = %s, price = %s, sale_date = %s WHERE id = %s", (product_id, quantity, price, sale_date, id))
        self.connection.commit()

    def purchase(self, id, product_id, quantity, price, purchase_date):
        self.cursor.execute("UPDATE Purchases SET product_id = %s, quantity = %s, price = %s, purchase_date = %s WHERE id = %s", (product_id, quantity, price, purchase_date, id))
        self.connection.commit()

    def order(self, id, product_id, quantity, order_date, delivery_date):
        self.cursor.execute("UPDATE Orders SET product_id = %s, quantity = %s, order_date = %s, delivery_date = %s WHERE id = %s", (product_id, quantity, order_date, delivery_date, id))
        self.connection.commit()

    def transaction(self, id, product_id, quantity, transaction_date, transaction_type):
        self.cursor.execute("UPDATE Transactions SET product_id = %s, quantity = %s, transaction_date = %s, transaction_type = %s WHERE id = %s", (product_id, quantity, transaction_date, transaction_type, id))
        self.connection.commit()

    def invoice(self, id, client_id, total_amount, invoice_date):
        self.cursor.execute("UPDATE Invoices SET client_id = %s, total_amount = %s, invoice_date = %s WHERE id = %s", (client_id, total_amount, invoice_date, id))
        self.connection.commit()

    def payment(self, id, invoice_id, amount, payment_date):
        self.cursor.execute("UPDATE Payments SET invoice_id = %s, amount = %s, payment_date = %s WHERE id = %s", (invoice_id, amount, payment_date, id))
        self.connection.commit()


class Delete(Database):
    def __init__(self):
        super().__init__()

    def category(self, id):
        self.cursor.execute("DELETE FROM Categories WHERE id = %s", (id,))
        self.connection.commit()

    def client(self, id):
        self.cursor.execute("DELETE FROM Clients WHERE id = %s", (id,))
        self.connection.commit()

    def supplier(self, id):
        self.cursor.execute("DELETE FROM Suppliers WHERE id = %s", (id,))
        self.connection.commit()

    def user(self, id):
        self.cursor.execute("DELETE FROM Users WHERE id = %s", (id,))
        self.connection.commit()

    def employee(self, id):
        self.cursor.execute("DELETE FROM Employers WHERE id = %s", (id,))
        self.connection.commit()

    def product(self, id):
        self.cursor.execute("DELETE FROM Products WHERE id = %s", (id,))
        self.connection.commit()

    def sale(self, id):
        self.cursor.execute("DELETE FROM Sales WHERE id = %s", (id,))
        self.connection.commit()

    def purchase(self, id):
        self.cursor.execute("DELETE FROM Purchases WHERE id = %s", (id,))
        self.connection.commit()

    def order(self, id):
        self.cursor.execute("DELETE FROM Orders WHERE id = %s", (id,))
        self.connection.commit()

    def transaction(self, id):
        self.cursor.execute("DELETE FROM Transactions WHERE id = %s", (id,))
        self.connection.commit()

    def invoice(self, id):
        self.cursor.execute("DELETE FROM Invoices WHERE id = %s", (id,))
        self.connection.commit()

    def payment(self, id):
        self.cursor.execute("DELETE FROM Payments WHERE id = %s", (id,))
        self.connection.commit()


class Select(Database):
    def __init__(self):
        super().__init__()

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