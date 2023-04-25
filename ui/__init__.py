# ui/__init__.py
import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

__all__ = ['MainWindow', 'Tab1', 'Tab2', 'Window1', 'Window2']

from .MainWindow import MainWindow
from .Tab1 import Tab1
# from .Tab2 import Tab2
# from .Window1 import Window1
# from .Window2 import Window2

