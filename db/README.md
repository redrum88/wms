# Implement **CRUD** (create, read, update, delete) 
functionality for each table in the database, including `Branch`, `Place`, `Location`, `UserGroup`, `Users`, `Category`, `SubCategory`, `Clients`, `Employee`, `Supplier`, `Product`, `Purchase`, `Stock`, and `Sale`.

1. Branch:
   * ✅Implement a function for adding a new branch to the database
        * `create_branch(branch_name, phone, address, post_code)`
   * ✅Implement a function for fetching all branches from the database and displaying them in the UI
        * `read_branch()`
        * `read_branch_by_id()`
        * `read_branch_by_any()`
        * `read_branch_id_last()`
   * ✅Implement a function for updating a branch in the database
        * `update_branch(branch_id, branch_name, phone, address, post_code)`
   * ✅Implement a function for deleting a branch from the database
        * `delete_branch(branch_id)`
        * `delete_branch_last()`

        
2. Place:
   * ✅Implement a function for adding a new place to the database
        * `create_place(place_name, place_barcode, description, branch_id)`
   * ✅Implement a function for fetching all places from the database and displaying them in the UI
        * `read_place()`
        * `read_place_by_any(column, value)`
        * `read_place_by_id(place_id)`
        * `read_place_id_last()`
   * ✅Implement a function for updating a place in the database
        * `update_place(place_id, place_name, place_barcode, description, branch_id)`
   * ✅Implement a function for deleting a place from the database
        * `delete_place(place_id)`
        * `delete_place_last()`

 * Location:
   * ✅ Implement a function for adding a new location to the database
        * `create_location(self, x, y, z, location_barcode, place_id)`
   * ✅ Implement a function for fetching all locations from the database and displaying them in the UI
        * `read_location(self)`
        * `read_location_by_any(self, column, value)`
        * `read_location_by_id(self, location_id)`
        * `read_location_id_last(self)`
   * ✅ Implement a function for updating a location in the database
        * `update_location(self, location_id, x, y, z, location_barcode, place_id)`
   * ✅ Implement a function for deleting a location from the database
        * `delete_location(self, location_id)`
        * `delete_location_last(self)`
 * UserGroup:
   * ✅ Implement a function for adding a new user group to the database
        * `create_usergroup(self, name, access_level)`
   * ✅ Implement a function for fetching all user groups from the database and displaying them in the UI
        * `read_usergroup(self)`
        * `read_usergroup_by_any(self, group_id, name, access_level)`
        * `read_usergroup_by_id(self, group_id)`
        * `read_usergroup_id_last(self)`
   * ✅ Implement a function for updating a user group in the database
        * `update_usergroup(self, group_id, name, access_level)`
   * ✅ Implement a function for deleting a user group from the database
        * `delete_usergroup(self, group_id)`
        * `delete_usergroup_last(self)`
 * Users:
   * Implement a function for adding a new user to the database
   * Implement a function for fetching all users from the database and displaying them in the UI
   * Implement a function for updating a user in the database
   * Implement a function for deleting a user from the database
 * Category:
   * Implement a function for adding a new category to the database
   * Implement a function for fetching all categories from the database and displaying them in the UI
   * Implement a function for updating a category in the database
   * Implement a function for deleting a category from the database
 * SubCategory:
   * Implement a function for adding a new subcategory to the database
   * Implement a function for fetching all subcategories from the database and displaying them in the UI
   * Implement a function for updating a subcategory in the database
   * Implement a function for deleting a subcategory from the database
 * Clients:
   * Implement functionality to create a new client.
   * Implement functionality to read client information by their ID.
   * Implement functionality to update client information by their ID.
   * Implement functionality to delete a client by their ID.
 * Employee:
   * Implement functionality to create a new employee.
   * Implement functionality to read employee information by their ID.
   * Implement functionality to update employee information by their ID.
   * Implement functionality to delete an employee by their ID.
 * Supplier:
   * Implement functionality to create a new supplier.
   * Implement functionality to read supplier information by their ID.
   * Implement functionality to update supplier information by their ID.
   * Implement functionality to delete a supplier by their ID.
 * Product:
   * Implement functionality to create a new product.
   * Implement functionality to read product information by its ID.
   * Implement functionality to update product information by its ID.
   * Implement functionality to delete a product by its ID.
 * Purchase:
   * Implement functionality to create a new purchase record.
   * Implement functionality to read purchase information by its ID.
   * Implement functionality to update purchase information by its ID.
   * Implement functionality to delete a purchase record by its ID.
 * Stock:
   * Implement functionality to create a new stock entry.
   * Implement functionality to read stock information by its ID.
   * Implement functionality to update stock information by its ID.
   * Implement functionality to delete a stock entry by its ID.
 * Sale:
   * Implement functionality to create a new sale record.
   * Implement functionality to read sale information by its ID.
   * Implement functionality to update sale information by its ID.
   * Implement functionality to delete a sale record by its ID.