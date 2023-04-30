from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Inventory tab with actions (Product list, Stock list, Purchase list, Sale list, Search, Filter). Must be clicked from MainWindow menu to be shown.
class Inventory(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Inventory")
        self.gridLayout = QGridLayout()
        self.btnProductList = QPushButton("Product List")
        self.btnProductList.clicked.connect(self.product_list)
        self.btnStockList = QPushButton("Stock List")
        self.btnStockList.clicked.connect(self.stock_list)
        self.btnPurchaseList = QPushButton("Purchase List")
        self.btnPurchaseList.clicked.connect(self.purchase_list)
        self.btnSaleList = QPushButton("Sale List")
        self.btnSaleList.clicked.connect(self.sale_list)
        self.btnSearch = QPushButton("Search")
        self.btnSearch.clicked.connect(self.search)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnProductList, 0, 0)
        self.gridLayout.addWidget(self.btnStockList, 0, 1)
        self.gridLayout.addWidget(self.btnPurchaseList, 0, 2)
        self.gridLayout.addWidget(self.btnSaleList, 1, 0)
        self.gridLayout.addWidget(self.btnSearch, 1, 1)
        self.gridLayout.addWidget(self.btnFilter, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def product_list(self):
        pass

    def stock_list(self):
        pass

    def purchase_list(self):
        pass

    def sale_list(self):
        pass

    def search(self):
        pass

    def filter(self):
        pass