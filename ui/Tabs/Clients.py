from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Clients tab with actions (Client list, Add Client, Search Client, Filter). Must be clicked from MainWindow menu to be shown.
class Clients(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Clients")
        self.gridLayout = QGridLayout()
        self.btnClientList = QPushButton("Client List")
        self.btnClientList.clicked.connect(self.client_list)
        self.btnAddClient = QPushButton("Add Client")
        self.btnAddClient.clicked.connect(self.add_client)
        self.btnSearchClient = QPushButton("Search Client")
        self.btnSearchClient.clicked.connect(self.search_client)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnClientList, 0, 0)
        self.gridLayout.addWidget(self.btnAddClient, 0, 1)
        self.gridLayout.addWidget(self.btnSearchClient, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def client_list(self):
        pass

    def add_client(self):
        pass

    def search_client(self):
        pass

    def filter(self):
        pass
