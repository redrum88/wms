import os
import sys
# Walk through current directory and print all files and directories
from db.CRUD import CRUD
from db.settings import DB
from ui.MainWindow import MainWindow
from ui.Widgets.py import AllWidgets

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                                QVBoxLayout, QGroupBox, QGridLayout, QPushButton,
                                QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem,
                                QHeaderView, QAbstractItemView, QComboBox, QFormLayout,
                                QLineEdit, QLabel, QDateEdit, QSpinBox, QCheckBox, QFileDialog,
                                QRadioButton, QButtonGroup, QStatusBar, QMenuBar, QMenu)
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QKeySequence, QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from PySide6.QtSql import QSqlDatabase

# Users widget
class Users(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Users")
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
