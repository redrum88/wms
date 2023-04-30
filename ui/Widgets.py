import os
import sys
# Walk through current directory and print all files and directories
from db.CRUD import CRUD
from db.settings import DB
from ui.Tabs.Dashboard import Dashboard
from ui.Tabs.Users import Users
from ui.Tabs.Clients import Clients
from ui.Tabs.Employees import Employees
from ui.Tabs.Suppliers import Suppliers
from ui.Tabs.Products import Products
from ui.Tabs.Inventory import Inventory
from ui.Tabs.Locations import Locations
from ui.Tabs.Orders import Orders
from ui.Tabs.Invoices import Invoices
from ui.Tabs.Reports import Reports
from ui.Tabs.FileMenu import FileMenu
from ui.Tabs.Help import Help

from PySide6.QtWidgets import (QWidget, QTabWidget,
                                QVBoxLayout)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        # Define tabs to be called from MainWindow menu and shown separately
        self.dashboard = Dashboard()
        self.users = Users()
        self.clients = Clients()
        self.employees = Employees()
        self.suppliers = Suppliers()
        self.products = Products()
        self.inventory = Inventory()
        self.locations = Locations()
        self.orders = Orders()
        self.invoices = Invoices()
        self.reports = Reports()
        self.filemenu = FileMenu()
        self.help = Help()
        # Add tabs to QTabWidget when in menu is clicked then tab is shown 
    
    def show_dashboard_tab(self):
        self.tabs.addTab(self.dashboard, "Dashboard")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_users_tab(self):
        self.tabs.addTab(self.users, "Users")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_clients_tab(self):
        self.tabs.addTab(self.clients, "Clients")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_employees_tab(self):
        self.tabs.addTab(self.employees, "Employees")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_suppliers_tab(self):
        self.tabs.addTab(self.suppliers, "Suppliers")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_products_tab(self):
        self.tabs.addTab(self.products, "Products")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_inventory_tab(self):
        self.tabs.addTab(self.inventory, "Inventory")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_locations_tab(self):
        self.tabs.addTab(self.locations, "Locations")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_orders_tab(self):
        self.tabs.addTab(self.orders, "Orders")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_invoices_tab(self):
        self.tabs.addTab(self.invoices, "Invoices")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_reports_tab(self):
        self.tabs.addTab(self.reports, "Reports")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_filemenu_tab(self):
        self.tabs.addTab(self.filemenu, "File Menu")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def show_help_tab(self):
        self.tabs.addTab(self.help, "Help")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

