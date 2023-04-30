from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLabel, QStatusBar
from db.settings import DB
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
        # Show PostgreSQL database information in Dashboard tab
        self.db = DB()
        version = self.db.execute("SELECT version();")
        while version.next():
            print("Connected to PostgreSQL " + version.value(0))
            self.setStatusTip("Connected to PostgreSQL " + version.value(0))
        self.db.disconnect()





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