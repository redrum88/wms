# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from datetime import date

BRANCH_SQL = """
DROP TABLE IF EXISTS Branch;
    CREATE TABLE Branch (
  branch_id SERIAL PRIMARY KEY,
  branch_name VARCHAR(50) NOT NULL,
  phone VARCHAR(50) NOT NULL,
  address VARCHAR(100) NOT NULL,
  post_code VARCHAR(10) NOT NULL
);
    """
INSERT_BRANCH_SQL = """
    INSERT INTO Branch (branch_name, phone, address, post_code)
    VALUES (?, ?, ?, ?)
    """
def add_branch(q, branch_name, phone, address, post_code):
    q.addBindValue(branch_name)
    q.addBindValue(phone)
    q.addBindValue(address)
    q.addBindValue(post_code)
    q.exec()
    return q.lastInsertId()
def add_default_branches():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_branch(q, "Default Branch", "1234567890", "1234 Default Street", "12345")
    add_branch(q, "Branch 2", "1234567890", "1234 Default Street", "12345")
    add_branch(q, "Branch 3", "1234567890", "1234 Default Street", "12345")
    add_branch(q, "Branch 4", "1234567890", "1234 Default Street", "12345")
    add_branch(q, "Branch 5", "1234567890", "1234 Default Street", "12345")

PLACE_SQL = """
DROP TABLE IF EXISTS Place;
CREATE TABLE Place (
  place_id SERIAL PRIMARY KEY,
  place_name VARCHAR(50) NOT NULL,
  place_barcode VARCHAR(50) NOT NULL,
  description TEXT,
  branch_id INTEGER NOT NULL,
  FOREIGN KEY (branch_id)
    REFERENCES Branch (branch_id)
);
"""
INSERT_PLACE_SQL = """
    INSERT INTO Place (place_name, place_barcode, description, branch_id)
    VALUES (?, ?, ?, ?)
    """
def add_place(q, place_name, place_barcode, description, branch_id):
    q.addBindValue(place_name)
    q.addBindValue(place_barcode)
    q.addBindValue(description)
    q.addBindValue(branch_id)
    q.exec()
    return q.lastInsertId()
def add_default_places():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_place(q, "Default Place", "1234567890", "Default Place", 1)
    add_place(q, "Place 2", "1234567890", "Place 2", 1)
    add_place(q, "Place 3", "1234567890", "Place 3", 1)
    add_place(q, "Place 4", "1234567890", "Place 4", 1)
    add_place(q, "Place 5", "1234567890", "Place 5", 1)

LOCATION_SQL = """
DROP TABLE IF EXISTS Location;
CREATE TABLE Location (
  location_id SERIAL PRIMARY KEY,
  x TEXT NOT NULL,
  y TEXT NOT NULL,
  z TEXT NOT NULL,
  location_barcode VARCHAR(50) NOT NULL,
  place_id INTEGER NOT NULL,
  FOREIGN KEY (place_id)
    REFERENCES Place (place_id)
);
"""
INSERT_LOCATION_SQL = """
    INSERT INTO Location (x, y, z, location_barcode, place_id)
    VALUES (?, ?, ?, ?, ?)
    """
def add_location(q, x, y, z, location_barcode, place_id):
    q.addBindValue(x)
    q.addBindValue(y)
    q.addBindValue(z)
    q.addBindValue(location_barcode)
    q.addBindValue(place_id)
    q.exec()
    return q.lastInsertId()
def add_default_locations():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_location(q, "0", "0", "0", "safasdf", 1)
    add_location(q, "0", "0", "0", "asdgfsadg", 1)
    add_location(q, "0", "0", "0", "gsdfg", 1)
    add_location(q, "0", "0", "0", "asgfsddf", 1)
    add_location(q, "0", "0", "0", "gdfsdf", 1)
    if not q.execBatch():
        print(q.lastError().text())


USERGROUP_SQL = """
DROP TABLE IF EXISTS UserGroup;
CREATE TABLE UserGroup (
  group_id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  access_level INTEGER NOT NULL
);
"""
INSERT_USERGROUP_SQL = """
    INSERT INTO UserGroup (name, access_level)
    VALUES (?, ?)
    """
def add_usergroup(q, name, access_level):
    q.addBindValue(name)
    q.addBindValue(access_level)
    q.exec()
    return q.lastInsertId()
def add_default_usergroups():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_usergroup(q, "System Admin", 10)
    add_usergroup(q, "Admin", 5)
    add_usergroup(q, "Manager", 3)
    add_usergroup(q, "Employee", 1)
    if not q.execBatch():
        print(q.lastError().text())


USERS_SQL = """
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  user_id SERIAL PRIMARY KEY,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  group_id INTEGER NOT NULL,
  FOREIGN KEY (group_id)
    REFERENCES UserGroup (group_id)
);
"""
INSERT_USERS_SQL = """
    INSERT INTO Users (email, password, group_id)
    VALUES (?, ?, ?)
    """
def add_users(q, email, password, group_id):
    q.addBindValue(email)
    q.addBindValue(password)
    q.addBindValue(group_id)
    q.exec()
    return q.lastInsertId()
def add_default_users():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_users(q, "Admin", "Admin", 1)
    add_users(q, "Manager", "Manager", 2)
    add_users(q, "Employee", "Employee", 3)
    if not q.execBatch():
        print(q.lastError().text())


CATEGORY_SQL = """
DROP TABLE IF EXISTS Category;
CREATE TABLE Category (
  category_id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  place_id INTEGER,
  FOREIGN KEY (place_id)
    REFERENCES Place (place_id)
);
"""
INSERT_CATEGORY_SQL = """
    INSERT INTO Category (name, description, place_id)
    VALUES (?, ?, ?)
    """
def add_category(q, name, description, place_id):
    q.addBindValue(name)
    q.addBindValue(description)
    q.addBindValue(place_id)
    q.exec()
    return q.lastInsertId()
def add_default_categories():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_category(q, "Default Category", "Default Category", 1)
    add_category(q, "Category 2", "Category 2", 1)
    add_category(q, "Category 3", "Category 3", 1)
    add_category(q, "Category 4", "Category 4", 1)
    add_category(q, "Category 5", "Category 5", 1)
    if not q.execBatch():
        print(q.lastError().text())

SUBCATEGORY_SQL = """
DROP TABLE IF EXISTS SubCategory;
CREATE TABLE SubCategory (
  subcategory_id SERIAL PRIMARY KEY,
  category_id INTEGER NOT NULL,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  location_id INTEGER,
  FOREIGN KEY (category_id)
    REFERENCES Category (category_id),
  FOREIGN KEY (location_id)
    REFERENCES Location (location_id)
);
"""
INSERT_SUBCATEGORY_SQL = """
    INSERT INTO SubCategory (category_id, name, description, location_id)
    VALUES (?, ?, ?, ?)
    """
def add_subcategory(q, category_id, name, description, location_id):
    q.addBindValue(category_id)
    q.addBindValue(name)
    q.addBindValue(description)
    q.addBindValue(location_id)
    q.exec()
    return q.lastInsertId()
def add_default_subcategories():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_subcategory(q, 1, "Default SubCategory", "Default SubCategory", 1)
    add_subcategory(q, 1, "SubCategory 2", "SubCategory 2", 1)
    add_subcategory(q, 1, "SubCategory 3", "SubCategory 3", 1)
    add_subcategory(q, 1, "SubCategory 4", "SubCategory 4", 1)
    add_subcategory(q, 1, "SubCategory 5", "SubCategory 5", 1)
    if not q.execBatch():
        print(q.lastError().text())


CLIENTS_SQL = """
DROP TABLE IF EXISTS Clients;
CREATE TABLE Clients (
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  company VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  post_code VARCHAR(255) NOT NULL,
  note VARCHAR(255) NULL
);
"""
INSERT_CLIENTS_SQL = """
    INSERT INTO Clients (firstname, lastname, company, email, phone, address, post_code, note)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
def add_clients(q, firstname, lastname, company, email, phone, address, post_code, note):
    q.addBindValue(firstname)
    q.addBindValue(lastname)
    q.addBindValue(company)
    q.addBindValue(email)
    q.addBindValue(phone)
    q.addBindValue(address)
    q.addBindValue(post_code)
    q.addBindValue(note)
    q.exec()
    return q.lastInsertId()
def add_default_clients():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_clients(q, "Default", "Client", "Default Company", "Email", "Phone", "Address", "Post Code", "Note")
    add_clients(q, "Client", "2", "Company", "Email", "Phone", "Address", "Post Code", "Note")
    add_clients(q, "Client", "3", "Company", "Email", "Phone", "Address", "Post Code", "Note")
    add_clients(q, "Client", "4", "Company", "Email", "Phone", "Address", "Post Code", "Note")
    add_clients(q, "Client", "5", "Company", "Email", "Phone", "Address", "Post Code", "Note")



EMPLOYEE_SQL = """
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  job_title VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  post_code VARCHAR(255) NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id)
    REFERENCES Users (user_id)
);
"""
INSERT_EMPLOYEE_SQL = """
    INSERT INTO Employee (firstname, lastname, job_title, phone, address, post_code, user_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
def add_employee(q, firstname, lastname, job_title, phone, address, post_code, user_id):
    q.addBindValue(firstname)
    q.addBindValue(lastname)
    q.addBindValue(job_title)
    q.addBindValue(phone)
    q.addBindValue(address)
    q.addBindValue(post_code)
    q.addBindValue(user_id)
    q.exec()
    return q.lastInsertId()
def add_default_employee():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_employee(q, "Default", "Employee", "Default Job Title", "Phone", "Address", "Post Code", 1)
    add_employee(q, "Manager", "2", "Job Title", "Phone", "Address", "Post Code", 2)
    add_employee(q, "Employee", "3", "Job Title", "Phone", "Address", "Post Code", 3)

SUPPLIER_SQL = """
DROP TABLE IF EXISTS Supplier;
CREATE TABLE Supplier (
  id SERIAL PRIMARY KEY,
  company VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  post_code VARCHAR(255) NOT NULL,
  note VARCHAR(255) NULL
);
"""
INSERT_SUPPLIER_SQL = """
    INSERT INTO Supplier (company, contact_name, email, phone, address, post_code, note)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
def add_supplier(q, company, contact_name, email, phone, address, post_code, note):
    q.addBindValue(company)
    q.addBindValue(contact_name)
    q.addBindValue(email)
    q.addBindValue(phone)
    q.addBindValue(address)
    q.addBindValue(post_code)
    q.addBindValue(note)
    q.exec()
    return q.lastInsertId()
def add_default_supplier():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_supplier(q, "Default", "Supplier", "Email", "Phone", "Address", "Post Code", "Note")
    add_supplier(q, "Supplier", "2", "Email", "Phone", "Address", "Post Code", "Note")
    add_supplier(q, "Supplier", "3", "Email", "Phone", "Address", "Post Code", "Note")
    add_supplier(q, "Supplier", "4", "Email", "Phone", "Address", "Post Code", "Note")
    add_supplier(q, "Supplier", "5", "Email", "Phone", "Address", "Post Code", "Note")


PRODUCT_SQL = """
DROP TABLE IF EXISTS Product;
CREATE TABLE Product (
  id SERIAL PRIMARY KEY,
  barcode VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL,
  subcategory_id INT NOT NULL,
  quantity INT NOT NULL,
  price INT,
  supplier_id INT NOT NULL,
  note VARCHAR(255) NULL,
  FOREIGN KEY (subcategory_id)
    REFERENCES SubCategory (subcategory_id),
  FOREIGN KEY (supplier_id)
    REFERENCES Supplier (id)
);
"""
INSERT_PRODUCT_SQL = """
    INSERT INTO Product (barcode, name, description, subcategory_id, quantity, price, supplier_id, note)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
def add_product(q, barcode, name, description, subcategory_id, quantity, price, supplier_id, note):
    q.addBindValue(barcode)
    q.addBindValue(name)
    q.addBindValue(description)
    q.addBindValue(subcategory_id)
    q.addBindValue(quantity)
    q.addBindValue(price)
    q.addBindValue(supplier_id)
    q.addBindValue(note)
    q.exec()
    return q.lastInsertId()
def add_default_product():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_product(q, "Default", "Product", "Description", 1, 1, 1, 1, "Note")
    add_product(q, "Product", "2", "Description", 2, 2, 2, 2, "Note")
    add_product(q, "Product", "3", "Description", 3, 3, 3, 3, "Note")
    add_product(q, "Product", "4", "Description", 4, 4, 4, 4, "Note")
    add_product(q, "Product", "5", "Description", 5, 5, 5, 5, "Note")

PURCHASE_SQL = """
DROP TABLE IF EXISTS Purchase;
CREATE TABLE Purchase (
  id SERIAL PRIMARY KEY,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  purchase_date DATE NOT NULL,
  supplier_id INT NOT NULL,
  employee_id INT NOT NULL,
  FOREIGN KEY (product_id)
    REFERENCES Product (id),
  FOREIGN KEY (supplier_id)
    REFERENCES Supplier (id),
  FOREIGN KEY (employee_id)
    REFERENCES Employee (id)
);
"""
INSERT_PURCHASE_SQL = """
    INSERT INTO Purchase (product_id, quantity, purchase_date, supplier_id, employee_id)
    VALUES (?, ?, ?, ?, ?)
    """
def add_purchase(q, product_id, quantity, purchase_date, supplier_id, employee_id):
    q.addBindValue(product_id)
    q.addBindValue(quantity)
    q.addBindValue(purchase_date)
    q.addBindValue(supplier_id)
    q.addBindValue(employee_id)
    q.exec()
    return q.lastInsertId()
def add_default_purchase():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_purchase(q, 1, 1, "2019-01-01", 1, 1)
    add_purchase(q, 2, 2, "2019-01-02", 2, 2)
    add_purchase(q, 3, 3, "2019-01-03", 3, 3)
    add_purchase(q, 4, 4, "2019-01-04", 4, 4)
    add_purchase(q, 5, 5, "2019-01-05", 5, 5)


STOCK_SQL = """
DROP TABLE IF EXISTS Stock;
CREATE TABLE Stock (
  stock_id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL,
  category_id INTEGER NOT NULL,
  subcategory_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  supplier_id INTEGER NOT NULL,
  purchase_id INTEGER NOT NULL,
  employee_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  cost_price NUMERIC(10,2) NOT NULL,
  selling_price NUMERIC(10,2) NOT NULL,
  barcode TEXT NOT NULL,
  FOREIGN KEY (product_id) REFERENCES Product (id),
  FOREIGN KEY (category_id) REFERENCES Category (category_id),
  FOREIGN KEY (subcategory_id) REFERENCES SubCategory (subcategory_id),
  FOREIGN KEY (location_id) REFERENCES Location (location_id),
  FOREIGN KEY (supplier_id) REFERENCES Supplier (id),
  FOREIGN KEY (purchase_id) REFERENCES Purchase (id),
  FOREIGN KEY (employee_id) REFERENCES Employee (id)
);
"""
INSERT_STOCK_SQL = """
    INSERT INTO Stock (product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
def add_stock(q, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
    q.addBindValue(product_id)
    q.addBindValue(category_id)
    q.addBindValue(subcategory_id)
    q.addBindValue(location_id)
    q.addBindValue(supplier_id)
    q.addBindValue(purchase_id)
    q.addBindValue(employee_id)
    q.addBindValue(quantity)
    q.addBindValue(cost_price)
    q.addBindValue(selling_price)
    q.addBindValue(barcode)
    q.exec()
    return q.lastInsertId()
def add_default_stock():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_stock(q, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "1")
    add_stock(q, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "2")
    add_stock(q, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, "3")
    add_stock(q, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, "4")
    add_stock(q, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, "5")

SALE_SQL = """
DROP TABLE IF EXISTS Sale;
CREATE TABLE Sale (
  id SERIAL PRIMARY KEY,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  sale_date DATE NOT NULL,
  client_id INT NOT NULL,
  employee_id INT NOT NULL,
  FOREIGN KEY (product_id)
    REFERENCES Product (id),
  FOREIGN KEY (client_id)
    REFERENCES Clients (id),
  FOREIGN KEY (employee_id)
    REFERENCES Employee (id)
);
"""
INSERT_SALE_SQL = """
    INSERT INTO Sale (product_id, quantity, sale_date, client_id, employee_id)
    VALUES (?, ?, ?, ?, ?)
    """
def add_sale(q, product_id, quantity, sale_date, client_id, employee_id):
    q.addBindValue(product_id)
    q.addBindValue(quantity)
    q.addBindValue(sale_date)
    q.addBindValue(client_id)
    q.addBindValue(employee_id)
    q.exec()
    return q.lastInsertId()
def add_default_sale():
    db = QSqlDatabase.database()
    q = QSqlQuery(db=db)
    add_sale(q, 1, 1, "2019-01-01", 1, 1)
    add_sale(q, 2, 2, "2019-01-02", 2, 2)
    add_sale(q, 3, 3, "2019-01-03", 3, 3)
    add_sale(q, 4, 4, "2019-01-04", 4, 4)
    add_sale(q, 5, 5, "2019-01-05", 5, 5)

import sys
def init_db(DB_TYPE="QPSQL", HOSTNAME="localhost", DATABASE="", USERNAME="postgres", PASSWORD="", PORT=5432):
    """
    init_db()
    Initializes PostgreSQL database with PySide6.QtSql.
    If tables "User" and "Category" etc.. are already in the database, do nothing.
    Prints error message if database cannot be opened.
    """
    def check(func, *args):
        if func(*args):
            return True
        else:
            print("ERROR: ", func(*args).lastError().text())
            sys.exit(1)

    db = QSqlDatabase.addDatabase(DB_TYPE)
    db.setHostName(HOSTNAME)
    db.setDatabaseName(DATABASE)
    db.setUserName(USERNAME)
    db.setPassword(PASSWORD)

    check(db.open)
    print("Opened database successfully")
    q = QSqlQuery()
    check(q.exec, BRANCH_SQL)
    print("Branch table created successfully")

    check(q.exec, PLACE_SQL)
    print("Place table created successfully")

    check(q.exec, LOCATION_SQL)
    print("Location table created successfully")

    check(q.exec, USERGROUP_SQL)
    print("UserGroup table created successfully")

    check(q.exec, USERS_SQL)
    print("User table created successfully")

    check(q.exec, CATEGORY_SQL)
    print("Category table created successfully")

    check(q.exec, SUBCATEGORY_SQL)
    print("SubCategory table created successfully")

    check(q.exec, CLIENTS_SQL)
    print("Client table created successfully")

    check(q.exec, SUPPLIER_SQL)
    print("Supplier table created successfully")

    check(q.exec, EMPLOYEE_SQL)
    print("Employee table created successfully")

    check(q.exec, PRODUCT_SQL)
    print("Product table created successfully")

    check(q.exec, PURCHASE_SQL)
    print("Purchase table created successfully")

    check(q.exec, STOCK_SQL)
    print("Stock table created successfully")

    check(q.exec, SALE_SQL)
    print("Sale table created successfully")
    print("All tables initialized successfully")

    add_default_branches()
    print("Default branches added successfully")

    add_default_places()
    print("Default places added successfully")

    add_default_locations()
    print("Default locations added successfully")

    add_default_usergroups()
    print("Default usergroups added successfully")

    add_default_users()
    print("Default users added successfully")

    add_default_categories()
    print("Default categories added successfully")

    add_default_subcategories()
    print("Default subcategories added successfully")

    add_default_clients()
    print("Default clients added successfully")

    add_default_supplier()
    print("Default suppliers added successfully")

    add_default_employee()
    print("Default employees added successfully")

    add_default_product()
    print("Default products added successfully")

    add_default_purchase()
    print("Default purchases added successfully")

    add_default_stock()
    print("Default stock added successfully")

    add_default_sale()
    print("Default sales added successfully")

    print("Default data added successfully")
