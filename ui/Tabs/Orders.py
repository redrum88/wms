from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Orders tab with actions (Order list, Add Order, Search Order, Filter). Must be clicked from MainWindow menu to be shown.
class Orders(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Orders")
        self.gridLayout = QGridLayout()
        self.btnOrderList = QPushButton("Order List")
        self.btnOrderList.clicked.connect(self.order_list)
        self.btnAddOrder = QPushButton("Add Order")
        self.btnAddOrder.clicked.connect(self.add_order)
        self.btnSearchOrder = QPushButton("Search Order")
        self.btnSearchOrder.clicked.connect(self.search_order)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnOrderList, 0, 0)
        self.gridLayout.addWidget(self.btnAddOrder, 0, 1)
        self.gridLayout.addWidget(self.btnSearchOrder, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def order_list(self):
        pass

    def add_order(self):
        pass

    def search_order(self):
        pass

    def filter(self):
        pass