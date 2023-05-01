from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLabel, QStatusBar
from PySide6.QtCore import Qt
from PySide6 import QtWebEngineWidgets
from db.settings import DB
from db.CRUD import CRUD
# Dashboard tab with actions (Add, Edit, Delete, Refresh, Search, Filter). Must be clicked from MainWindow menu to be shown.
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        # Show all available tabs as buttons in Dashboard tab. Products, Customers, Orders, etc.
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Dashboard")
        self.gridLayout = QGridLayout()
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)
        
        # Show https://github.com/redrum88/wms/
        self.github = QtWebEngineWidgets.QWebEngineView()
        self.github.load("https://kedevo.com/")
        self.layout.addWidget(self.github)
