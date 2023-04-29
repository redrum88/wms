import sys
from ui.MainWindow import MainWindow
from ui.ui_Login import Login
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec())