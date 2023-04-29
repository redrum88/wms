import os
import sys
# Walk through current directory and print all files and directories
from db.CRUD import CRUD
from db.settings import DB
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                                QVBoxLayout, QGroupBox, QGridLayout, QPushButton,
                                QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem,
                                QHeaderView, QAbstractItemView, QComboBox, QFormLayout,
                                QLineEdit, QLabel, QDateEdit, QSpinBox, QCheckBox, QFileDialog,
                                QRadioButton, QButtonGroup, QStatusBar, QMenuBar, QMenu)
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QKeySequence, QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from PySide6.QtSql import QSqlDatabase

# This is Widgets.py, is a file that contains all widgets used in the application.
# It imports all widgets from the Widgets folder.
# This class will be imported to MainWindow.py and used in the MainWidget class.


# Main window with menu bar and status bar only
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Management System")
        self.setWindowIcon(QIcon('wms\icons\warehouse.png'))
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.setCentralWidget(MainWidget())
        self.statusBar().showMessage("Ready")
        self.show()

# Main widget will show Tabs specified to MenuBar actions which have (File, Dashboard, Inventory, Locations, Users, Clients, Employees, Suppliers, Reports, Help)
# Those will be imported from the Widgets folder.
# Tabs will be shown in the MainWidget class once the user clicks on the MenuBar action.

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.addTab(FileMenu(), "File")
        self.tabs.addTab(Dashboard(), "Dashboard")
        self.tabs.addTab(Inventory(), "Inventory")
        self.tabs.addTab(Locations(), "Locations")
        self.tabs.addTab(Users(), "Users")
        self.tabs.addTab(Clients(), "Clients")
        self.tabs.addTab(Employees(), "Employees")
        self.tabs.addTab(Suppliers(), "Suppliers")
        self.tabs.addTab(Reports(), "Reports")
        self.tabs.addTab(Help(), "Help")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

# File menu tab with actions (Exit, Theme Settings, Open, Import, Export, Settings). Must be clicked from MainWindow menu to be shown.
class FileMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("File")
        self.gridLayout = QGridLayout()
        self.btnExit = QPushButton("Exit")
        self.btnExit.clicked.connect(self.exit)
        self.btnThemeSettings = QPushButton("Theme Settings")
        self.btnThemeSettings.clicked.connect(self.theme_settings)
        self.btnOpen = QPushButton("Open")
        self.btnOpen.clicked.connect(self.open)
        self.btnImport = QPushButton("Import")
        self.btnImport.clicked.connect(self.import_)
        self.btnExport = QPushButton("Export")
        self.btnExport.clicked.connect(self.export)
        self.btnSettings = QPushButton("Settings")
        self.btnSettings.clicked.connect(self.settings)

        self.gridLayout.addWidget(self.btnExit, 0, 0)
        self.gridLayout.addWidget(self.btnThemeSettings, 0, 1)
        self.gridLayout.addWidget(self.btnOpen, 0, 2)
        self.gridLayout.addWidget(self.btnImport, 1, 0)
        self.gridLayout.addWidget(self.btnExport, 1, 1)
        self.gridLayout.addWidget(self.btnSettings, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def exit(self):
        sys.exit()

    def theme_settings(self):
        pass

    def open(self):
        pass

    def import_(self):
        pass

    def export(self):
        pass

    def settings(self):
        pass

# Dashboard tab with actions (Add, Edit, Delete, Refresh, Search, Filter). Must be clicked from MainWindow menu to be shown.
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Dashboard")
        self.gridLayout = QGridLayout()
        self.btnAdd = QPushButton("Add")
        self.btnAdd.clicked.connect(self.add)
        self.btnEdit = QPushButton("Edit")
        self.btnEdit.clicked.connect(self.edit)
        self.btnDelete = QPushButton("Delete")
        self.btnDelete.clicked.connect(self.delete)
        self.btnRefresh = QPushButton("Refresh")
        self.btnRefresh.clicked.connect(self.refresh)
        self.btnSearch = QPushButton("Search")
        self.btnSearch.clicked.connect(self.search)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnAdd, 0, 0)
        self.gridLayout.addWidget(self.btnEdit, 0, 1)
        self.gridLayout.addWidget(self.btnDelete, 0, 2)
        self.gridLayout.addWidget(self.btnRefresh, 1, 0)
        self.gridLayout.addWidget(self.btnSearch, 1, 1)
        self.gridLayout.addWidget(self.btnFilter, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def refresh(self):
        pass

    def search(self):
        pass

    def filter(self):
        pass

# Inventory tab with actions (Product list, Stock list, Purchase list, Sale list, Search, Filter). Must be clicked from MainWindow menu to be shown.
class Inventory(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Inventory")
        self.gridLayout = QGridLayout()
        self.btnProductList = QPushButton("Product List")
        self.btnProductList.clicked.connect(self.product_list)
        self.btnStockList = QPushButton("Stock List")
        self.btnStockList.clicked.connect(self.stock_list)
        self.btnPurchaseList = QPushButton("Purchase List")
        self.btnPurchaseList.clicked.connect(self.purchase_list)
        self.btnSaleList = QPushButton("Sale List")
        self.btnSaleList.clicked.connect(self.sale_list)
        self.btnSearch = QPushButton("Search")
        self.btnSearch.clicked.connect(self.search)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnProductList, 0, 0)
        self.gridLayout.addWidget(self.btnStockList, 0, 1)
        self.gridLayout.addWidget(self.btnPurchaseList, 0, 2)
        self.gridLayout.addWidget(self.btnSaleList, 1, 0)
        self.gridLayout.addWidget(self.btnSearch, 1, 1)
        self.gridLayout.addWidget(self.btnFilter, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def product_list(self):
        pass

    def stock_list(self):
        pass

    def purchase_list(self):
        pass

    def sale_list(self):
        pass

    def search(self):
        pass

    def filter(self):
        pass

# Locations tab with actions (branch_list, place_list, location_list, Add[Branch, Place, List], Search[Branch, Place, List], Filter). Must be clicked from MainWindow menu to be shown.
class Locations(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Locations")
        self.gridLayout = QGridLayout()
        self.btnBranchList = QPushButton("Branch List")
        self.btnBranchList.clicked.connect(self.branch_list)
        self.btnPlaceList = QPushButton("Place List")
        self.btnPlaceList.clicked.connect(self.place_list)
        self.btnLocationList = QPushButton("Location List")
        self.btnLocationList.clicked.connect(self.location_list)
        self.btnAddBranch = QPushButton("Add Branch")
        self.btnAddBranch.clicked.connect(self.add_branch)
        self.btnAddPlace = QPushButton("Add Place")
        self.btnAddPlace.clicked.connect(self.add_place)
        self.btnAddLocation = QPushButton("Add Location")
        self.btnAddLocation.clicked.connect(self.add_location)
        self.btnSearchBranch = QPushButton("Search Branch")
        self.btnSearchBranch.clicked.connect(self.search_branch)
        self.btnSearchPlace = QPushButton("Search Place")
        self.btnSearchPlace.clicked.connect(self.search_place)
        self.btnSearchLocation = QPushButton("Search Location")
        self.btnSearchLocation.clicked.connect(self.search_location)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnBranchList, 0, 0)
        self.gridLayout.addWidget(self.btnPlaceList, 0, 1)
        self.gridLayout.addWidget(self.btnLocationList, 0, 2)
        self.gridLayout.addWidget(self.btnAddBranch, 1, 0)
        self.gridLayout.addWidget(self.btnAddPlace, 1, 1)
        self.gridLayout.addWidget(self.btnAddLocation, 1, 2)
        self.gridLayout.addWidget(self.btnSearchBranch, 2, 0)
        self.gridLayout.addWidget(self.btnSearchPlace, 2, 1)
        self.gridLayout.addWidget(self.btnSearchLocation, 2, 2)
        self.gridLayout.addWidget(self.btnFilter, 3, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def branch_list(self):
        pass

    def place_list(self):
        pass

    def location_list(self):
        pass

    def add_branch(self):
        pass

    def add_place(self):
        pass

    def add_location(self):
        pass

    def search_branch(self):
        pass

    def search_place(self):
        pass

    def search_location(self):
        pass

    def filter(self):
        pass

# Users tab with actions (User & Group list, Add[User, User Group], Search[User, User Group], Filter). Must be clicked from MainWindow menu to be shown.
class Users(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Users")
        self.gridLayout = QGridLayout()
        self.btnUserGroupList = QPushButton("User & Group List")
        self.btnUserGroupList.clicked.connect(self.user_group_list)
        self.btnAddUser = QPushButton("Add User")
        self.btnAddUser.clicked.connect(self.add_user)
        self.btnAddUserGroup = QPushButton("Add User Group")
        self.btnAddUserGroup.clicked.connect(self.add_user_group)
        self.btnSearchUser = QPushButton("Search User")
        self.btnSearchUser.clicked.connect(self.search_user)
        self.btnSearchUserGroup = QPushButton("Search User Group")
        self.btnSearchUserGroup.clicked.connect(self.search_user_group)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnUserGroupList, 0, 0)
        self.gridLayout.addWidget(self.btnAddUser, 0, 1)
        self.gridLayout.addWidget(self.btnAddUserGroup, 0, 2)
        self.gridLayout.addWidget(self.btnSearchUser, 1, 0)
        self.gridLayout.addWidget(self.btnSearchUserGroup, 1, 1)
        self.gridLayout.addWidget(self.btnFilter, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def user_group_list(self):
        pass

    def add_user(self):
        pass

    def add_user_group(self):
        pass

    def search_user(self):
        pass

    def search_user_group(self):
        pass

    def filter(self):
        pass

# Clients tab with actions (Client list, Add Client, Search Client, Filter). Must be clicked from MainWindow menu to be shown.
class Clients(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Clients")
        self.gridLayout = QGridLayout()
        self.btnClientList = QPushButton("Client List")
        self.btnClientList.clicked.connect(self.client_list)
        self.btnAddClient = QPushButton("Add Client")
        self.btnAddClient.clicked.connect(self.add_client)
        self.btnSearchClient = QPushButton("Search Client")
        self.btnSearchClient.clicked.connect(self.search_client)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnClientList, 0, 0)
        self.gridLayout.addWidget(self.btnAddClient, 0, 1)
        self.gridLayout.addWidget(self.btnSearchClient, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def client_list(self):
        pass

    def add_client(self):
        pass

    def search_client(self):
        pass

    def filter(self):
        pass

# Employees tab with actions (Employee list, Add Employee, Search Employee, Filter). Must be clicked from MainWindow menu to be shown.
class Employees(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Employees")
        self.gridLayout = QGridLayout()
        self.btnEmployeeList = QPushButton("Employee List")
        self.btnEmployeeList.clicked.connect(self.employee_list)
        self.btnAddEmployee = QPushButton("Add Employee")
        self.btnAddEmployee.clicked.connect(self.add_employee)
        self.btnSearchEmployee = QPushButton("Search Employee")
        self.btnSearchEmployee.clicked.connect(self.search_employee)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnEmployeeList, 0, 0)
        self.gridLayout.addWidget(self.btnAddEmployee, 0, 1)
        self.gridLayout.addWidget(self.btnSearchEmployee, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def employee_list(self):
        pass

    def add_employee(self):
        pass

    def search_employee(self):
        pass

    def filter(self):
        pass

# Suppliers tab with actions (Supplier list, Add Supplier, Search Supplier, Filter). Must be clicked from MainWindow menu to be shown.
class Suppliers(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Suppliers")
        self.gridLayout = QGridLayout()
        self.btnSupplierList = QPushButton("Supplier List")
        self.btnSupplierList.clicked.connect(self.supplier_list)
        self.btnAddSupplier = QPushButton("Add Supplier")
        self.btnAddSupplier.clicked.connect(self.add_supplier)
        self.btnSearchSupplier = QPushButton("Search Supplier")
        self.btnSearchSupplier.clicked.connect(self.search_supplier)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnSupplierList, 0, 0)
        self.gridLayout.addWidget(self.btnAddSupplier, 0, 1)
        self.gridLayout.addWidget(self.btnSearchSupplier, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def supplier_list(self):
        pass

    def add_supplier(self):
        pass

    def search_supplier(self):
        pass

    def filter(self):
        pass

# Products tab with actions (Product list, Add Product, Search Product, Filter). Must be clicked from MainWindow menu to be shown.
class Products(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Products")
        self.gridLayout = QGridLayout()
        self.btnProductList = QPushButton("Product List")
        self.btnProductList.clicked.connect(self.product_list)
        self.btnAddProduct = QPushButton("Add Product")
        self.btnAddProduct.clicked.connect(self.add_product)
        self.btnSearchProduct = QPushButton("Search Product")
        self.btnSearchProduct.clicked.connect(self.search_product)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnProductList, 0, 0)
        self.gridLayout.addWidget(self.btnAddProduct, 0, 1)
        self.gridLayout.addWidget(self.btnSearchProduct, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def product_list(self):
        pass

    def add_product(self):
        pass

    def search_product(self):
        pass

    def filter(self):
        pass

# Orders tab with actions (Order list, Add Order, Search Order, Filter). Must be clicked from MainWindow menu to be shown.
class Orders(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Orders")
        self.gridLayout = QGridLayout()
        self.btnOrderList = QPushButton("Order List")
        self.btnOrderList.clicked.connect(self.order_list)
        self.btnAddOrder = QPushButton("Add Order")
        self.btnAddOrder.clicked.connect(self.add_order)
        self.btnSearchOrder = QPushButton("Search Order")
        self.btnSearchOrder.clicked.connect(self.search_order)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnOrderList, 0, 0)
        self.gridLayout.addWidget(self.btnAddOrder, 0, 1)
        self.gridLayout.addWidget(self.btnSearchOrder, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def order_list(self):
        pass

    def add_order(self):
        pass

    def search_order(self):
        pass

    def filter(self):
        pass

# Invoices tab with actions (Invoice list, Add Invoice, Search Invoice, Filter). Must be clicked from MainWindow menu to be shown.
class Invoices(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Invoices")
        self.gridLayout = QGridLayout()
        self.btnInvoiceList = QPushButton("Invoice List")
        self.btnInvoiceList.clicked.connect(self.invoice_list)
        self.btnAddInvoice = QPushButton("Add Invoice")
        self.btnAddInvoice.clicked.connect(self.add_invoice)
        self.btnSearchInvoice = QPushButton("Search Invoice")
        self.btnSearchInvoice.clicked.connect(self.search_invoice)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnInvoiceList, 0, 0)
        self.gridLayout.addWidget(self.btnAddInvoice, 0, 1)
        self.gridLayout.addWidget(self.btnSearchInvoice, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def invoice_list(self):
        pass

    def add_invoice(self):
        pass

    def search_invoice(self):
        pass

    def filter(self):
        pass

# Reports tab with actions (Report list, Add Report, Search Report, Filter, Generate reports, Generate plots, View Plots, Search Plots). Must be clicked from MainWindow menu to be shown.
class Reports(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Reports")
        self.gridLayout = QGridLayout()
        self.btnReportList = QPushButton("Report List")
        self.btnReportList.clicked.connect(self.report_list)
        self.btnAddReport = QPushButton("Add Report")
        self.btnAddReport.clicked.connect(self.add_report)
        self.btnSearchReport = QPushButton("Search Report")
        self.btnSearchReport.clicked.connect(self.search_report)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)
        self.btnGenerateReports = QPushButton("Generate Reports")
        self.btnGenerateReports.clicked.connect(self.generate_reports)
        self.btnGeneratePlots = QPushButton("Generate Plots")
        self.btnGeneratePlots.clicked.connect(self.generate_plots)
        self.btnViewPlots = QPushButton("View Plots")
        self.btnViewPlots.clicked.connect(self.view_plots)
        self.btnSearchPlots = QPushButton("Search Plots")
        self.btnSearchPlots.clicked.connect(self.search_plots)

        self.gridLayout.addWidget(self.btnReportList, 0, 0)
        self.gridLayout.addWidget(self.btnAddReport, 0, 1)
        self.gridLayout.addWidget(self.btnSearchReport, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.gridLayout.addWidget(self.btnGenerateReports, 1, 1)
        self.gridLayout.addWidget(self.btnGeneratePlots, 1, 2)
        self.gridLayout.addWidget(self.btnViewPlots, 2, 0)
        self.gridLayout.addWidget(self.btnSearchPlots, 2, 1)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def report_list(self):
        pass

    def add_report(self):
        pass

    def search_report(self):
        pass

    def filter(self):
        pass

    def generate_reports(self):
        pass

    def generate_plots(self):
        pass

    def view_plots(self):
        pass

    def search_plots(self):
        pass

# Help tab with actions (Help, About). Must be clicked from MainWindow menu to be shown.
class Help(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Help")
        self.gridLayout = QGridLayout()
        self.btnHelp = QPushButton("Help")
        self.btnHelp.clicked.connect(self.help)
        self.btnAbout = QPushButton("About")
        self.btnAbout.clicked.connect(self.about)

        self.gridLayout.addWidget(self.btnHelp, 0, 0)
        self.gridLayout.addWidget(self.btnAbout, 0, 1)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def help(self):
        pass

    def about(self):
        pass