# Import tkinter gui class from MainWindow.py
# # ui/MainWindow.py

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from ui.MainWindow import MainWindow

app = qtw.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())
