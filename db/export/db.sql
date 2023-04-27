CREATE TABLE Branch (
  branch_id SERIAL PRIMARY KEY,
  branch_name VARCHAR(50) NOT NULL,
  phone VARCHAR(50) NOT NULL,
  address VARCHAR(100) NOT NULL,
  post_code VARCHAR(10) NOT NULL
);

CREATE TABLE Place (
  place_id SERIAL PRIMARY KEY,
  place_name VARCHAR(50) NOT NULL,
  place_barcode VARCHAR(50) NOT NULL,
  description TEXT,
  branch_id INTEGER NOT NULL,
  FOREIGN KEY (branch_id)
    REFERENCES Branch (branch_id)
);

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

CREATE TABLE UserGroup (
  group_id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  access_level INTEGER NOT NULL
);

CREATE TABLE Users (
  user_id SERIAL PRIMARY KEY,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  group_id INTEGER NOT NULL,
  FOREIGN KEY (group_id)
    REFERENCES UserGroup (group_id)
);

CREATE TABLE Category (
  category_id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  place_id INTEGER,
  FOREIGN KEY (place_id)
    REFERENCES Place (place_id)
);

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