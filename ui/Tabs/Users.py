import os
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton


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