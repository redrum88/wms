import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

# Create QT tab 1 class for MainWindow
class Tab2(qtw.QWidget):
    
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            self.create_widgets()
    
        def create_widgets(self):
            self.layout = qtw.QVBoxLayout()
            self.setLayout(self.layout)
    
            self.label = qtw.QLabel('Test')
            self.layout.addWidget(self.label)

            self.button = qtw.QPushButton('Open Window 1')
            self.layout.addWidget(self.button)
            self.button.clicked.connect(self.open_window1)

            self.button = qtw.QPushButton('Open Window 2')
            self.layout.addWidget(self.button)
            self.button.clicked.connect(self.open_window1)

            self.button = qtw.QPushButton('Open Window 3')
            self.layout.addWidget(self.button)
            self.button.clicked.connect(self.open_window1)

    
            self.button = qtw.QPushButton('Open Settings Window')
            self.layout.addWidget(self.button)
            self.button.clicked.connect(self.open_window1)
    
        def open_window1(self):
            print('Open Window 1')
