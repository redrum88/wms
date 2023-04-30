from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# File menu tab with actions (Exit, Theme Settings, Open, Import, Export, Settings). Must be clicked from MainWindow menu to be shown.
class FileMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("File")
        self.gridLayout = QGridLayout()
        self.btnExit = QPushButton("Exit")
        self.btnExit.clicked.connect(self.exit)
        self.btnThemeSettings = QPushButton("Theme Settings")
        self.btnThemeSettings.clicked.connect(self.theme_settings)
        self.btnOpen = QPushButton("Open")
        self.btnOpen.clicked.connect(self.open)
        self.btnImport = QPushButton("Import")
        self.btnImport.clicked.connect(self.import_)
        self.btnExport = QPushButton("Export")
        self.btnExport.clicked.connect(self.export)
        self.btnSettings = QPushButton("Settings")
        self.btnSettings.clicked.connect(self.settings)

        self.gridLayout.addWidget(self.btnExit, 0, 0)
        self.gridLayout.addWidget(self.btnThemeSettings, 0, 1)
        self.gridLayout.addWidget(self.btnOpen, 0, 2)
        self.gridLayout.addWidget(self.btnImport, 1, 0)
        self.gridLayout.addWidget(self.btnExport, 1, 1)
        self.gridLayout.addWidget(self.btnSettings, 1, 2)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def exit(self):
        sys.exit()

    def theme_settings(self):
        pass

    def open(self):
        pass

    def import_(self):
        pass

    def export(self):
        pass

    def settings(self):
        pass