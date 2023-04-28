import os
import sys
# Walk through current directory and print all files and directories
from db.CRUD import CRUD

crud = CRUD()

all_branch = crud.read_branch()
last_branch = crud.read_branch_id_last()
print(all_branch)
print(last_branch)