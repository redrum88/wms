# This file contains the class for the Branches table
import sys
import os

from wms.db.CRUD import CRUD

class Branches(CRUD):
    def __init__(self, db):
        super().__init__(db)

    def create(self, branch_name, phone, address, post_code):
        self.branch_name = branch_name
        self.phone = phone
        self.address = address
        self.post_code = post_code
        super().create("branch", f"('{self.branch_name}', '{self.phone}', '{self.address}', '{self.post_code}')")

    def read(self, id):
        super().read("branch", id)

    def read_all(self):
        super().read_all("branch")

    def update(self, id, branch_name, phone, address, post_code):
        self.branch_name = branch_name
        self.phone = phone
        self.address = address
        self.post_code = post_code
        super().update("branch", id, f"branch_name = '{self.branch_name}', phone = '{self.phone}', address = '{self.address}', post_code = '{self.post_code}'")

    def delete(self, id):
        super().delete("branch", id)
        

# Test
from wms.db import Database
db = Database()
b = Branches(db)
b.create("test", "test", "test", "test")