from PySide6.QtWidgets import QMenu, QAction, QMenuBar, QToolBar, QTabWidget
from PySide6.QtGui import QIcon, QKeySequence
from TABS import AllTabs

# Create menu bar with menus and actions to load tab to mainwindow: File[Exit, Theme Settings, Open, Import, Export, Settings], Dashboard (will show some metrics etc. later will implement), Inventory[Product list, Stock list, Purchase list, Sale list], Locations[Branch list, Place list, Location list], Users, Clients[Add client, View Clients], Employees[Add Employee, View Employees], Suppliers[Add Supplier, View Suppliers], Reports[Generate reports, View Reports, Generate Plots, View Plots], Help[About, Help]
class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.create_menu()
    
    def create_menu(self):
        self.addMenu(self.file_menu())
        self.addMenu(self.dashboard_menu())
        self.addMenu(self.inventory_menu())
        self.addMenu(self.locations_menu())
        self.addMenu(self.users_menu())
        self.addMenu(self.clients_menu())
        self.addMenu(self.employees_menu())
        self.addMenu(self.suppliers_menu())
        self.addMenu(self.reports_menu())
        self.addMenu(self.help_menu())
    
    # File menu
    def file_menu(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction("&Exit", self.parent.close, QKeySequence("Ctrl+Q"))
        self.fileMenu.addAction("&Theme Settings", self.parent.theme_settings, QKeySequence("Ctrl+T"))
        self.fileMenu.addAction("&Open", self.parent.open_file, QKeySequence("Ctrl+O"))
        self.fileMenu.addAction("&Import", self.parent.import_file, QKeySequence("Ctrl+I"))
        self.fileMenu.addAction("&Export", self.parent.export_file, QKeySequence("Ctrl+E"))
        self.fileMenu.addAction("&Settings", self.parent.settings, QKeySequence(""))
        return self.fileMenu
    
    # Dashboard menu. On click will show dashboard tab
    def dashboard_menu(self):
        self.dashboardMenu = QMenu("&Dashboard", self)
        self.dashboardMenu.addAction("&Dashboard", self.parent.dashboard, QKeySequence(""))
        return self.dashboardMenu
    
    # Inventory menu
    def inventory_menu(self):
        self.inventoryMenu = QMenu("&Inventory", self)
        self.inventoryMenu.addAction("&Product list", self.parent.product_list, QKeySequence(""))
        self.inventoryMenu.addAction("&Stock list", self.parent.stock_list, QKeySequence(""))
        self.inventoryMenu.addAction("&Purchase list", self.parent.purchase_list, QKeySequence(""))
        self.inventoryMenu.addAction("&Sale list", self.parent.sale_list, QKeySequence(""))
        return self.inventoryMenu
    
    # Locations menu
    def locations_menu(self):
        self.locationsMenu = QMenu("&Locations", self)
        self.locationsMenu.addAction("&Branch list", self.parent.branch_list, QKeySequence(""))
        self.locationsMenu.addAction("&Place list", self.parent.place_list, QKeySequence(""))
        self.locationsMenu.addAction("&Location list", self.parent.location_list, QKeySequence(""))
        return self.locations
    
    # Users menu
    def users_menu(self):
        self.usersMenu = QMenu("&Users", self)
        self.usersMenu.addAction("&Add user", self.parent.add_user, QKeySequence(""))
        self.usersMenu.addAction("&View users", self.parent.view_users, QKeySequence(""))
        return self.usersMenu
    
    # Clients menu
    def clients_menu(self):
        self.clientsMenu = QMenu("&Clients", self)
        self.clientsMenu.addAction("&Add client", self.parent.add_client, QKeySequence(""))
        self.clientsMenu.addAction("&View clients", self.parent.view_clients, QKeySequence(""))
        return self.clientsMenu
    
    # Employees menu
    def employees_menu(self):
        self.employeesMenu = QMenu("&Employees", self)
        self.employeesMenu.addAction("&Add employee", self.parent.add_employee, QKeySequence(""))
        self.employeesMenu.addAction("&View employees", self.parent.view_employees, QKeySequence(""))
        return self.employeesMenu
    
    # Suppliers menu
    def suppliers_menu(self):
        self.suppliersMenu = QMenu("&Suppliers", self)
        self.suppliersMenu.addAction("&Add supplier", self.parent.add_supplier, QKeySequence(""))
        self.suppliersMenu.addAction("&View suppliers", self.parent.view_suppliers, QKeySequence(""))
        return self.suppliersMenu
    
    # Reports menu
    def reports_menu(self):
        self.reportsMenu = QMenu("&Reports", self)
        self.reportsMenu.addAction("&Generate reports", self.parent.generate_reports, QKeySequence(""))
        self.reportsMenu.addAction("&View reports", self.parent.view_reports, QKeySequence(""))
        self.reportsMenu.addAction("&Generate plots", self.parent.generate_plots, QKeySequence(""))
        self.reportsMenu.addAction("&View plots", self.parent.view_plots, QKeySequence(""))
        return self.reportsMenu
    
    # Help menu
    def help_menu(self):
        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction("&About", self.parent.about, QKeySequence(""))
        self.helpMenu.addAction("&Help", self.parent.help, QKeySequence(""))
        return self.helpMenu
    
    # Toolbar
    def toolbar(self):
        self.toolbar = QToolBar()
        self.toolbar.addAction(QIcon("icons/exit.png"), "Exit", self.parent.close)
        self.toolbar.addAction(QIcon("icons/theme.png"), "Theme Settings", self.parent.theme_settings)
        self.toolbar.addAction(QIcon("icons/open.png"), "Open", self.parent.open_file)
        self.toolbar.addAction(QIcon("icons/import.png"), "Import", self.parent.import_file)
        self.toolbar.addAction(QIcon("icons/export.png"), "Export", self.parent.export_file)
        self.toolbar.addAction(QIcon("icons/settings.png"), "Settings", self.parent.settings)
        self.toolbar.addAction(QIcon("icons/dashboard.png"), "Dashboard", self.parent.dashboard)
        self.toolbar.addAction(QIcon("icons/product.png"), "Product list", self.parent.product_list)
        self.toolbar.addAction(QIcon("icons/stock.png"), "Stock list", self.parent.stock_list)
        self.toolbar.addAction(QIcon("icons/purchase.png"), "Purchase list", self.parent.purchase_list)
        self.toolbar.addAction(QIcon("icons/sale.png"), "Sale list", self.parent.sale_list)
        self.toolbar.addAction(QIcon("icons/branch.png"), "Branch list", self.parent.branch_list)
        self.toolbar.addAction(QIcon("icons/place.png"), "Place list", self.parent.place_list)
        self.toolbar.addAction(QIcon("icons/location.png"), "Location list", self.parent.location_list)
        self.toolbar.addAction(QIcon("icons/user.png"), "Add user", self.parent.add_user)
        self.toolbar.addAction(QIcon("icons/user.png"), "View users", self.parent.view_users)
        self.toolbar.addAction(QIcon("icons/client.png"), "Add client", self.parent.add_client)
        self.toolbar.addAction(QIcon("icons/client.png"), "View clients", self.parent.view_clients)
        self.toolbar.addAction(QIcon("icons/employee.png"), "Add employee", self.parent.add_employee)
        self.toolbar.addAction(QIcon("icons/employee.png"), "View employees", self.parent.view_employees)
        self.toolbar.addAction(QIcon("icons/supplier.png"), "Add supplier", self.parent.add_supplier)
        self.toolbar.addAction(QIcon("icons/supplier.png"), "View suppliers", self.parent.view_suppliers)
        self.toolbar.addAction(QIcon("icons/reports.png"), "Generate reports", self.parent.generate_reports)
        self.toolbar.addAction(QIcon("icons/reports.png"), "View reports", self.parent.view_reports)
        self.toolbar.addAction(QIcon("icons/plots.png"), "Generate plots", self.parent.generate_plots)
        self.toolbar.addAction(QIcon("icons/plots.png"), "View plots", self.parent.view_plots)
        self.toolbar.addAction(QIcon("icons/about.png"), "About", self.parent.about)
        self.toolbar.addAction(QIcon("icons/help.png"), "Help", self.parent.help)
        return self.toolbar
    
    # Statusbar will show User email logged in and once hover over menu item, it will show the description of the menu item
    def statusbar(self):
        self.statusbar = QStatusBar()
        self.statusbar.showMessage("User: " + self.parent.user_email)
        self.statusbar.setStyleSheet("background-color: #ffffff; color: #000000")
        return self.statusbar