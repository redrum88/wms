import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from settings import DB

db = DB()

class CRUD:
    def __init__(self, db):
        self.db = db

    def branch_columns(self):
        # Get from table Branch all columns
        query = QSqlQuery()
        query.exec("SELECT * FROM branch")
        record = query.record()
        columns = []
        for i in range(record.count()):
            columns.append(record.fieldName(i))
        return columns
    
    def place_columns(self):
        # Get from table Place all columns
        query = QSqlQuery()
        query.exec("SELECT * FROM place")
        record = query.record()
        columns = []
        for i in range(record.count()):
            columns.append(record.fieldName(i))
        return columns

    def create(self, table, values):
        query = QSqlQuery()
        query.exec(f"INSERT INTO {table} VALUES {values}")
    def read(self, table, id):
        query = QSqlQuery()
        query.exec(f"SELECT * FROM {table} WHERE id = {id}")
        return query
    def read_all(self, table):
        query = QSqlQuery()
        query.exec(f"SELECT * FROM {table}")
        return query
    def update(self, table, id, values):
        query = QSqlQuery()
        query.exec(f"UPDATE {table} SET {values} WHERE id = {id}")
    def delete(self, table, id):
        query = QSqlQuery()
        query.exec(f"DELETE FROM {table} WHERE id = {id}")

    def select_branch():
        query = QSqlQuery()
        query.exec("SELECT * FROM branch")
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def select_branch_by_any(branch_name='', phone='', address='', post_code=''):
        query = QSqlQuery()
        query.prepare("SELECT * FROM branch WHERE branch_name = ? OR phone = ? OR address = ? OR post_code = ?")
        query.addBindValue(branch_name)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def select_branch_by_id(branch_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM branch WHERE branch_id = ? ")
        query.addBindValue(branch_id)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def insert_branch(branch_name, phone, address, post_code):
        query = QSqlQuery()
        query.prepare("INSERT INTO branch (branch_name, phone, address, post_code) VALUES (?, ?, ?, ?)")
        query.addBindValue(branch_name)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        if not query.exec():
            print("Insert branch error: ", query.lastError().text())
            return False
        print("Insert branch success")
        print(query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def update_branch(branch_id, branch_name, phone, address, post_code):
        query = QSqlQuery()
        query.prepare("UPDATE branch SET branch_name = ?, phone = ?, address = ?, post_code = ? WHERE branch_id = ?")
        query.addBindValue(branch_name)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(branch_id)
        if not query.exec():
            print("Update branch error: ", query.lastError().text())
            return False
        print("Update branch success")
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def delete_branch(self, branch_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM branch WHERE branch_id = ?")
        query.addBindValue(branch_id)
        if not query.exec():
            print("Delete branch error: ", query.lastError().text())
            return False
        print("Delete branch success")
        print(query.executedQuery())
        print(query.boundValues())
        return True
    
    def select_place():
        query = QSqlQuery()
        query.exec("SELECT * FROM place")
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def select_place_by_any(place_id, place_name, place_barcode, branch_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM place WHERE place_id = ? OR place_name = ? OR place_barcode = ? OR branch_id = ?")
        query.addBindValue(place_id)
        query.addBindValue(place_name)
        query.addBindValue(place_barcode)
        query.addBindValue(branch_id)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def select_place_by_id(place_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM place WHERE place_id = ?")
        query.addBindValue(place_id)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def insert_place(place_name, place_barcode, branch_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO place (place_name, place_barcode, branch_id) VALUES (?, ?, ?)")
        query.addBindValue(place_name)
        query.addBindValue(place_barcode)
        query.addBindValue(branch_id)
        if not query.exec():
            print("Insert place error: ", query.lastError().text())
            return False
        print("Insert place success. Last insert id: ", query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def update_place(place_id, place_name, place_barcode, branch_id):
        query = QSqlQuery()
        query.prepare("UPDATE place SET place_id = ?, place_name = ?, place_barcode = ?, branch_id = ? WHERE place_id = ?")
        query.addBindValue(place_id)
        query.addBindValue(place_name)
        query.addBindValue(place_barcode)
        query.addBindValue(branch_id)
        query.addBindValue(place_id)
        if not query.exec():
            print("Update place error: ", query.lastError().text())
            return False
        print("Update place success. Id: ", query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def delete_place(place_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM place WHERE place_id = ?")
        query.addBindValue(place_id)
        if not query.exec():
            print("Delete place error: ", query.lastError().text())
            return False
        print("Delete place success. Id: ", query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    
    def select_location(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM location")
        return query
    def select_location_by_any(self, location_id, x, y, z, location_barcode, place_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM location WHERE location_id = ? OR x = ? OR y = ? OR z = ? OR location_barcode = ? OR place_id = ?")
        query.addBindValue(location_id)
        query.addBindValue(x)
        query.addBindValue(y)
        query.addBindValue(z)
        query.addBindValue(location_barcode)
        query.addBindValue(place_id)
        query.exec()
        return query
    def select_location_by_id(self, location_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM location WHERE id = ?")
        query.addBindValue(location_id)
        query.exec()
        return query
    def insert_location(self, location_id, x, y, z, location_barcode, place_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO location (location_id, x, y, z, location_barcode, place_id) VALUES (?, ?, ?, ?, ?, ?)")
        query.addBindValue(location_id)
        query.addBindValue(x)
        query.addBindValue(y)
        query.addBindValue(z)
        query.addBindValue(location_barcode)
        query.addBindValue(place_id)
        if not query.exec():
            print("Insert location error: ", query.lastError().text())
            return False
        return True
    def update_location(self, location_id, x, y, z, location_barcode, place_id):
        query = QSqlQuery()
        query.prepare("UPDATE location SET location_id = ?, x = ?, y = ?, z = ?, location_barcode = ?, place_id = ? WHERE id = ?")
        query.addBindValue(location_id)
        query.addBindValue(x)
        query.addBindValue(y)
        query.addBindValue(z)
        query.addBindValue(location_barcode)
        query.addBindValue(place_id)
        query.addBindValue(location_id)
        if not query.exec():
            print("Update location error: ", query.lastError().text())
            return False
        return True
    def delete_location(self, location_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM location WHERE id = ?")
        query.addBindValue(location_id)
        if not query.exec():
            print("Delete location error: ", query.lastError().text())
            return False
        return True
    
    def select_usergroup(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM usergroup")
        return query
    def select_usergroup_by_any(self, group_id, name, access_level):
        query = QSqlQuery()
        query.prepare("SELECT * FROM usergroup WHERE group_id = ? OR name = ? OR access_level = ?")
        query.addBindValue(group_id)
        query.addBindValue(name)
        query.addBindValue(access_level)
        query.exec()
        return query
    def select_usergroup_by_id(self, group_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM usergroup WHERE id = ?")
        query.addBindValue(group_id)
        query.exec()
        return query
    def insert_usergroup(self, name, access_level):
        query = QSqlQuery()
        query.prepare("INSERT INTO usergroup (name, access_level) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(access_level)
        if not query.exec():
            print("Insert usergroup error: ", query.lastError().text())
            return False
        return True
    def update_usergroup(self, group_id, name, access_level):
        query = QSqlQuery()
        query.prepare("UPDATE usergroup SET group_id = ?, name = ?, access_level = ? WHERE id = ?")
        query.addBindValue(group_id)
        query.addBindValue(name)
        query.addBindValue(access_level)
        query.addBindValue(group_id)
        if not query.exec():
            print("Update usergroup error: ", query.lastError().text())
            return False
        return True
    def delete_usergroup(self, group_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM usergroup WHERE id = ?")
        query.addBindValue(group_id)
        if not query.exec():
            print("Delete usergroup error: ", query.lastError().text())
            return False
        return True
    
    def select_users(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM users")
        return query
    def select_users_by_any(self, user_id, username, password, group_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE user_id = ? OR username = ? OR password = ? OR group_id = ?")
        query.addBindValue(user_id)
        query.addBindValue(username)
        query.addBindValue(password)
        query.addBindValue(group_id)
        query.exec()
        return query
    def select_users_by_id(self, user_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE id = ?")
        query.addBindValue(user_id)
        query.exec()
        return query
    def insert_users(self, email, password, group_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO users (email, password, group_id) VALUES (?, ?, ?, ?)")
        query.addBindValue(email)
        query.addBindValue(password)
        query.addBindValue(group_id)
        if not query.exec():
            print("Insert users error: ", query.lastError().text())
            return False
        return True
    def update_users(self, user_id, username, password, group_id):
        query = QSqlQuery()
        query.prepare("UPDATE users SET user_id = ?, username = ?, password = ?, group_id = ? WHERE id = ?")
        query.addBindValue(user_id)
        query.addBindValue(username)
        query.addBindValue(password)
        query.addBindValue(group_id)
        query.addBindValue(user_id)
        if not query.exec():
            print("Update users error: ", query.lastError().text())
            return False
        return True
    def delete_users(self, user_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM users WHERE id = ?")
        query.addBindValue(user_id)
        if not query.exec():
            print("Delete users error: ", query.lastError().text())
            return False
        return True
    
    def select_category(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM category")
        return query
    def select_category_by_any(self, category_id, name, description, place_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM category WHERE category_id = ? OR name = ? OR description = ? OR place_id = ?")
        query.addBindValue(category_id)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(place_id)
        query.exec()
        return query
    def select_category_by_id(self, category_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM category WHERE category_id = ?")
        query.addBindValue(category_id)
        query.exec()
        return query
    def insert_category(self, name, description, place_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO category (name, description, place_id) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(place_id)
        if not query.exec():
            print("Insert category error: ", query.lastError().text())
            return False
        return True
    def update_category(self, category_id, name, description, place_id):
        query = QSqlQuery()
        query.prepare("UPDATE category SET name = ?, description = ?, place_id = ? WHERE category_id = ?")
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(place_id)
        query.addBindValue(category_id)
        if not query.exec():
            print("Update category error: ", query.lastError().text())
            return False
        return True
    def delete_category(self, category_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM category WHERE category_id = ?")
        query.addBindValue(category_id)
        if not query.exec():
            print("Delete category error: ", query.lastError().text())
            return False
        return True
    
    def select_subcategory(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM subcategory")
        return query
    def select_subcategory_by_any(self, subcategory_id, category_id, name, description, location_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM subcategory WHERE subcategory_id = ? OR category_id = ? OR name = ? OR description = ? OR location_id = ?")
        query.addBindValue(subcategory_id)
        query.addBindValue(category_id)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(location_id)
        query.exec()
        return query
    def select_subcategory_by_id(self, subcategory_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM subcategory WHERE subcategory_id = ?")
        query.addBindValue(subcategory_id)
        query.exec()
        return query
    def insert_subcategory(self, category_id, name, description, location_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO subcategory (category_id, name, description, location_id) VALUES (?, ?, ?, ?)")
        query.addBindValue(category_id)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(location_id)
        if not query.exec():
            print("Insert subcategory error: ", query.lastError().text())
            return False
        return True
    def update_subcategory(self, subcategory_id, category_id, name, description, location_id):
        query = QSqlQuery()
        query.prepare("UPDATE subcategory SET category_id = ?, name = ?, description = ?, location_id = ? WHERE subcategory_id = ?")
        query.addBindValue(category_id)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(location_id)
        query.addBindValue(subcategory_id)
        if not query.exec():
            print("Update subcategory error: ", query.lastError().text())
            return False
        return True
    def delete_subcategory(self, subcategory_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM subcategory WHERE subcategory_id = ?")
        query.addBindValue(subcategory_id)
        if not query.exec():
            print("Delete subcategory error: ", query.lastError().text())
            return False
        return True
    
    def select_clients(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM clients")
        return query
    def select_clients_by_any(self, id, firstname, lastname, conpany, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("SELECT * FROM clients WHERE id = ? OR firstname = ? OR lastname = ? OR conpany = ? OR email = ? OR phone = ? OR address = ? OR post_code = ? OR note = ?")
        query.addBindValue(id)
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(conpany)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        query.exec()
        return query
    def select_clients_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM clients WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_clients(self, firstname, lastname, conpany, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("INSERT INTO clients (firstname, lastname, conpany, email, phone, address, post_code, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(conpany)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        if not query.exec():
            print("Insert clients error: ", query.lastError().text())
            return False
        return True
    def update_clients(self, id, firstname, lastname, conpany, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("UPDATE clients SET firstname = ?, lastname = ?, conpany = ?, email = ?, phone = ?, address = ?, post_code = ?, note = ? WHERE id = ?")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(conpany)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        query.addBindValue(id)
        if not query.exec():
            print("Update clients error: ", query.lastError().text())
            return False
        return True
    def delete_clients(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM clients WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete clients error: ", query.lastError().text())
            return False
        return True
    
    def select_employee(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM employee")
        return query
    def select_employee_by_any(self, id, firstname, lastname, job_title, phone, address, post_code, user_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM employee WHERE id = ? OR firstname = ? OR lastname = ? OR job_title = ? OR phone = ? OR address = ? OR post_code = ? OR user_id = ?")
        query.addBindValue(id)
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(job_title)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(user_id)
        query.exec()
        return query
    def select_employee_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM employee WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_employee(self, firstname, lastname, job_title, phone, address, post_code, user_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO employee (firstname, lastname, job_title, phone, address, post_code, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(job_title)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(user_id)
        if not query.exec():
            print("Insert employee error: ", query.lastError().text())
            return False
        return True
    def update_employee(self, id, firstname, lastname, job_title, phone, address, post_code, user_id):
        query = QSqlQuery()
        query.prepare("UPDATE employee SET firstname = ?, lastname = ?, job_title = ?, phone = ?, address = ?, post_code = ?, user_id = ? WHERE id = ?")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(job_title)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(user_id)
        query.addBindValue(id)
        if not query.exec():
            print("Update employee error: ", query.lastError().text())
            return False
        return True
    def delete_employee(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM employee WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete employee error: ", query.lastError().text())
            return False
        return True
    
    def select_supplier(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM supplier")
        return query
    def select_supplier_by_any(self, id, company, contact_name, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("SELECT * FROM supplier WHERE id = ? OR company = ? OR contact_name = ? OR email = ? OR phone = ? OR address = ? OR post_code = ? OR note = ?")
        query.addBindValue(id)
        query.addBindValue(company)
        query.addBindValue(contact_name)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        query.exec()
        return query
    def select_supplier_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM supplier WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_supplier(self, company, contact_name, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("INSERT INTO supplier (company, contact_name, email, phone, address, post_code, note) VALUES (?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(company)
        query.addBindValue(contact_name)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        if not query.exec():
            print("Insert supplier error: ", query.lastError().text())
            return False
        return True
    def update_supplier(self, id, company, contact_name, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("UPDATE supplier SET company = ?, contact_name = ?, email = ?, phone = ?, address = ?, post_code = ?, note = ? WHERE id = ?")
        query.addBindValue(company)
        query.addBindValue(contact_name)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        query.addBindValue(id)
        if not query.exec():
            print("Update supplier error: ", query.lastError().text())
            return False
        return True
    def delete_supplier(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM supplier WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete supplier error: ", query.lastError().text())
            return False
        return True
    
    def select_product(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM product")
        return query
    def select_product_by_any(self, id, barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
        query = QSqlQuery()
        query.prepare("SELECT * FROM product WHERE id = ? OR barcode = ? OR name = ? OR description = ? OR subcategory_id = ? OR quanity = ? OR price = ? OR supplier_id = ? OR note = ?")
        query.addBindValue(id)
        query.addBindValue(barcode)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(subcategory_id)
        query.addBindValue(quanity)
        query.addBindValue(price)
        query.addBindValue(supplier_id)
        query.addBindValue(note)
        query.exec()
        return query
    def select_product_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM product WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_product(self, barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
        query = QSqlQuery()
        query.prepare("INSERT INTO product (barcode, name, description, subcategory_id, quanity, price, supplier_id, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(barcode)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(subcategory_id)
        query.addBindValue(quanity)
        query.addBindValue(price)
        query.addBindValue(supplier_id)
        query.addBindValue(note)
        if not query.exec():
            print("Insert product error: ", query.lastError().text())
            return False
        return True
    def update_product(self, id, barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
        query = QSqlQuery()
        query.prepare("UPDATE product SET barcode = ?, name = ?, description = ?, subcategory_id = ?, quanity = ?, price = ?, supplier_id = ?, note = ? WHERE id = ?")
        query.addBindValue(barcode)
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(subcategory_id)
        query.addBindValue(quanity)
        query.addBindValue(price)
        query.addBindValue(supplier_id)
        query.addBindValue(note)
        query.addBindValue(id)
        if not query.exec():
            print("Update product error: ", query.lastError().text())
            return False
        return True
    def delete_product(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM product WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete product error: ", query.lastError().text())
            return False
        return True
    
    def select_purchase(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM purchase")
        return query
    def select_purchase_by_any(self, id, product_id, quanity, purchase_date, supplier_id, employee_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM purchase WHERE id = ? OR product_id = ? OR quanity = ? OR purchase_date = ? OR supplier_id = ? OR employee_id = ?")
        query.addBindValue(id)
        query.addBindValue(product_id)
        query.addBindValue(quanity)
        query.addBindValue(purchase_date)
        query.addBindValue(supplier_id)
        query.addBindValue(employee_id)
        query.exec()
        return query
    def select_purchase_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM purchase WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_purchase(self, product_id, quanity, purchase_date, supplier_id, employee_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO purchase (product_id, quanity, purchase_date, supplier_id, employee_id) VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(product_id)
        query.addBindValue(quanity)
        query.addBindValue(purchase_date)
        query.addBindValue(supplier_id)
        query.addBindValue(employee_id)
        if not query.exec():
            print("Insert purchase error: ", query.lastError().text())
            return False
        return True
    def update_purchase(self, id, product_id, quanity, purchase_date, supplier_id, employee_id):
        query = QSqlQuery()
        query.prepare("UPDATE purchase SET product_id = ?, quanity = ?, purchase_date = ?, supplier_id = ?, employee_id = ? WHERE id = ?")
        query.addBindValue(product_id)
        query.addBindValue(quanity)
        query.addBindValue(purchase_date)
        query.addBindValue(supplier_id)
        query.addBindValue(employee_id)
        query.addBindValue(id)
        if not query.exec():
            print("Update purchase error: ", query.lastError().text())
            return False
        return True
    def delete_purchase(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM purchase WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete purchase error: ", query.lastError().text())
            return False
        return True
    
    def select_stock(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM stock")
        return query
    def select_stock_by_any(self, stock_id, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
        query = QSqlQuery()
        query.prepare("SELECT * FROM stock WHERE stock_id = ? OR product_id = ? OR category_id = ? OR subcategory_id = ? OR location_id = ? OR supplier_id = ? OR purchase_id = ? OR employee_id = ? OR quantity = ? OR cost_price = ? OR selling_price = ? OR barcode = ?")
        query.addBindValue(stock_id)
        query.addBindValue(product_id)
        query.addBindValue(category_id)
        query.addBindValue(subcategory_id)
        query.addBindValue(location_id)
        query.addBindValue(supplier_id)
        query.addBindValue(purchase_id)
        query.addBindValue(employee_id)
        query.addBindValue(quantity)
        query.addBindValue(cost_price)
        query.addBindValue(selling_price)
        query.addBindValue(barcode)
        query.exec()
        return query
    def select_stock_by_id(self, stock_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM stock WHERE stock_id = ?")
        query.addBindValue(stock_id)
        query.exec()
        return query
    def insert_stock(self, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
        query = QSqlQuery()
        query.prepare("INSERT INTO stock (product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(product_id)
        query.addBindValue(category_id)
        query.addBindValue(subcategory_id)
        query.addBindValue(location_id)
        query.addBindValue(supplier_id)
        query.addBindValue(purchase_id)
        query.addBindValue(employee_id)
        query.addBindValue(quantity)
        query.addBindValue(cost_price)
        query.addBindValue(selling_price)
        query.addBindValue(barcode)
        if not query.exec():
            print("Insert stock error: ", query.lastError().text())
            return False
        return True
    def update_stock(self, stock_id, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
        query = QSqlQuery()
        query.prepare("UPDATE stock SET product_id = ?, category_id = ?, subcategory_id = ?, location_id = ?, supplier_id = ?, purchase_id = ?, employee_id = ?, quantity = ?, cost_price = ?, selling_price = ?, barcode = ? WHERE stock_id = ?")
        query.addBindValue(product_id)
        query.addBindValue(category_id)
        query.addBindValue(subcategory_id)
        query.addBindValue(location_id)
        query.addBindValue(supplier_id)
        query.addBindValue(purchase_id)
        query.addBindValue(employee_id)
        query.addBindValue(quantity)
        query.addBindValue(cost_price)
        query.addBindValue(selling_price)
        query.addBindValue(barcode)
        query.addBindValue(stock_id)
        if not query.exec():
            print("Update stock error: ", query.lastError().text())
            return False
        return True
    def delete_stock(self, stock_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM stock WHERE stock_id = ?")
        query.addBindValue(stock_id)
        if not query.exec():
            print("Delete stock error: ", query.lastError().text())
            return False
        return True
    
    def select_sale(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM sale")
        return query
    def select_sale_by_any(self, id, product_id, quantity, sale_date, client_id, employee_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM sale WHERE id = ? OR product_id = ? OR quantity = ? OR sale_date = ? OR client_id = ? OR employee_id = ?")
        query.addBindValue(id)
        query.addBindValue(product_id)
        query.addBindValue(quantity)
        query.addBindValue(sale_date)
        query.addBindValue(client_id)
        query.addBindValue(employee_id)
        query.exec()
        return query
    def select_sale_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM sale WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def insert_sale(self, product_id, quantity, sale_date, client_id, employee_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO sale (product_id, quantity, sale_date, client_id, employee_id) VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(product_id)
        query.addBindValue(quantity)
        query.addBindValue(sale_date)
        query.addBindValue(client_id)
        query.addBindValue(employee_id)
        if not query.exec():
            print("Insert sale error: ", query.lastError().text())
            return False
        return True
    def update_sale(self, id, product_id, quantity, sale_date, client_id, employee_id):
        query = QSqlQuery()
        query.prepare("UPDATE sale SET product_id = ?, quantity = ?, sale_date = ?, client_id = ?, employee_id = ? WHERE id = ?")
        query.addBindValue(product_id)
        query.addBindValue(quantity)
        query.addBindValue(sale_date)
        query.addBindValue(client_id)
        query.addBindValue(employee_id)
        query.addBindValue(id)
        if not query.exec():
            print("Update sale error: ", query.lastError().text())
            return False
        return True
    def delete_sale(self, id):
        query = QSqlQuery()
        query.prepare("DELETE FROM sale WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete sale error: ", query.lastError().text())
            return False
        return True



# test insert_branch()

query = CRUD.branch_columns('branch')
print(query)