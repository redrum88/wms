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


crud = CRUD()
db = DB()

# Main window with menu bar and status bar only
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Management System")
        self.setWindowIcon(QIcon('wms\icons\warehouse.png'))
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.statusBar().showMessage("Ready")
        self.setCentralWidget(MainWidget())
        self.show()

# Main widget with tab widget
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.addTab(Database(), "Database")
        self.tabs.addTab(Users(), "Users")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

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