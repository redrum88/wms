# Warehouse Management System (WMS)

WMS is a Warehouse Management System implemented in Python. The project has been organized into two main folders: `db` and `ui`, and a `README.md`, and `requirements.txt` file in the root directory.

# TODO:
1. Create a graphical user interface (**GUI**) using `PySide6` to display and interact with the data in your `PostgreSQL` database.
    * Install `PySide6` and other required libraries for **GUI** development (e.g., `PyQtGraph`, `NumPy`, `Pandas`, etc.).
    * Design the layout and interface of the **GUI** using `PySide6`'s designer tool or by coding the **UI** directly in Python.
    * Create a connection to the `PostgreSQL` database using `PySide6`'s `QtSql` module.
    * Write code to retrieve data from the database and display it in the GUI (e.g., using table widgets or custom graphical plots).
    * Implement **CRUD** functionality for each table in the database, including `Branch`, `Place`, `Location`, `UserGroup`, `Users`, `Category`, `SubCategory`, `Clients`, `Employee`, `Supplier`, `Product`, `Purchase`, `Stock`, and `Sale`.
    * Implement a search functionality to allow users to search for specific data in the database.
    * Implement user authentication and authorization to restrict access to certain features based on the user's access level.
    * Implement data validation to prevent users from entering invalid data into the database.
    * Implement data filtering and sorting functionality to allow users to filter and sort data based on specific criteria.
    * Implement data import and export functionality to allow users to import data from external sources and export data to external files.
    * Implement reporting functionality to generate reports based on the data in the database.
    * Implement transaction management to ensure that database operations are executed in a consistent and reliable manner.
    * Test and debug the **GUI** to ensure that it works correctly and reliably.
    * Optimize the **GUI** for performance and scalability to ensure that it can handle large amounts of data and users.
    * Document the **GUI**'s functionality and architecture to aid in maintenance and future development.

2. Implement **CRUD** (create, read, update, delete) functionality for each table in the database, including `Branch`, `Place`, `Location`, `UserGroup`, `Users`, `Category`, `SubCategory`, `Clients`, `Employee`, `Supplier`, `Product`, `Purchase`, `Stock`, and `Sale`.
  * Branch:
    * Implement a UI form for creating a new branch
    * Implement a function for adding a new branch to the database
    * Implement a UI form for viewing all branches in the database
    * Implement a function for fetching all branches from the database and displaying them in the UI
    * Implement a UI form for updating an existing branch
    * Implement a function for updating a branch in the database
    * Implement a UI form for deleting a branch
    * Implement a function for deleting a branch from the database
  * Place:
    * Implement a UI form for creating a new place
    * Implement a function for adding a new place to the database
    * Implement a UI form for viewing all places in the database
    * Implement a function for fetching all places from the database and displaying them in the UI
    * Implement a UI form for updating an existing place
    * Implement a function for updating a place in the database
    * Implement a UI form for deleting a place
    * Implement a function for deleting a place from the database
  * Location:
    * Implement a UI form for creating a new location
    * Implement a function for adding a new location to the database
    * Implement a UI form for viewing all locations in the database
    * Implement a function for fetching all locations from the database and displaying them in the UI
    * Implement a UI form for updating an existing location
    * Implement a function for updating a location in the database
    * Implement a UI form for deleting a location
    * Implement a function for deleting a location from the database
  * UserGroup:
    * Implement a UI form for creating a new user group
    * Implement a function for adding a new user group to the database
    * Implement a UI form for viewing all user groups in the database
    * Implement a function for fetching all user groups from the database and displaying them in the UI
    * Implement a UI form for updating an existing user group
    * Implement a function for updating a user group in the database
    * Implement a UI form for deleting a user group
    * Implement a function for deleting a user group from the database
  * Users:
    * Implement a UI form for creating a new user
    * Implement a function for adding a new user to the database
    * Implement a UI form for viewing all users in the database
    * Implement a function for fetching all users from the database and displaying them in the UI
    * Implement a UI form for updating an existing user
    * Implement a function for updating a user in the database
    * Implement a UI form for deleting a user
    * Implement a function for deleting a user from the database
  * Category:
    * Implement a UI form for creating a new category
    * Implement a function for adding a new category to the database
    * Implement a UI form for viewing all categories in the database
    * Implement a function for fetching all categories from the database and displaying them in the UI
    * Implement a UI form for updating an existing category
    * Implement a function for updating a category in the database
    * Implement a UI form for deleting a category
    * Implement a function for deleting a category from the database
  * SubCategory:
    * Implement a UI form for creating a new subcategory
    * Implement a function for adding a new subcategory to the database
    * Implement a UI form for viewing all subcategories in the database
    * Implement a function for fetching all subcategories from the database and displaying them in the UI
    * Implement a UI form for updating an existing subcategory
    * Implement a function for updating a subcategory in the database
    * Implement a UI form for deleting a subcategory
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
    
3. Implement a search functionality to allow users to search for specific data in the database.
    1. Identify the tables that will be searchable and the fields within each table that will be searchable.
    2. Determine the type of search functionality required (e.g. exact match, partial match, fuzzy search, etc.).
    3. Decide on the user interface for the search functionality (e.g. search bar, advanced search options, etc.).
    4. Implement the search functionality using SQL queries and programming language of your choice.
    5. Test the search functionality for accuracy and efficiency.
    6. Optimize the search functionality for performance, if necessary.
    7. Implement any necessary security measures to prevent unauthorized access to sensitive data.
    8. Add error handling and logging to identify any issues with the search functionality.
    9. Deploy the search functionality to a production environment.
    10. Provide documentation and training to users on how to use the search functionality.

4. Implement user authentication and authorization to restrict access to certain features based on the user's access level.
    * Define user roles: Identify the different roles that users can have in your system, such as admin, manager, employee, or customer.
    * Implement a user registration process: Allow users to create accounts with their personal information, email addresses, and passwords.
    * Implement a login process: Allow users to enter their email address and password to log in to the system.
    * Implement password reset functionality: Allow users to reset their password in case they forget it or need to change it.
    * Define access levels for each role: Define what features and data each role can access in the system. For example, an admin might be able to create, read, update, and delete all data, while a manager might only be able to read and update data for their team.
    * Implement access controls: Implement access controls to restrict access to certain features or data based on the user's role and access level. For example, if a user tries to delete a record that they do not have access to, they should receive an error message or be redirected to a different page.
    * Implement session management: Implement session management to track whether a user is currently logged in and whether they have the necessary permissions to access certain features or data.
    * Implement auditing and logging: Implement auditing and logging functionality to track user activity and identify any unauthorized access attempts or suspicious behavior.

5. Implement data validation to prevent users from entering invalid data into the database.
    * Identify the input fields in the application that require validation.
    * Determine the data types and formats that are acceptable for each field.
    * Decide on the validation rules for each field (e.g., minimum and maximum values, required fields, allowed characters, etc.).
    * Implement server-side validation to check the input data against the validation rules.
    * Implement client-side validation to provide immediate feedback to the user about invalid data.
    * Display error messages when validation fails to inform the user about the issue.
    * Add input sanitization to prevent malicious code injection.
    * Test the validation thoroughly to ensure that all data is properly validated and that no invalid data can be submitted to the database.
    * Update the validation rules as needed to address any new requirements or issues that arise.

6. Implement data filtering and sorting functionality to allow users to filter and sort data based on specific criteria.
    * Determine which tables and columns need to be filterable and sortable.
    * Implement filtering functionality by creating a search form where users can input specific search criteria and then querying the database to retrieve the relevant data.
    * Implement sorting functionality by creating clickable column headers that sort the data based on the clicked column. You can also provide options for ascending and descending sorting.
    * Add pagination to ensure that the data is displayed in manageable chunks and not all at once.
    * Test the filtering and sorting functionality with various scenarios to ensure that it works as expected.
    * Consider implementing caching to improve the performance of the filtering and sorting functionality.
    
7. Implement data import and export functionality to allow users to import data from external sources and export data to external files.
    * Identify the external data sources and file formats that need to be supported for data import and export.
    * Design the data import and export functionality, including the user interface for selecting files and the validation and error handling logic for imported data.
    * Implement the functionality for importing data from external sources, such as CSV files or Excel spreadsheets, into the appropriate database tables. Make sure to handle errors and data validation issues.
    * Implement the functionality for exporting data from the database to external files, such as CSV or Excel files. Make sure to handle large data sets and provide options for filtering and sorting data before exporting.
    * Test the data import and export functionality thoroughly, including edge cases and error handling scenarios.
    * Document the data import and export functionality, including user guides and technical documentation for future maintenance and updates.

8. Implement reporting functionality to generate reports based on the data in the database.
    * Identify the types of reports that need to be generated, such as sales reports, inventory reports, and financial reports.
    * Determine the data that needs to be included in each report.
    * Decide on the format of the reports, such as PDF, Excel, or HTML.
    * Design the layout of each report, including the headers, footers, and columns.
    * Implement the code to retrieve the data from the database and populate the report template.
    * Add options to filter and sort the data in the report.
    * Add options to export the report to different formats and print the report.
    * Test the reporting functionality thoroughly to ensure accuracy and completeness of the reports.

9. Implement transaction management to ensure that database operations are executed in a consistent and reliable manner.
    * Identify the database management system (DBMS) being used and the supported transaction isolation levels.
    * Determine the appropriate transaction isolation level for the application's needs.
    * Ensure that the DBMS is configured to support the desired transaction isolation level.
    * Design the transaction boundaries for the application, identifying where transactions should begin and end.
    * Use appropriate programming techniques to implement transactions, such as using try-catch blocks to catch and handle exceptions that may occur during transaction processing.
    * Implement commit and rollback operations within the application code to ensure that transactions are either fully committed or fully rolled back in the event of an error.
    * Test the application to ensure that transactions are being executed correctly and that data integrity is being maintained.
    * Monitor the application in production to ensure that transactions are being executed efficiently and that any issues are being addressed promptly.

10. Test and debug the system to ensure that it works correctly and reliably.
    * Create a test plan that outlines the objectives, scope, and procedures for testing the system.
    * Write test cases for each feature to be tested, including positive and negative scenarios.
    * Perform unit testing on each module of the system to ensure that individual components are working correctly.
    * Conduct integration testing to ensure that different modules of the system are working together as expected.
    * Perform system testing to ensure that the entire system is working correctly and meets the requirements.
    * Conduct user acceptance testing (UAT) with a small group of end-users to ensure that the system is user-friendly and meets their needs.
    * Use debugging tools to identify and fix any issues or errors in the system.
    * Perform regression testing after any changes or updates to ensure that existing features are still working correctly.
    * Document the test results and any issues or bugs found during testing.
    * Repeat the testing process as needed until all issues are resolved and the system is functioning correctly and reliably.

11. Optimize the system for performance and scalability to ensure that it can handle large amounts of data and users.
    * Identify potential performance bottlenecks in the system, such as slow queries, inefficient algorithms, or resource constraints.
    * Use caching mechanisms, such as in-memory caches or content delivery networks (CDNs), to reduce the number of requests to the database and improve response times.
    * Optimize database schema and indexing to improve query performance and reduce storage requirements.
    * Use load balancing and horizontal scaling techniques, such as clustering or sharding, to distribute the workload across multiple servers and improve system scalability.
    * Use asynchronous processing and message queues to offload resource-intensive tasks, such as image or video processing, to background workers and free up resources for other requests.
    * Implement monitoring and logging tools, such as application performance monitoring (APM) or log aggregators, to track system performance and identify issues before they become critical.
    * Test the system under realistic production conditions, such as high traffic, large datasets, or concurrent users, to ensure that it can handle the expected workload without degrading performance or crashing.
    * Continuously monitor and optimize the system over time to ensure that it remains performant and scalable as the data and user traffic grow.


12. Document the system's functionality and architecture to aid in maintenance and future development.
    * Create a high-level architecture diagram that shows the components and their relationships, such as the database, server, user interface, and external services.
    * Create detailed documentation for each component, including its purpose, input and output parameters, dependencies, and potential failure modes.
    * Create user manuals and guides that explain how to use the system's features and perform common tasks, such as creating new records, searching for data, and generating reports.
    * Document the database schema, including the tables, fields, and relationships between them. Provide clear explanations of the purpose of each table and how they are connected.
    * Create a glossary of technical terms and acronyms used throughout the documentation to ensure consistency and clarity.
    * Provide code documentation for any custom code or scripts used in the system, including explanations of the purpose of each function or method, input and output parameters, and potential side effects.
    * Include examples and sample code snippets to help developers and maintainers understand how to use the system's APIs and libraries.
    * Create a change log to track updates and changes to the system, including bug fixes, feature enhancements, and changes to the database schema or APIs.
    * Ensure that the documentation is easily accessible and searchable, such as by hosting it on a dedicated wiki or using a documentation tool like Read the Docs.
    * Encourage feedback from users and maintainers to continuously improve the documentation and ensure that it remains up-to-date and accurate.

## Installation

To install WMS, you will need to follow these steps:

1. Clone the repository: `git clone https://github.com/redrum88/wms.git`.
2. Navigate to the `wms` directory: `cd wms`.
3. Install the required dependencies: `pip install -r requirements.txt`.

## Usage

To use WMS, you will need to follow these steps:

1. Navigate to the `wms` directory: `cd wms`.
2. Run the `main.py` file: `python main.py`.

## DB

The `db` folder contains all the database-related files. It has subfolders such as `__init__.py`, `createdb.py`, `db.sql`, and `Manager.py`. 

`__init__.py` is used to initialize the folder as a module.

`createdb.py` is a script to create the database with tables and insert default rows into the tables.

`db.sql` is an example of a database creation script.

`Manager.py` contains the `DbManager` class which is responsible for handling all the database operations like insert, update, delete, and select data in tables. It uses PySide6.QtSql and other PySide6 modules for future UI for the Warehouse Management System.

## UI

The `ui` folder contains all the user interface components of the application. It has subfolders such as `Tabs`, `Windows`, and `assets`. 

`Tabs` folder contains all the individual tabs like Categories, Users, and so on. Each tab will contain specific functionalities related to that particular aspect of the warehouse management system. 

`Windows` folder contains all the individual windows files which will be opened from the `MainWindow.py` file in the `ui` folder. 

`assets` folder contains all the files in different folders like images, plots, and maps.

## Conclusion

WMS is a Warehouse Management System that provides a user-friendly interface to manage all the warehouse-related tasks. It is implemented in Python and uses PySide6.QtSql and other PySide6 modules for future UI for the Warehouse Management System.,
