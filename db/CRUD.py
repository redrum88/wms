import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from settings import DB



class CRUD(object):
    def __init__(self):
        self.db = object

    def __version__(self):
        return "0.1.0"

    # Get columns
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
    # Default CRUD
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

    # Branch CRUD
    def create_branch(self, branch_name, phone, address, post_code):
        query = QSqlQuery()
        query.prepare("INSERT INTO branch (branch_name, phone, address, post_code) VALUES (?, ?, ?, ?)")
        query.addBindValue(branch_name)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        if not query.exec():
            print("Insert branch error: ", query.lastError().text())
            return False
        print(f"Insert branch success. Branch id: {query.lastInsertId()}")
        print(query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def read_branch(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM branch")
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        print(f"Total rows: {query.size()}")
        return query
    def read_branch_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM branch WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        print(f"Total rows: {query.size()}")
        return query
    def read_branch_by_id(self, branch_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM branch WHERE branch_id = ? ")
        query.addBindValue(branch_id)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def read_branch_id_last(self):
        print("Gettting last branch id...")
        query = QSqlQuery()
        query.exec("SELECT MAX(branch_id) FROM branch")
        query.next()
        branch_id = query.value(0)
        return branch_id    
    def update_branch(self, branch_id, branch_name, phone, address, post_code):
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
        print(f"Update branch success. Branch id: {branch_id}")
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
        print(f"Delete branch success. Branch id: {branch_id}")
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def delete_branch_last(self):
        print("Removing last branch...")
        query = QSqlQuery()
        self.last = self.read_branch_id_last()
        query.prepare("DELETE FROM branch WHERE branch_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete branch error: ", query.lastError().text())
            return False
        print(f"Delete last branch success. Branch id: {self.last}")
        print("-----------------------------")
        return True

    # Place CRUD
    def create_place(self, place_name, place_barcode, description, branch_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO place (place_name, place_barcode, description, branch_id) VALUES (?, ?, ?, ?)")
        query.addBindValue(place_name)
        query.addBindValue(place_barcode)
        query.addBindValue(description)
        query.addBindValue(branch_id)
        if not query.exec():
            print("Insert place error: ", query.lastError().text())
            return False
        print("Insert place success. Last insert id: ", query.lastInsertId())
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def read_place(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM place")
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        print(f"Total rows: {query.size()}")
        return query
    def read_place_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM place WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        print(f"Total rows: {query.size()}")
        return query
    def read_place_by_id(self, place_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM place WHERE place_id = ?")
        query.addBindValue(place_id)
        query.exec()
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        return query
    def read_place_id_last(self):
        print("Gettting last place id...")
        query = QSqlQuery()
        query.exec("SELECT MAX(place_id) FROM place")
        query.next()
        place_id = query.value(0)
        return place_id
    def update_place(self, place_id, place_name, place_barcode, description, branch_id):
        query = QSqlQuery()
        query.prepare("UPDATE place SET place_name = ?, place_barcode = ?, description = ?, branch_id = ? WHERE place_id = ?")
        query.addBindValue(place_name)
        query.addBindValue(place_barcode)
        query.addBindValue(description)
        query.addBindValue(branch_id)
        query.addBindValue(place_id)
        if not query.exec():
            print("Update place error: ", query.lastError().text())
            return False
        print("Update place success. Id: ", place_id)
        print(query.executedQuery())
        print(query.boundValues())
        return True
    def delete_place(self, place_id):
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
    def delete_place_last(self):
        print("Removing last place...")
        query = QSqlQuery()
        self.last = self.read_place_id_last()
        query.prepare("DELETE FROM place WHERE place_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete place error: ", query.lastError().text())
            return False
        print("Delete last place success. Id: ", self.last)
        print("-----------------------------")
        return True
    
    # Location CRUD
    def create_location(self, x, y, z, location_barcode, place_id):
        print("Creating location...")
        query = QSqlQuery()
        query.prepare("INSERT INTO location (x, y, z, location_barcode, place_id) VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(x)
        query.addBindValue(y)
        query.addBindValue(z)
        query.addBindValue(location_barcode)
        query.addBindValue(place_id)
        if not query.exec():
            print("Insert location error: ", query.lastError().text())
            return False
        print("Insert location success. Last insert id: ", query.lastInsertId())
        return True
    def read_location(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM location")
        print(query.lastError().text())
        print(query.executedQuery())
        print(query.boundValues())
        print(f"Total rows: {query.size()}")
        return query
    def read_location_by_any(self, column, value):
        print("Reading location...")
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM location WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print(query.lastError().text())
        return query
    def read_location_by_id(self, location_id):
        print("Reading location...")
        query = QSqlQuery()
        query.prepare("SELECT * FROM location WHERE id = ?")
        query.addBindValue(location_id)
        query.exec()
        if not query.exec():
            print("Read location error: ", query.lastError().text())
            return False
        print(f"X: {query.value(1)}")
        print(f"Y: {query.value(2)}")
        print(f"Z: {query.value(3)}")
        print(f"Location barcode: {query.value(4)}")
        print(f"Place id: {query.value(5)}")
        return query
    def read_location_id_last(self):
        print("Gettting last location id...")
        query = QSqlQuery()
        query.exec("SELECT MAX(location_id) FROM location")
        query.next()
        location_id = query.value(0)
        return location_id    
    def update_location(self, location_id, x, y, z, location_barcode, place_id):
        print("Updating location...")
        query = QSqlQuery()
        query.prepare("UPDATE location SET location_id = ?, x = ?, y = ?, z = ?, location_barcode = ?, place_id = ? WHERE location_id = ?")
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
        print("Update location success. Id: ", location_id)
        return True
    def delete_location(self, location_id):
        print("Deleting location...")
        query = QSqlQuery()
        query.prepare("DELETE FROM location WHERE location_id = ?")
        query.addBindValue(location_id)
        if not query.exec():
            print("Delete location error: ", query.lastError().text())
            return False
        print("Delete location success. Id: ", location_id)
        return True
    def delete_location_last(self):
        print("Removing last location...")
        query = QSqlQuery()
        self.last = self.read_location_id_last()
        query.prepare("DELETE FROM location WHERE location_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete location error: ", query.lastError().text())
            return False
        print("Delete last location success. Id: ", self.last)
        print("-----------------------------")
        return True

    # User Group CRUD
    def create_usergroup(self, name, access_level):
        query = QSqlQuery()
        query.prepare("INSERT INTO usergroup (name, access_level) VALUES (?, ?)")
        query.addBindValue(name)
        query.addBindValue(access_level)
        if not query.exec():
            print("Insert usergroup error: ", query.lastError().text())
            return False
        print("Insert usergroup success. Last insert id: ", query.lastInsertId())
        return True
    def read_usergroup(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM usergroup")
        return query
    def read_usergroup_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM usergroup WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        return query
    def read_usergroup_by_id(self, group_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM usergroup WHERE group_id = ?")
        query.addBindValue(group_id)
        query.exec()
        return query
    def read_usergroup_id_last(self):
        query = QSqlQuery()
        query.exec("SELECT MAX(group_id) FROM usergroup")
        query.next()
        group_id = query.value(0)
        return group_id
    def update_usergroup(self, group_id, name, access_level):
        query = QSqlQuery()
        query.prepare("UPDATE usergroup SET group_id = ?, name = ?, access_level = ? WHERE group_id = ?")
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
        query.prepare("DELETE FROM usergroup WHERE group_id = ?")
        query.addBindValue(group_id)
        if not query.exec():
            print("Delete usergroup error: ", query.lastError().text())
            return False
        return True
    def delete_usergroup_last(self):
        query = QSqlQuery()
        self.last = self.read_usergroup_id_last()
        query.prepare("DELETE FROM usergroup WHERE group_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete usergroup error: ", query.lastError().text())
            return False
        print("Delete last usergroup success. Id: ", self.last)
        return True
    
    # Users CRUD
    def read_users(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM users")
        return query
    def read_users_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM users WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        return query
    def read_users_by_id(self, user_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE user_id = ?")
        query.addBindValue(user_id)
        query.exec()
        return query
    def read_users_id_last(self):
        query = QSqlQuery()
        query.exec("SELECT MAX(user_id) FROM users")
        query.next()
        user_id = query.value(0)
        return user_id
    def create_users(self, email, password, group_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO users (email, password, group_id) VALUES (?, ?, ?)")
        query.addBindValue(email)
        query.addBindValue(password)
        query.addBindValue(group_id)
        if not query.exec():
            print("Insert users error: ", query.lastError().text())
            return False
        print("Insert users success. Last insert id: ", query.lastInsertId())
        return True
    def update_users(self, user_id, email, password, group_id):
        query = QSqlQuery()
        query.prepare("UPDATE users SET user_id = ?, email = ?, password = ?, group_id = ? WHERE user_id = ?")
        query.addBindValue(user_id)
        query.addBindValue(email)
        query.addBindValue(password)
        query.addBindValue(group_id)
        query.addBindValue(user_id)
        if not query.exec():
            print("Update users error: ", query.lastError().text())
            return False
        print("Update users success. Id: ", user_id)
        return True
    def delete_users(self, user_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM users WHERE user_id = ?")
        query.addBindValue(user_id)
        if not query.exec():
            print("Delete users error: ", query.lastError().text())
            return False
        return True
    def delete_users_last(self):
        query = QSqlQuery()
        self.last = self.read_users_id_last()
        query.prepare("DELETE FROM users WHERE user_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete users error: ", query.lastError().text())
            return False
        print("Delete last users success. Id: ", self.last)
        return True
    
    # Category CRUD
    def create_category(self, name, description=None, place_id=None):
        query = QSqlQuery()
        query.prepare("INSERT INTO category (name, description, place_id) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(description)
        query.addBindValue(place_id)
        if not query.exec():
            print("Insert category error: ", query.lastError().text())
            return False
        return True
    def read_category(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM category")
        print("Total categories: ", query.size())
        return query
    def read_category_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM category WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print("Total categories: ", query.size())
        return query
    def read_category_by_id(self, category_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM category WHERE category_id = ?")
        query.addBindValue(category_id)
        query.exec()
        return query
    def read_category_id_last(self):
        query = QSqlQuery()
        query.exec("SELECT MAX(category_id) FROM category")
        query.next()
        category_id = query.value(0)
        return category_id
    def update_category(self, category_id, name, description, place_id):
        query = QSqlQuery()
        query.prepare("UPDATE category SET category_id = ?, name = ?, description = ?, place_id = ? WHERE category_id = ?")
        query.addBindValue(category_id)
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
    def delete_category_last(self):
        query = QSqlQuery()
        self.last = self.read_category_id_last()
        query.prepare("DELETE FROM category WHERE category_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete category error: ", query.lastError().text())
            return False
        print("Delete last category success. Id: ", self.last)
        return True
    
    # Subcategory CRUD
    def read_subcategory(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM subcategory")
        return query
    def read_subcategory_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM subcategory WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print("From column: ", column, "Value: ", value)
        print("Total subcategories: ", query.size())
        return query
    def read_subcategory_by_id(self, subcategory_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM subcategory WHERE subcategory_id = ?")
        query.addBindValue(subcategory_id)
        query.exec()
        return query
    def read_subcategory_id_last(self):
        query = QSqlQuery()
        query.exec("SELECT MAX(subcategory_id) FROM subcategory")
        query.next()
        subcategory_id = query.value(0)
        return subcategory_id
    def create_subcategory(self, category_id, name, description, location_id):
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
    def delete_subcategory_last(self):
        query = QSqlQuery()
        self.last = self.read_subcategory_id_last()
        query.prepare("DELETE FROM subcategory WHERE subcategory_id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete subcategory error: ", query.lastError().text())
            return False
        print("Delete last subcategory success. Id: ", self.last)
        return True
    
    # Clients CRUD
    def create_clients(self, firstname, lastname, company, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("INSERT INTO clients (firstname, lastname, company, email, phone, address, post_code, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(company)
        query.addBindValue(email)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue(post_code)
        query.addBindValue(note)
        if not query.exec():
            print("Insert clients error: ", query.lastError().text())
            return False
        return True
    def read_clients(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM clients")
        return query
    def read_clients_by_any(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT * FROM clients WHERE {column} = ?")
        query.addBindValue(value)
        query.exec()
        print("From column: ", column, "Value: ", value)
        print("Total clients: ", query.size())
        return query
    def read_clients_by_id(self, id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM clients WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def read_clients_id_last(self):
        query = QSqlQuery()
        query.exec("SELECT MAX(id) FROM clients")
        query.next()
        id = query.value(0)
        return id
    def update_clients(self, id, firstname, lastname, company, email, phone, address, post_code, note):
        query = QSqlQuery()
        query.prepare("UPDATE clients SET firstname = ?, lastname = ?, company = ?, email = ?, phone = ?, address = ?, post_code = ?, note = ? WHERE id = ?")
        query.addBindValue(firstname)
        query.addBindValue(lastname)
        query.addBindValue(company)
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
    def delete_clients_last(self):
        query = QSqlQuery()
        self.last = self.read_clients_id_last()
        query.prepare("DELETE FROM clients WHERE id = ?")
        query.addBindValue(self.last)
        if not query.exec():
            print("Delete clients error: ", query.lastError().text())
            return False
        print("Delete last clients success. Id: ", self.last)
        return True
    
    # Employee CRUD
    def read_employee():
        query = QSqlQuery()
        query.exec("SELECT * FROM employee")
        return query
    def read_employee_by_any(id, firstname, lastname, job_title, phone, address, post_code, user_id):
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
    def read_employee_by_id(id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM employee WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def create_employee(firstname, lastname, job_title, phone, address, post_code, user_id):
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
    def update_employee(id, firstname, lastname, job_title, phone, address, post_code, user_id):
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
    def delete_employee(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM employee WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete employee error: ", query.lastError().text())
            return False
        return True
    
    # Supplier CRUD
    def read_supplier():
        query = QSqlQuery()
        query.exec("SELECT * FROM supplier")
        return query
    def read_supplier_by_any(id, company, contact_name, email, phone, address, post_code, note):
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
    def read_supplier_by_id(id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM supplier WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def create_supplier(company, contact_name, email, phone, address, post_code, note):
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
    def update_supplier(id, company, contact_name, email, phone, address, post_code, note):
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
    def delete_supplier(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM supplier WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete supplier error: ", query.lastError().text())
            return False
        return True
    
    # Product CRUD
    def read_product():
        query = QSqlQuery()
        query.exec("SELECT * FROM product")
        return query
    def read_product_by_any(id, barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
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
    def read_product_by_id(id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM product WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def create_product(barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
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
    def update_product(id, barcode, name, description, subcategory_id, quanity, price, supplier_id, note):
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
    def delete_product(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM product WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete product error: ", query.lastError().text())
            return False
        return True
    
    # Purchase CRUD
    def read_purchase():
        query = QSqlQuery()
        query.exec("SELECT * FROM purchase")
        return query
    def read_purchase_by_any(id, product_id, quanity, purchase_date, supplier_id, employee_id):
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
    def read_purchase_by_id(id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM purchase WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def create_purchase(product_id, quanity, purchase_date, supplier_id, employee_id):
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
    def update_purchase(id, product_id, quanity, purchase_date, supplier_id, employee_id):
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
    def delete_purchase(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM purchase WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete purchase error: ", query.lastError().text())
            return False
        return True
    
    # Stock CRUD
    def read_stock():
        query = QSqlQuery()
        query.exec("SELECT * FROM stock")
        return query
    def read_stock_by_any(stock_id, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
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
    def read_stock_by_id(stock_id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM stock WHERE stock_id = ?")
        query.addBindValue(stock_id)
        query.exec()
        return query
    def create_stock(product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
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
    def update_stock(stock_id, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode):
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
    def delete_stock(stock_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM stock WHERE stock_id = ?")
        query.addBindValue(stock_id)
        if not query.exec():
            print("Delete stock error: ", query.lastError().text())
            return False
        return True
    
    # Sale CRUD
    def read_sale():
        query = QSqlQuery()
        query.exec("SELECT * FROM sale")
        return query
    def read_sale_by_any(id, product_id, quantity, sale_date, client_id, employee_id):
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
    def read_sale_by_id(id):
        query = QSqlQuery()
        query.prepare("SELECT * FROM sale WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        return query
    def create_sale(product_id, quantity, sale_date, client_id, employee_id):
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
    def update_sale(id, product_id, quantity, sale_date, client_id, employee_id):
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
    def delete_sale(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM sale WHERE id = ?")
        query.addBindValue(id)
        if not query.exec():
            print("Delete sale error: ", query.lastError().text())
            return False
        return True

    
db = DB()
crud = CRUD()

#############################################
############# TEST CRUD #####################
#############################################

clients = crud.read_clients()
while clients.next():
    print(clients.value(0), clients.value(1), clients.value(2))
# crud.delete_clients_last()

# clients = crud.read_clients()
# while clients.next():
#     print(clients.value(1), clients.value(2))