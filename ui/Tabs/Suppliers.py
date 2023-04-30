from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Suppliers tab with actions (Supplier list, Add Supplier, Search Supplier, Filter). Must be clicked from MainWindow menu to be shown.
class Suppliers(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Suppliers")
        self.gridLayout = QGridLayout()
        self.btnSupplierList = QPushButton("Supplier List")
        self.btnSupplierList.clicked.connect(self.supplier_list)
        self.btnAddSupplier = QPushButton("Add Supplier")
        self.btnAddSupplier.clicked.connect(self.add_supplier)
        self.btnSearchSupplier = QPushButton("Search Supplier")
        self.btnSearchSupplier.clicked.connect(self.search_supplier)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnSupplierList, 0, 0)
        self.gridLayout.addWidget(self.btnAddSupplier, 0, 1)
        self.gridLayout.addWidget(self.btnSearchSupplier, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def supplier_list(self):
        pass

    def add_supplier(self):
        pass

    def search_supplier(self):
        pass

    def filter(self):
        pass