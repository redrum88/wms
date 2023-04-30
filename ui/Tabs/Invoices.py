from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Invoices tab with actions (Invoice list, Add Invoice, Search Invoice, Filter). Must be clicked from MainWindow menu to be shown.
class Invoices(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Invoices")
        self.gridLayout = QGridLayout()
        self.btnInvoiceList = QPushButton("Invoice List")
        self.btnInvoiceList.clicked.connect(self.invoice_list)
        self.btnAddInvoice = QPushButton("Add Invoice")
        self.btnAddInvoice.clicked.connect(self.add_invoice)
        self.btnSearchInvoice = QPushButton("Search Invoice")
        self.btnSearchInvoice.clicked.connect(self.search_invoice)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnInvoiceList, 0, 0)
        self.gridLayout.addWidget(self.btnAddInvoice, 0, 1)
        self.gridLayout.addWidget(self.btnSearchInvoice, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def invoice_list(self):
        pass

    def add_invoice(self):
        pass

    def search_invoice(self):
        pass

    def filter(self):
        pass