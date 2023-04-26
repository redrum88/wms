# Import tkinter gui class from MainWindow.py
# # ui/MainWindow.py

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from PySide6.QtWidgets import QApplication
from ui import MainWindow
import rc_books

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
