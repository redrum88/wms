from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Locations tab with actions (branch_list, place_list, location_list, Add[Branch, Place, List], Search[Branch, Place, List], Filter). Must be clicked from MainWindow menu to be shown.
class Locations(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Locations")
        self.gridLayout = QGridLayout()
        self.btnBranchList = QPushButton("Branch List")
        self.btnBranchList.clicked.connect(self.branch_list)
        self.btnPlaceList = QPushButton("Place List")
        self.btnPlaceList.clicked.connect(self.place_list)
        self.btnLocationList = QPushButton("Location List")
        self.btnLocationList.clicked.connect(self.location_list)
        self.btnAddBranch = QPushButton("Add Branch")
        self.btnAddBranch.clicked.connect(self.add_branch)
        self.btnAddPlace = QPushButton("Add Place")
        self.btnAddPlace.clicked.connect(self.add_place)
        self.btnAddLocation = QPushButton("Add Location")
        self.btnAddLocation.clicked.connect(self.add_location)
        self.btnSearchBranch = QPushButton("Search Branch")
        self.btnSearchBranch.clicked.connect(self.search_branch)
        self.btnSearchPlace = QPushButton("Search Place")
        self.btnSearchPlace.clicked.connect(self.search_place)
        self.btnSearchLocation = QPushButton("Search Location")
        self.btnSearchLocation.clicked.connect(self.search_location)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)

        self.gridLayout.addWidget(self.btnBranchList, 0, 0)
        self.gridLayout.addWidget(self.btnPlaceList, 0, 1)
        self.gridLayout.addWidget(self.btnLocationList, 0, 2)
        self.gridLayout.addWidget(self.btnAddBranch, 1, 0)
        self.gridLayout.addWidget(self.btnAddPlace, 1, 1)
        self.gridLayout.addWidget(self.btnAddLocation, 1, 2)
        self.gridLayout.addWidget(self.btnSearchBranch, 2, 0)
        self.gridLayout.addWidget(self.btnSearchPlace, 2, 1)
        self.gridLayout.addWidget(self.btnSearchLocation, 2, 2)
        self.gridLayout.addWidget(self.btnFilter, 3, 0)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def branch_list(self):
        pass

    def place_list(self):
        pass

    def location_list(self):
        pass

    def add_branch(self):
        pass

    def add_place(self):
        pass

    def add_location(self):
        pass

    def search_branch(self):
        pass

    def search_place(self):
        pass

    def search_location(self):
        pass

    def filter(self):
        pass