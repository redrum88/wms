from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLabel, QStatusBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor
from db.settings import DB
from db.CRUD import CRUD
# Dashboard tab with actions (Add, Edit, Delete, Refresh, Search, Filter). Must be clicked from MainWindow menu to be shown.
class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Arial", 10))

        # Set up the layout and group box
        self.layout = QVBoxLayout(self)
        self.groupBox = QGroupBox("About")
        self.layout.addWidget(self.groupBox)
        self.gridLayout = QGridLayout(self.groupBox)

                # Create About text with description of the application and its purpose. Show at the top center of the Dashboard tab
        self.about_text = QLabel()
        self.about_text_css = """
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #808080;
                text-align: center;
                margin-top: 50px;
            }
            #aboutTable {
                border-collapse: collapse;
                margin-left: auto;
                margin-right: 20px;
                margin-bottom: 20px;
                border: 1px solid #000000;
                border-radius: 5px;
                box-shadow: 2px 2px 5px #888888;
                font-size: 14px;
                font-weight: bold;
                color: #000000;
                background-color: #ffffff;
                position: absolute;
                bottom: 0;
                left: 0;
            }
            #aboutTable th {
                border: 1px solid #000000;
                padding: 10px;
                background-color: #f5f5f5;
                color: #000000;
            }
            #aboutTable td {
                border: 1px solid #000000;
                padding: 10px;
                text-align: center;
                color: #808080;
            }
        """

        self.db = DB()
        version = self.db.execute("SELECT version();")
        while version.next():
            print("Connected to PostgreSQL " + version.value(0))
            self.setStatusTip("Connected to PostgreSQL " + version.value(0))
            db_version = version.value(0)
        self.about_text.setStyleSheet(self.about_text_css)
        self.about_text.setAlignment(Qt.AlignCenter)

        self.about_text.setText("""
            <html>
                <body>
                    <div id="aboutText">
                        <h1>Warehouse Management System (WMS)</h1>
                        <p>Warehouse Management System (WMS) is a software application</p>
                        <p> that helps manage inventory and order fulfillment.</p>
                        </br>
                        </br>
                        </br>
                    </div>
                    </br>
                    </br>
                    </br>
                    <table id="aboutTable">
                        <tr>
                            <th>Database Server:</th>
                            <td>%s</td>
                        </tr>
                        <tr>
                            <th>CRUD Version:</th>
                            <td>%s</td>
                        </tr>
                        <tr>
                            <th>DB Version:</th>
                            <td>%s</td>
                        </tr>
                        <tr>
                            <th>Total Tables:</th>
                            <td>%s</td>
                        </tr>
                        <tr>
                            <th>Total Users:</th>
                            <td>%s</td>
                        </tr>
                    </table>
                    </br>
                    <div style="margin-bottom: 20px;">
                        <p><strong>Author:</strong> </p>
                        <p><strong>Website:</strong> <a href="https://kedevo.com/">here</a></p>
                    </div>
                </body>
            </html>
        """ % (db_version, CRUD().__version__(), DB().__version__(), self._get_total_tables(), self._get_total_users()))

        
        self.gridLayout.addWidget(self.about_text)

        # Add some padding around the group box
        self.groupBox.setStyleSheet("QGroupBox { padding: 20px; border: 1px solid #e4e4e4 }")
        
    def _get_total_tables(self):
        total_tables_query = DB().execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")
        if total_tables_query.next():
            return total_tables_query.value(0)
        else:
            return ""

    def _get_total_users(self):
        total_users_query = DB().execute("SELECT COUNT(*) FROM users;")
        if total_users_query.next():
            return total_users_query.value(0)
        else:
            return ""



        




    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def refresh(self):
        pass

    def search(self):
        pass

    def filter(self):
        pass