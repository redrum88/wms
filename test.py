import os
# Walk through current directory and print all files and directories
from db.CRUD import CRUD
from db.settings import DB
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

