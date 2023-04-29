import os
import sys
# Walk through current directory and print all files and directories
# from db.CRUD import CRUD
# from db.settings import DB
from ui.Widgets import MainWidget

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                                QVBoxLayout, QGroupBox, QGridLayout, QPushButton,
                                QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem,
                                QHeaderView, QAbstractItemView, QComboBox, QFormLayout,
                                QLineEdit, QLabel, QDateEdit, QSpinBox, QCheckBox, QFileDialog,
                                QRadioButton, QButtonGroup, QStatusBar, QMenuBar, QMenu)
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QKeySequence, QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from PySide6.QtSql import QSqlDatabase
from db.CRUD import CRUD
from db.settings import DB

crud = CRUD()
db = DB()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Management System")
        self.setWindowIcon(QIcon('wms\icons\warehouse.png'))
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.statusBar().showMessage("Ready")
        self.setCentralWidget(MainWidget())
        self.create_menu(self.menuBar())  # Remove parentheses here
        self.show()

    # Create menu bar with menus and actions: File[Exit, Theme Settings, Open, Import, Export, Settings], Dashboard (will show some metrics etc. later will implement), Inventory[Product list, Stock list, Purchase list, Sale list], Locations[Branch list, Place list, Location list], Users, Clients[Add client, View Clients], Employees[Add Employee, View Employees], Suppliers[Add Supplier, View Suppliers], Reports[Generate reports, View Reports, Generate Plots, View Plots], Help[About, Help]
    def create_menu(self, menuBar):
        menuBar.addMenu(self.file_menu())
        menuBar.addMenu(self.dashboard_menu())
        # menuBar.addMenu(self.inventory_menu())
        # menuBar.addMenu(self.locations_menu())
        # menuBar.addMenu(self.users_menu())
        # menuBar.addMenu(self.clients_menu())
        # menuBar.addMenu(self.employees_menu())
        # menuBar.addMenu(self.suppliers_menu())
        # menuBar.addMenu(self.reports_menu())
        menuBar.addMenu(self.help_menu())
        return menuBar




    
    # File menu
    def file_menu(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction("&Exit", self.close, QKeySequence("Ctrl+Q"))
        self.fileMenu.addAction("&Theme Settings", self.theme_settings, QKeySequence("Ctrl+T"))
        self.fileMenu.addAction("&Open", self.open_file, QKeySequence("Ctrl+O"))
        self.fileMenu.addAction("&Import", self.import_file, QKeySequence("Ctrl+I"))
        self.fileMenu.addAction("&Export", self.export_file, QKeySequence("Ctrl+E"))
        self.fileMenu.addAction("&Settings", self.settings, QKeySequence("Ctrl+S"))
        return self.fileMenu
    
    # Dashboard menu
    def dashboard_menu(self):
        self.dashboardMenu = QMenu("&Dashboard", self)
        return self.dashboardMenu
    
    # Inventory menu
    def inventory_menu(self):
        self.inventoryMenu = QMenu("&Inventory", self)
        self.inventoryMenu.addAction("&Product list", self.product_list, QKeySequence("Ctrl+P"))
        self.inventoryMenu.addAction("&Stock list", self.stock_list, QKeySequence("Ctrl+K"))
        self.inventoryMenu.addAction("&Purchase list", self.purchase_list, QKeySequence("Ctrl+U"))
        self.inventoryMenu.addAction("&Sale list", self.sale_list, QKeySequence("Ctrl+L"))
        return self.inventoryMenu
    
    # Locations menu
    def locations_menu(self):
        self.locationsMenu = QMenu("&Locations", self)
        self.locationsMenu.addAction("&Branch list", self.branch_list, QKeySequence("Ctrl+B"))
        self.locationsMenu.addAction("&Place list", self.place_list, QKeySequence("Ctrl+A"))
        self.locationsMenu.addAction("&Location list", self.location_list, QKeySequence("Ctrl+L"))
        return self.locationsMenu
    
    # Users menu
    def users_menu(self):
        self.usersMenu = QMenu("&Users", self)
        self.usersMenu.addAction("&Add user", self.add_user, QKeySequence("Ctrl+U"))
        return self.usersMenu
    
    # Clients menu
    def clients_menu(self):
        self.clientsMenu = QMenu("&Clients", self)
        self.clientsMenu.addAction("&Add client", self.add_client, QKeySequence("Ctrl+C"))
        self.clientsMenu.addAction("&View clients", self.view_clients, QKeySequence("Ctrl+V"))
        return self.clientsMenu
    
    # Employees menu
    def employees_menu(self):
        self.employeesMenu = QMenu("&Employees", self)
        self.employeesMenu.addAction("&Add employee", self.add_employee, QKeySequence("Ctrl+E"))
        self.employeesMenu.addAction("&View employees", self.view_employees, QKeySequence("Ctrl+V"))
        return self.employeesMenu
    
    # Suppliers menu
    def suppliers_menu(self):
        self.suppliersMenu = QMenu("&Suppliers", self)
        self.suppliersMenu.addAction("&Add supplier", self.add_supplier, QKeySequence("Ctrl+S"))
        self.suppliersMenu.addAction("&View suppliers", self.view_suppliers, QKeySequence("Ctrl+V"))
        return self.suppliersMenu
    
    # Reports menu
    def reports_menu(self):
        self.reportsMenu = QMenu("&Reports", self)
        self.reportsMenu.addAction("&Generate reports", self.generate_reports, QKeySequence("Ctrl+G"))
        self.reportsMenu.addAction("&View reports", self.view_reports, QKeySequence("Ctrl+V"))
        self.reportsMenu.addAction("&Generate plots", self.generate_plots, QKeySequence("Ctrl+P"))
        self.reportsMenu.addAction("&View plots", self.view_plots, QKeySequence("Ctrl+V"))
        return self.reportsMenu
    
    # Help menu
    def help_menu(self):
        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction("&About", self.about, QKeySequence("Ctrl+A"))
        self.helpMenu.addAction("&Help", self.help, QKeySequence("Ctrl+H"))
        return self.helpMenu
    
    # About
    def about(self):
        print("About")
        pass

    # Help
    def help(self):
        print("Help")
        pass
    
    # Theme settings
    def theme_settings(self):
        print("Theme settings")
        pass

    # Open file
    def open_file(self):
        print("Open file")
        pass

    # Import file
    def import_file(self):
        print("Import file")
        pass
    
    # Export file
    def export_file(self):
        print("Export file")
        pass

    # Settings
    def settings(self):
        print("Settings")
        pass

    # Product list
    def product_list(self):
        print("Product list")
        pass

    # Stock list
    def stock_list(self):
        print("Stock list")
        pass

    # Purchase list
    def purchase_list(self):
        print("Purchase list")
        pass

    # Sale list
    def sale_list(self):
        print("Sale list")
        pass
    
    # Branch list
    def branch_list(self):
        print("Branch list")
        pass
    
    # Place list
    def place_list(self):
        print("Place list")
        pass

    # Location list
    def location_list(self):
        print("Location list")
        pass

    # Add user
    def add_user(self):
        print("Add user")
        pass

    # View users
    def view_users(self):
        print("View users")
        pass

    # Add client
    def add_client(self):
        print("Add client")
        pass

    # View clients
    def view_clients(self):
        print("View clients")
        pass

    # Add employee
    def add_employee(self):
        print("Add employee")
        pass

    # View employees
    def view_employees(self):
        print("View employees")
        pass

    # Add supplier
    def add_supplier(self):
        print("Add supplier")
        pass

    # View suppliers
    def view_suppliers(self):
        print("View suppliers")
        pass

    # Generate reports
    def generate_reports(self):
        print("Generate reports")
        pass

    # View reports
    def view_reports(self):
        print("View reports")
        pass

    # Generate plots
    def generate_plots(self):
        print("Generate plots")
        pass

    # View plots
    def view_plots(self):
        print("View plots")
        pass

    # About
    def about(self):
        # Show about dialog
        QMessageBox.about(self, "About", "Inventory Management System\n\nVersion: 1.0.0\n\nAuthor: Eimantas Kulbe ")

    # Help
    def help(self):
        # Show help dialog
        QMessageBox.about(self, "Help", "Help")

# # Main widget with tab widget
# class MainWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout()
#         self.tabs = QTabWidget()
#         self.tabs.addTab(Database(), "Database")
#         self.tabs.addTab(Users(), "Users")

#         self.layout.addWidget(self.tabs)
#         self.setLayout(self.layout)

# Database tab
class Database(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Database")
        self.gridLayout = QGridLayout()
        self.btnCreateTables = QPushButton("Create tables")
        self.btnCreateTables.clicked.connect(db.create_tables)
        self.btnVersionCheck = QPushButton("Version check")
        self.btnVersionCheck.clicked.connect(self.db_version_check)
        self.btnDisconnect = QPushButton("Disconnect")
        self.btnDisconnect.clicked.connect(db.disconnect)

        self.gridLayout.addWidget(self.btnCreateTables, 0, 0)
        self.gridLayout.addWidget(self.btnVersionCheck, 0, 1)
        self.gridLayout.addWidget(self.btnDisconnect, 0, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    @Slot()
    def db_version_check(self):
        # Info message box with version
        QMessageBox.information(self, "Version", "Database version: " + db.__version__())

# Users tab
class Users(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Users")
        self.gridLayout = QGridLayout()
        self.btnCreateUser = QPushButton("Create user")
        self.btnCreateUser.clicked.connect(self.create_user)
        self.btnReadUser = QPushButton("Read user")
        self.btnReadUser.clicked.connect(self.read_user)
        self.btnUpdateUser = QPushButton("Update user")
        self.btnUpdateUser.clicked.connect(self.update_user)
        self.btnDeleteUser = QPushButton("Delete user")
        self.btnDeleteUser.clicked.connect(self.delete_user)

        self.gridLayout.addWidget(self.btnCreateUser, 0, 0)
        self.gridLayout.addWidget(self.btnReadUser, 0, 1)
        self.gridLayout.addWidget(self.btnUpdateUser, 0, 2)
        self.gridLayout.addWidget(self.btnDeleteUser, 0, 3)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)

        self.setLayout(self.layout)

    @Slot()
    def create_user(self):
        # Message box for email input
        # Title, label, default text
        email, ok = QInputDialog.getText(self, "Create user", "Enter email:")
        if ok:
            # Message box for password input
            password, ok = QInputDialog.getText(self, "Create user", "Enter password:")
            if ok:
                # Message box for group_id input
                group_id, ok = QInputDialog.getText(self, "Create user", "Enter group_id:")
                return crud.create_users(email, password, group_id)
            
    @Slot()
    def read_user(self):
        # Open new window with table
        self.data = crud.read_users()

        self.window = QWidget()
        self.window.setWindowTitle("Users")
        self.window.setMinimumSize(800, 600)
        self.window.setMaximumSize(800, 600)

        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Users")
        self.gridLayout = QGridLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["id", "email", "password", "group_id"])
        self.table.setRowCount(self.data.size())
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.edit_selected_field)
        
        while self.data.next():
            self.table.setItem(self.data.at(), 0, QTableWidgetItem(str(self.data.value(0))))
            self.table.setItem(self.data.at(), 1, QTableWidgetItem(str(self.data.value(1))))
            self.table.setItem(self.data.at(), 2, QTableWidgetItem(str(self.data.value(2))))
            self.table.setItem(self.data.at(), 3, QTableWidgetItem(str(self.data.value(3))))

        self.gridLayout.addWidget(self.table)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.window.setLayout(self.layout)

        self.window.show()

    @Slot()
    def edit_selected_field(self):
        # Get selected row
        row = self.table.currentRow()
        # Get all columns
        self.table.editItem(self.table.item(row, 0))
        self.table.editItem(self.table.item(row, 1))
        self.table.editItem(self.table.item(row, 2))
        self.table.editItem(self.table.item(row, 3))

        # Save changes
        id = self.table.item(row, 0).text()
        email = self.table.item(row, 1).text()
        password = self.table.item(row, 2).text()
        group_id = self.table.item(row, 3).text()
        crud.update_users(id, email, password, group_id)

    


    @Slot()
    def update_user(self, id):
        id = QInputDialog.getInt(self, "Update user", "Enter id:")
        if id:
            # Message box for email input
            email, ok = QInputDialog.getText(self, "Update user", "Enter email:")
            if ok:
                # Message box for password input
                password, ok = QInputDialog.getText(self, "Update user", "Enter password:")
                if ok:
                    # Message box for group_id input
                    group_id, ok = QInputDialog.getText(self, "Update user", "Enter group_id:")
                    return crud.update_users(id, email, password, group_id)

    @Slot()
    def delete_user(self):
        id, status = QInputDialog.getInt(self, "Delete user", "Enter id:")
        print(id)
        if status:
            crud.delete_users(id)
            # Info message box
            QMessageBox.information(self, "Delete user", "User deleted with id: " + str(id))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

