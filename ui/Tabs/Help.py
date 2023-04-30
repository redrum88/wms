from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton

# Help tab with actions (Help, About). Must be clicked from MainWindow menu to be shown.
class Help(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.groupBox = QGroupBox("Help")
        self.gridLayout = QGridLayout()
        self.btnHelp = QPushButton("Help")
        self.btnHelp.clicked.connect(self.help)
        self.btnAbout = QPushButton("About")
        self.btnAbout.clicked.connect(self.about)

        self.gridLayout.addWidget(self.btnHelp, 0, 0)
        self.gridLayout.addWidget(self.btnAbout, 0, 1)
        self.groupBox.setLayout(self.gridLayout)
        self.layout.addWidget(self.groupBox)
        self.setLayout(self.layout)

    def help(self):
        pass

    def about(self):
        pass