from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Products tab with actions (Product list, Add Product, Search Product, Filter). Must be clicked from MainWindow menu to be shown.
class Products(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Products")
        self.gridLayout = QGridLayout()
        self.btnProductList = QPushButton("Product List")
        self.btnProductList.clicked.connect(self.product_list)
        self.btnAddProduct = QPushButton("Add Product")
        self.btnAddProduct.clicked.connect(self.add_product)
        self.btnSearchProduct = QPushButton("Search Product")
        self.btnSearchProduct.clicked.connect(self.search_product)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnProductList, 0, 0)
        self.gridLayout.addWidget(self.btnAddProduct, 0, 1)
        self.gridLayout.addWidget(self.btnSearchProduct, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def product_list(self):
        pass

    def add_product(self):
        pass

    def search_product(self):
        pass

    def filter(self):
        pass