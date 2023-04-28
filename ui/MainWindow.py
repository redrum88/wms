# Autor: Eimantas aka REDRUM
# Date: 2023-04-23
# Version: 1.0.0 Initial version
# Description: This is a snippet for creating a main window with tabs and menu bar.
# Path: wms\ui\MainWindow.py

import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from PySide6.QtWidgets import (QAbstractItemView, QDataWidgetMapper,
    QHeaderView, QMainWindow, QMessageBox, QTabWidget, QTableView, QWidget, QVBoxLayout, QApplication)
from PySide6.QtGui import QKeySequence

from db.settings import DB
from db.CRUD import CRUD

class MainWindow(QMainWindow):
    """A window to show available tables in database. And a menu bar with actions."""

    def __init__(self):
        super().__init__()
        self.DB = DB()
        self.CRUD = CRUD()
        self.setWindowTitle("Warehouse Management System")
        self.resize(800, 600)
        self.create_menu()
        self.create_tabs()
        self.create_connections()
        self.statusBar().showMessage("Ready")

    def create_menu(self):
        """Create menu bar with actions. Create Database menu with self.DB commands"""
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.file_menu.addAction("&Exit", self.close,
            QKeySequence.Quit)
        self.database_menu = self.menu.addMenu("&Database")
        self.database_menu.addAction("&Create Tables", self.DB.create_tables)
        self.database_menu.addAction("&Disconnect", self.DB.disconnect)
        self.database_menu.addAction("&Connect", self.DB.__init__)

    def create_tabs(self):
        """Create Database tab with buttons for DB commands"""
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.create_database_tab()

    def create_database_tab(self):
        """Create Database tab with buttons for DB commands"""
        self.database_tab = QWidget()
        self.tabs.addTab(self.database_tab, "Database")
        self.database_tab_layout = QVBoxLayout()
        self.database_tab.setLayout(self.database_tab_layout)
        self.create_database_buttons()

    def create_database_buttons(self):
        """Create Database tab with buttons for DB commands"""
        self.database_tab_layout.addStretch()
        self.database_tab_layout.addStretch()

    def create_connections(self):
        """Create connections between signals and slots"""
        pass

    def closeEvent(self, event):
        """Close the window and exit the application."""
        self.DB.disconnect()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

