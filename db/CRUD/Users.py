import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from wms.db.CRUD import CRUD

class Users(CRUD):
    def __init__(self, db):
        super().__init__(db)

    def create(self, email, password, group_id):
        self.email = email
        self.password = password
        self.group_id = group_id
        super().create("users", f"('{self.email}', '{self.password}', {self.group_id})")

    def read(self, id):
        super().read("users", id)

    def read_all(self):
        super().read_all("users")

    def update(self, id, email, password, group_id):
        self.email = email
        self.password = password
        self.group_id = group_id
        super().update("users", id, f"email = '{self.email}', password = '{self.password}', group_id = {self.group_id}")

    def delete(self, id):
        super().delete("users", id)