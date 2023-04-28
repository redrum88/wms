import sys
import os
from PySide6.QtSql import QSqlDatabase
from db import createdb

DB_TYPE = "QPSQL"
HOST = "localhost"
DATABASE = "my_database"
USER = "postgres"
PASSWORD = "Naujas293"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DB:

    def __version__(self):
        return "0.1"

    def __init__(self):
        # Create connection
        self.db = QSqlDatabase.addDatabase(DB_TYPE)
        self.db.setHostName(HOST)
        self.db.setDatabaseName(DATABASE)
        self.db.setUserName(USER)
        self.db.setPassword(PASSWORD)

        if not self.db.open():
            print("Cannot open database: ", self.db.lastError().text())
            sys.exit(1)
        else:
            print("Connected to database.")
            
    def create_tables(self):
        createdb.init_db()

    def disconnect(self):
        self.db.close()
        print("Disconnected from database.")

    def __del__(self):
        self.db.close()
        print("Disconnected from database.")

    