import PySide6
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSql import *
import sys
import os
from db import createdb
from db.settings import DB
from db.CRUD import CRUD


# Create window which have box with Database configuration settings (host, db, name, password)with saving details and buttons to create tables, connect, disconnect.
# Box on right side will have information about database version, total number of tables, total number of rows in each table.
class Database(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Database")
        self.gridLayout = QGridLayout()
        self.btnCreateTables = QPushButton("Create tables")
        self.btnCreateTables.clicked.connect(self.create_tables)
        self.btnVersionCheck = QPushButton("Version check")
        self.btnVersionCheck.clicked.connect(self.db_version_check)
        self.btnDisconnect = QPushButton("Disconnect")
        self.btnDisconnect.clicked.connect(self.disconnect)

        self.gridLayout.addWidget(self.btnCreateTables, 0, 0)
        self.gridLayout.addWidget(self.btnVersionCheck, 0, 1)
        self.gridLayout.addWidget(self.btnDisconnect, 0, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    @Slot()
    def create_tables(self):
        self.db.create_tables()
        QMessageBox.information(self, "Create tables", "Tables created")

    @Slot()
    def db_version_check(self):
        QMessageBox.information(self, "Version", "Database version: " + self.db.__version__())

    @Slot()
    def disconnect(self):
        self.db.disconnect()
        QMessageBox.information(self, "Disconnect", "Disconnected")


# Create window which have box with user details (name, surname, email, password) and buttons to create, read, update, delete user.
class Users(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.crud = CRUD()
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
        email, ok = QInputDialog.getText(self, "Email", "Enter email address")
        if ok:
            # Check if email is in database
            if self.db.check_user(email):
                QMessageBox.information(self, "Create user", "User already exists")
            else:
                # Message box for name input
                name, ok = QInputDialog.getText(self, "Name", "Enter name")
                if ok:
                    # Message box for surname input
                    surname, ok = QInputDialog.getText(self, "Surname", "Enter surname")
                    if ok:
                        # Message box for password input
                        password, ok = QInputDialog.getText(self, "Password", "Enter password")
                        if ok:
                            # Create user
                            self.db.create_user(email, name, surname, password)
                            QMessageBox.information(self, "Create user", "User created")

    @Slot()
    def read_user(self):
        # Message box for email input
        email, ok = QInputDialog.getText(self, "Email", "Enter email address")
        if ok:
            # Check if email is in database
            if self.crud.read_users_by_any("email", email):
                password, ok = QInputDialog.getText(self, "Password", "Enter password")
                if ok:
                    # Check if password is correct
                    if self.crud.read_users_by_any("email", email)[0][4] == password:
                        QMessageBox.information(self, "Read user", "User found")
                    else:
                        QMessageBox.information(self, "Read user", "User not found")
            else:
                QMessageBox.information(self, "Read user", "User not found")

    @Slot()
    