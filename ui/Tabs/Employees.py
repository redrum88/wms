from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

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
