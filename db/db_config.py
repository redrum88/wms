import psycopg2
import psycopg2.extras

'''Connection to database class'''

HOST = "localhost"
DATABASE = "name"
USER = "postgres"
PASSWORD = "password"

class Database:
    def __init__(self):
        # Try to connect to database and if connection is successful create cursor else create database and connect to it
        try:
            self.connection = psycopg2.connect(
                host=HOST, database=DATABASE, user=USER, password=PASSWORD)
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            print("Database connected")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to database", error)
            self.connection = psycopg2.connect(
                host=HOST, database=DATABASE, user=USER, password=PASSWORD)
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
            print("Database created and connected")

    def create_tables(self):
        print("Creating tables")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Categories (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS UserGroups (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, access_level INT NOT NULL)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Clients (id SERIAL PRIMARY KEY, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, company VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, phone INT NOT NULL, address VARCHAR(255) NOT NULL, post_code VARCHAR(255) NOT NULL, note VARCHAR(255) NULL)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Suppliers (id SERIAL PRIMARY KEY, company VARCHAR(255) NOT NULL, contact_name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, phone INT NOT NULL, address VARCHAR(255) NOT NULL, post_code VARCHAR(255) NOT NULL, note VARCHAR(255) NULL)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Users (id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, usergroup_id INT NOT NULL, FOREIGN KEY (usergroup_id) REFERENCES UserGroups(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Employers (id SERIAL PRIMARY KEY, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, job_title VARCHAR(255) NOT NULL, phone INT NOT NULL, address VARCHAR(255) NOT NULL, employee_id INT NOT NULL, FOREIGN KEY (employee_id) REFERENCES Users(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Products (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, category_id INT NOT NULL, quantity INT NOT NULL, price INT NOT NULL, supplier_id INT NOT NULL, note VARCHAR(255) NULL, FOREIGN KEY (category_id) REFERENCES Categories(id), FOREIGN KEY (supplier_id) REFERENCES Suppliers(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Sales (id SERIAL PRIMARY KEY, product_id INT NOT NULL, quantity INT NOT NULL, price INT NOT NULL, sale_date DATE NOT NULL, FOREIGN KEY (product_id) REFERENCES Products(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Purchases (id SERIAL PRIMARY KEY, product_id INT NOT NULL, quantity INT NOT NULL, price INT NOT NULL, purchase_date DATE NOT NULL, FOREIGN KEY (product_id) REFERENCES Products(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Orders (id SERIAL PRIMARY KEY, product_id INT NOT NULL, quantity INT NOT NULL, order_date DATE NOT NULL, delivery_date DATE NOT NULL, FOREIGN KEY (product_id) REFERENCES Products(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Transactions (id SERIAL PRIMARY KEY, product_id INT NOT NULL, quantity INT NOT NULL, transaction_date DATE NOT NULL, transaction_type VARCHAR(255) NOT NULL, FOREIGN KEY (product_id) REFERENCES Products(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Invoices (id SERIAL PRIMARY KEY, client_id INT NOT NULL, total_amount INT NOT NULL, invoice_date DATE NOT NULL, FOREIGN KEY (client_id) REFERENCES Clients(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Payments (id SERIAL PRIMARY KEY, invoice_id INT NOT NULL, amount INT NOT NULL, payment_date DATE NOT NULL, FOREIGN KEY (invoice_id) REFERENCES Invoices(id))")
        
        self.connection.commit()
        print("Tables created")


    def insert_data(self):
        '''Insert data into tables'''
        print("Inserting data")
        self.cursor.execute(
            "INSERT INTO Categories (name, description) VALUES ('Electronics', 'Electronics description')")
        self.connection.commit()
        print("Data inserted into Categories table")

        self.cursor.execute(
            "INSERT INTO UserGroups (name, access_level) VALUES ('Admin', 1)")
        self.connection.commit()
        print("Data inserted into UserGroups table")

        self.cursor.execute(
            "INSERT INTO Clients (firstname, lastname, company, email, phone, address, post_code, note) VALUES ('John', 'Doe', 'Company', 'CocaCola', 123456789, 'Address', 'LT-12345', 'Note')")
        self.connection.commit()
        print("Data inserted into Clients table")

        self.cursor.execute(
            "INSERT INTO Suppliers (company, contact_name, email, phone, address, post_code, note) VALUES ('Company', 'Contact name', 'CocaCola', 123456789, 'Address', 'LT-12345', 'Note')")
        self.connection.commit()
        print("Data inserted into Suppliers table")

        self.cursor.execute(
            "INSERT INTO Users (username, password, usergroup_id) VALUES ('admin', 'admin', 1)")
        self.connection.commit()
        print("Data inserted into Users table")

        self.cursor.execute(
            "INSERT INTO Employers (firstname, lastname, job_title, phone, address, employee_id) VALUES ('John', 'Doe', 'Job title', 123456789, 'Address', 1)")
        self.connection.commit()
        print("Data inserted into Employers table")

        self.cursor.execute(
            "INSERT INTO Products (name, description, category_id, quantity, price, supplier_id, note) VALUES ('Product', 'Product description', 1, 10, 100, 1, 'Note')")
        self.connection.commit()
        print("Data inserted into Products table")

        self.cursor.execute(
            "INSERT INTO Sales (product_id, quantity, price, sale_date) VALUES (1, 1, 100, '2020-01-01')")
        self.connection.commit()
        print("Data inserted into Sales table")

        self.cursor.execute(
            "INSERT INTO Purchases (product_id, quantity, price, purchase_date) VALUES (1, 1, 100, '2020-01-01')")
        self.connection.commit()
        print("Data inserted into Purchases table")

        self.cursor.execute(
            "INSERT INTO Orders (product_id, quantity, order_date, delivery_date) VALUES (1, 1, '2020-01-01', '2020-01-01')")
        self.connection.commit()
        print("Data inserted into Orders table")

        self.cursor.execute(
            "INSERT INTO Transactions (product_id, quantity, transaction_date, transaction_type) VALUES (1, 1, '2020-01-01', 'Transaction type')")
        self.connection.commit()
        print("Data inserted into Transactions table")

        self.cursor.execute(
            "INSERT INTO Invoices (client_id, total_amount, invoice_date) VALUES (1, 100, '2020-01-01')")
        self.connection.commit()
        print("Data inserted into Invoices table")

        self.cursor.execute(
            "INSERT INTO Payments (invoice_id, amount, payment_date) VALUES (1, 100, '2020-01-01')")
        self.connection.commit()
        print("Data inserted into Payments table")


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    db.insert_data()