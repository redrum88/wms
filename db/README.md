# ⚒️ Implement **CRUD** (create, read, update, delete) 
*Implement **CRUD** (create, read, update, delete) functionality for each table in the database, including `Branch`, `Place`, `Location`, `UserGroup`, `Users`, `Category`, `SubCategory`, `Clients`, `Employee`, `Supplier`, `Product`, `Purchase`, `Stock`, and `Sale`.*

## Example usage:
```py
from db.CRUD import CRUD

crud = CRUD()
all_branch = crud.read_branch()
while all_branch.next():
    print(all_branch.value(0), all_branch.value(1), all_branch.value(2), all_branch.value(3), all_branch.value(4))

```
# --------------------
1. Branch:
   * Implement a function for adding a new branch to the database
        * `create_branch(branch_name, phone, address, post_code)` ✅
   * Implement a function for fetching all branches from the database and displaying them in the UI
        * `read_branch()` ✅
        * `read_branch_by_id()` ✅
        * `read_branch_by_any()` ✅
        * `read_branch_id_last()` ✅
   * Implement a function for updating a branch in the database
        * `update_branch(branch_id, branch_name, phone, address, post_code)` ✅
   * Implement a function for deleting a branch from the database
        * `delete_branch(branch_id)` ✅
        * `delete_branch_last()` ✅
 
2. Place:
   * Implement a function for adding a new place to the database
        * `create_place(place_name, place_barcode, description, branch_id)` ✅
   * Implement a function for fetching all places from the database and displaying them in the UI
        * `read_place()` ✅
        * `read_place_by_any(column, value)` ✅
        * `read_place_by_id(place_id)` ✅
        * `read_place_id_last()` ✅
   * Implement a function for updating a place in the database
        * `update_place(place_id, place_name, place_barcode, description, branch_id)` ✅
   * Implement a function for deleting a place from the database
        * `delete_place(place_id)` ✅
        * `delete_place_last()` ✅

 * Location:
   * Implement a function for adding a new location to the database
        * `create_location(self, x, y, z, location_barcode, place_id)` ✅
   * Implement a function for fetching all locations from the database and displaying them in the UI
        * `read_location(self)` ✅
        * `read_location_by_any(self, column, value)` ✅
        * `read_location_by_id(self, location_id)` ✅
        * `read_location_id_last(self)` ✅
   * Implement a function for updating a location in the database
        * `update_location(self, location_id, x, y, z, location_barcode, place_id)` ✅
   * Implement a function for deleting a location from the database
        * `delete_location(self, location_id)` ✅
        * `delete_location_last(self)` ✅
 
 * UserGroup:
   * Implement a function for adding a new user group to the database
        * `create_usergroup(self, name, access_level)` ✅
   * Implement a function for fetching all user groups from the database and displaying them in the UI
        * `read_usergroup(self)` ✅
        * `read_usergroup_by_any(self, column, value)` ✅
        * `read_usergroup_by_id(self, group_id)` ✅
        * `read_usergroup_id_last(self)` ✅
   * Implement a function for updating a user group in the database
        * `update_usergroup(self, group_id, name, access_level)` ✅
   * Implement a function for deleting a user group from the database
        * `delete_usergroup(self, group_id)` ✅
        * `delete_usergroup_last(self)` ✅
 * Users:
   * Implement a function for adding a new user to the database
        * `create_users(self, email, password, group_id)` ✅
   * Implement a function for fetching all users from the database and displaying them in the UI
        * `read_users(self)` ✅
        * `read_users_by_any(self, column, value)` ✅
        * `read_users_by_id(self, user_id)` ✅
        * `read_users_id_last(self)` ✅
   * Implement a function for updating a user in the database
        * `update_users(self, user_id, email, password, group_id)` ✅
   * Implement a function for deleting a user from the database
        * `delete_users(self, user_id)` ✅
        * `delete_users_last(self)` ✅
 * Category:
   * Implement a function for adding a new category to the database
        * `create_category(self, name, description=None, place_id=None)` ✅
   * Implement a function for fetching all categories from the database and displaying them in the UI
        * `read_category(self)` ✅
        * `read_category_by_any(self, column, value)` ✅
        * `read_category_by_id(self, category_id)` ✅
        * `read_category_id_last(self)` ✅
   * Implement a function for updating a category in the database
        * `update_category(self, category_id, name, description, place_id)` ✅
   * Implement a function for deleting a category from the database
        * `delete_category(self, category_id)` ✅
        * `delete_category_last(self)` ✅
        
 * SubCategory:
   * Implement a function for adding a new subcategory to the database
        * `create_subcategory(self, category_id, name, description, location_id)` ✅
   * Implement a function for fetching all subcategories from the database and displaying them in the UI
        * `read_subcategory(self)` ✅
        * `read_subcategory_by_any(self, column, value)` ✅
        * `read_subcategory_by_id(self, subcategory_id)` ✅
        * `read_subcategory_id_last(self)` ✅
   * Implement a function for updating a subcategory in the database
        * `update_subcategory(self, subcategory_id, category_id, name, description, location_id)` ✅
   * Implement a function for deleting a subcategory from the database
        * `delete_subcategory(self, subcategory_id)` ✅
        * `delete_subcategory_last(self)` ✅
 * Clients:
   * Implement functionality to create a new client.
        * `create_clients(self, firstname, lastname, company, email, phone, address, post_code, note)` ✅
   * Implement functionality to read client information by their ID.
        * `read_clients(self)` ✅
        * `read_clients_by_any(self, column, value)` ✅
        * `read_clients_by_id(self, id)` ✅
        * `read_clients_id_last(self)` ✅
   * Implement functionality to update client information by their ID.
        * `update_clients(self, id, firstname, lastname, company, email, phone, address, post_code, note)` ✅
   * Implement functionality to delete a client by their ID.
        * `delete_clients(self, id)` ✅
        * `delete_clients_last(self)` ✅
 * Employee:
   * Implement functionality to create a new employee.
        * `create_employee(self, firstname, lastname, job_title, phone, address, post_code, user_id)` ✅
   * Implement functionality to read employee information by their ID.
        * `read_employee(self)` ✅
        * `read_employee_by_any(self, column, value)` ✅
        * `read_employee_by_id(self, id)` ✅
        * `read_employee_id_last(self)` ✅
   * Implement functionality to update employee information by their ID.
        * `update_employee(self, id, firstname, lastname, job_title, phone, address, post_code, user_id)` ✅
   * Implement functionality to delete an employee by their ID.
        * `delete_employee(self, id)` ✅
        * `delete_employee_last(self)` ✅
 * Supplier:
   * Implement functionality to create a new supplier.
        * `create_supplier(self, company, contact_name, email, phone, address, post_code, note)` ✅
   * Implement functionality to read supplier information by their ID.
        * `read_supplier(self)` ✅
        * `read_supplier_by_any(self, column, value)` ✅
        * `read_supplier_by_id(self, id)` ✅
        * `read_supplier_id_last(self)` ✅
   * Implement functionality to update supplier information by their ID.
        * `update_supplier(self, id, company, contact_name, email, phone, address, post_code, note)` ✅
   * Implement functionality to delete a supplier by their ID.
        * `delete_supplier(self, id)` ✅
        * `delete_supplier_last(self)` ✅
 * Product:
   * Implement functionality to create a new product.
        * `create_product(self, barcode, name, description, subcategory_id, quanity, price, supplier_id, note)` ✅
   * Implement functionality to read product information by its ID.
        * `read_product(self)` ✅
        * `read_product_by_any(self, column, value)` ✅
        * `read_product_by_id(self, id)` ✅
        * `read_product_id_last(self)` ✅
   * Implement functionality to update product information by its ID.
        * `update_product(self, id, barcode, name, description, subcategory_id, quanity, price, supplier_id, note)` ✅
   * Implement functionality to delete a product by its ID.
        * `delete_product(self, id)` ✅
        * `delete_product_last(self)` ✅
 * Purchase:
   * Implement functionality to create a new purchase record.
        * `create_purchase(self, product_id, quanity, purchase_date, supplier_id, employee_id)` ✅
   * Implement functionality to read purchase information by its ID.
        * `read_purchase(self)` ✅
        * `read_purchase_by_any(self, column, value)` ✅
        * `read_purchase_by_id(self, id)` ✅
        * `read_purchase_id_last(self)` ✅
   * Implement functionality to update purchase information by its ID.
        * `update_purchase(self, id, product_id, quanity, purchase_date, supplier_id, employee_id)` ✅
   * Implement functionality to delete a purchase record by its ID.
        * `delete_purchase(self, id)` ✅
        * `delete_purchase_last(self)` ✅
 * Stock:
   * Implement functionality to create a new stock entry.
        * `create_stock(self, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode)` ✅
   * Implement functionality to read stock information by its ID.
        * `read_stock(self)` ✅
        * `read_stock_by_any(self, column, value)` ✅
        * `read_stock_by_id(self, stock_id)` ✅
        * `read_stock_id_last(self)` ✅
   * Implement functionality to update stock information by its ID.
        * `update_stock(self, stock_id, product_id, category_id, subcategory_id, location_id, supplier_id, purchase_id, employee_id, quantity, cost_price, selling_price, barcode)` ✅
   * Implement functionality to delete a stock entry by its ID.
        * `delete_stock(self, stock_id)` ✅
        * `delete_stock_last(self)` ✅
 * Sale:
   * Implement functionality to create a new sale record.
        * `create_sale(self, product_id, quantity, sale_date, client_id, employee_id)` ✅
   * Implement functionality to read sale information by its ID.
        * `read_sale(self)` ✅
        * `read_sale_by_any(self, column, value)` ✅
        * `read_sale_by_id(self, id)` ✅
        * `read_sale_id_last(self)` ✅
   * Implement functionality to update sale information by its ID.
        * `update_sale(self, id, product_id, quantity, sale_date, client_id, employee_id)` ✅
   * Implement functionality to delete a sale record by its ID.
        * `delete_sale(self, id)` ✅
        * `delete_sale_last(self)` ✅
