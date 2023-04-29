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
from ui.MainWindow import MainWindow

# Login window
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.crud = CRUD()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('wms\icons\warehouse.png'))
        self.setMinimumSize(300, 200)
        self.setMaximumSize(300, 200)
        self.setCentralWidget(self.login_widget())
        self.show()
        
    def login_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.txtUsername = QLineEdit()
        self.txtUsername.setPlaceholderText("Username")
        self.txtPassword = QLineEdit()
        self.txtPassword.setPlaceholderText("Password")
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButton("Login")
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister = QPushButton("Register")
        self.btnRegister.clicked.connect(self.register)
        layout.addWidget(self.txtUsername)
        layout.addWidget(self.txtPassword)
        layout.addWidget(self.btnLogin)
        layout.addWidget(self.btnRegister)
        widget.setLayout(layout)
        return widget
    
    def login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        if self.crud.login(username, password):
            QMessageBox.information(self, "Login", "Logged in")
            self.main = MainWindow()
            self.close()
        else:
            QMessageBox.warning(self, "Login", "Wrong username or password")



    @Slot()
    def register(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        if self.crud.create_users(username, password, 1):
            QMessageBox.information(self, "Register", "Registered")
        else:
            QMessageBox.warning(self, "Register", "Username already exists")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())