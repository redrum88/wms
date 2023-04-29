import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

__all__ = ['MainWindow', 'CRUD', 'DB']

from .MainWindow import MainWindow
from db.settings import DB
from db.CRUD import CRUD


