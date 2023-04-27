import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from wms.db.CRUD import CRUD

class Place(CRUD):
    def __init__(self, db):
        super().__init__(db)

    def create(self, place_name, place_barcode, description, branch_id):
        self.place_name = place_name
        self.place_barcode = place_barcode
        self.description = description
        self.branch_id = branch_id
        super().create("place", f"('{self.place_name}', '{self.place_barcode}', '{self.description}', {self.branch_id})")

    def read(self, id):
        super().read("place", id)

    def read_all(self):
        super().read_all("place")

    def update(self, id, place_name, place_barcode, description, branch_id):
        self.place_name = place_name
        self.place_barcode = place_barcode
        self.description = description
        self.branch_id = branch_id
        super().update("place", id, f"place_name = '{self.place_name}', place_barcode = '{self.place_barcode}', description = '{self.description}', branch_id = {self.branch_id}")

    def delete(self, id):
        super().delete("place", id)
