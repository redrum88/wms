# __init__.py

# Define the public interface for the package
__all__ = ['CRUD', 'createdb', 'settings']

# Import the modules that are part of the package
from .CRUD import CRUD
from .settings import DB
import createdb

# Define initialization code for the package
print('All modules initialized')