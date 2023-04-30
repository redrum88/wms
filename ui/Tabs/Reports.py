from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Reports tab with actions (Report list, Add Report, Search Report, Filter, Generate reports, Generate plots, View Plots, Search Plots). Must be clicked from MainWindow menu to be shown.
class Reports(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Reports")
        self.gridLayout = QGridLayout()
        self.btnReportList = QPushButton("Report List")
        self.btnReportList.clicked.connect(self.report_list)
        self.btnAddReport = QPushButton("Add Report")
        self.btnAddReport.clicked.connect(self.add_report)
        self.btnSearchReport = QPushButton("Search Report")
        self.btnSearchReport.clicked.connect(self.search_report)
        self.btnFilter = QPushButton("Filter")
        self.btnFilter.clicked.connect(self.filter)
        self.btnGenerateReports = QPushButton("Generate Reports")
        self.btnGenerateReports.clicked.connect(self.generate_reports)
        self.btnGeneratePlots = QPushButton("Generate Plots")
        self.btnGeneratePlots.clicked.connect(self.generate_plots)
        self.btnViewPlots = QPushButton("View Plots")
        self.btnViewPlots.clicked.connect(self.view_plots)
        self.btnSearchPlots = QPushButton("Search Plots")
        self.btnSearchPlots.clicked.connect(self.search_plots)

        self.gridLayout.addWidget(self.btnReportList, 0, 0)
        self.gridLayout.addWidget(self.btnAddReport, 0, 1)
        self.gridLayout.addWidget(self.btnSearchReport, 0, 2)
        self.gridLayout.addWidget(self.btnFilter, 1, 0)
        self.gridLayout.addWidget(self.btnGenerateReports, 1, 1)
        self.gridLayout.addWidget(self.btnGeneratePlots, 1, 2)
        self.gridLayout.addWidget(self.btnViewPlots, 2, 0)
        self.gridLayout.addWidget(self.btnSearchPlots, 2, 1)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def report_list(self):
        pass

    def add_report(self):
        pass

    def search_report(self):
        pass

    def filter(self):
        pass

    def generate_reports(self):
        pass

    def generate_plots(self):
        pass

    def view_plots(self):
        pass

    def search_plots(self):
        pass