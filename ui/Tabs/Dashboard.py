from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLabel, QStatusBar
from PySide6.QtCore import Qt
from db.settings import DB
from db.CRUD import CRUD
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
        self.crud = CRUD()
        version = self.db.execute("SELECT version();")
        while version.next():
            print("Connected to PostgreSQL " + version.value(0))
            self.setStatusTip("Connected to PostgreSQL " + version.value(0))
            db_version = version.value(0)
        # self.db.disconnect()

        # Get total labels
        total_tables_query = self.db.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")
        if total_tables_query.next():
            total_tables_result = total_tables_query.value(0)
            print("DB Tables:", total_tables_result)

        total_users_query = self.db.execute("SELECT COUNT(*) FROM users;")
        if total_users_query.next():
            total_users_result = total_users_query.value(0)
            print("Users:", total_users_result)
        
        # Set total labels in Vertical Layout box
        self.new_layout = QVBoxLayout()

        self.total_tables_label = QLabel("Total Tables: " + str(total_tables_result))
        self.total_users_label = QLabel("Total Users: " + str(total_users_result))
        self.database_version_label = QLabel("Database Server: " + str(db_version))
        self.crud_version_label = QLabel("CRUD Version: " + str(CRUD().__version__()))
        self.db_version_label = QLabel("DB Version: " + str(DB().__version__()))
        self.gridLayout.addWidget(self.total_tables_label, 2, 0, Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.total_users_label, 3, 0, Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.crud_version_label, 4, 0, Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.db_version_label, 5, 0, Qt.AlignmentFlag.AlignTop)
        self.gridLayout.addWidget(self.database_version_label, 6, 0, Qt.AlignmentFlag.AlignTop)
        self.new_layout.addLayout(self.gridLayout)
        self.setLayout(self.new_layout)




        




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