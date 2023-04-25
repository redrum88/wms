# ui/MainWindow.py

import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from Tab1 import Tab1
from Tab2 import Tab2
# Create QT tab 1 class for MainWindow


# Create main window class inheriting from QMainWindow class
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setWindowIcon(qtg.QIcon(':/icons/icon.png'))
        self.resize(800, 600)
        self.create_widgets()
        self.create_menus()
        self.create_status_bar()

    def create_widgets(self):
        self.tab_widget = qtw.QTabWidget()
        self.tab1 = Tab1(self.tab_widget)
        self.tab2 = Tab2(self.tab_widget)
        self.tab_widget.addTab(self.tab1, 'Categories')
        self.tab_widget.addTab(self.tab2, 'Tab 2')
        self.setCentralWidget(self.tab_widget)

    def create_menus(self):
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('File')
        self.edit_menu = self.menu_bar.addMenu('Edit')
        self.help_menu = self.menu_bar.addMenu('Help')

        self.new_action = qtw.QAction('New', self)
        self.file_menu.addAction(self.new_action)
        self.open_action = qtw.QAction('Open', self)
        self.file_menu.addAction(self.open_action)
        self.save_action = qtw.QAction('Save', self)
        self.file_menu.addAction(self.save_action)
        self.exit_action = qtw.QAction('Exit', self)
        self.file_menu.addAction(self.exit_action)

        self.cut_action = qtw.QAction('Cut', self)
        self.edit_menu.addAction(self.cut_action)
        self.copy_action = qtw.QAction('Copy', self)
        self.edit_menu.addAction(self.copy_action)
        self.paste_action = qtw.QAction('Paste', self)
        self.edit_menu.addAction(self.paste_action)

        self.about_action = qtw.QAction('About', self)
        self.help_menu.addAction(self.about_action)

    def create_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready')

    def open_window1(self):
        self.window1 = Window1(self)
        self.window1.show()

    def open_window2(self):
        self.window2 = Window2(self)
        self.window2.show()


# Run main window
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

# ui/Tab1.py



