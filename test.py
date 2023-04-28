import os
import sys
# Walk through current directory and print all files and directories
from db import settings
from db import CRUD
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


