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
from ui.Tabs.About import About

from PySide6.QtWidgets import (QWidget, QTabWidget,
                                QVBoxLayout,QToolBar)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.tabs.setTabsClosable(True)
        # self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.setMovable(True)

        # Bold font for tabs
        font = self.tabs.font()
        font.setBold(True)
        self.tabs.setFont(font)

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
        self.about = About()

        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)


    def close_tab(self, index):
        self.tabs.removeTab(index)



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

    def show_about_tab(self):
        self.tabs.addTab(self.about, "About")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class MainToolbar(QToolBar):
    def __init__(self):
        super().__init__()
        self.setMovable(False)
        self.setFloatable(False)
        self = QToolBar()
        self.setMovable(False)
        self.setFloatable
        self.addAction("Dashboard", self.show_dashboard_tab)
        self.addAction("Users", self.show_users_tab)
        self.addAction("Clients", self.show_clients_tab)
        self.addAction("Employees", self.show_employees_tab)
        self.addAction("Suppliers", self.show_suppliers_tab)
        self.addAction("Products", self.show_products_tab)
        self.addAction("Inventory", self.show_inventory_tab)
        self.addAction("Locations", self.show_locations_tab)
        self.addAction("Orders", self.show_orders_tab)
        self.addAction("Invoices", self.show_invoices_tab)
        self.addAction("Reports", self.show_reports_tab)
        self.addAction("Help", self.show_help_tab)
        # Bold font for toolbar
        font = self.toolbar.font()
        font.setBold(True)
        self.toolbar.setFont(font)


    def close_tab(self, index):
        self.tabs.removeTab(index)



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