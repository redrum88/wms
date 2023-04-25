# Import tkinter gui class from MainWindow.py
# # ui/MainWindow.py

import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

# Import tkinter gui class from MainWindow.py
from ui.MainWindow import MainWindow

# Create QT application
app = qtw.QApplication(sys.argv)

# Create main window object
main_window = MainWindow()

# Show main window
main_window.show()

# Execute QT application
sys.exit(app.exec_())
