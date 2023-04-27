from wms.db.CRUD import CRUD

class Location(CRUD):
    def __init__(self, db):
        super().__init__(db)

    def create(self, x, y, z, location_barcode, place_id):
        self.x = x
        self.y = y
        self.z = z
        self.location_barcode = location_barcode
        self.place_id = place_id
        super().create("location", f"({self.x}, {self.y}, {self.z}, '{self.location_barcode}', {self.place_id})")

    def read(self, location_id):
        super().read("location", location_id)

    def read_all(self):
        super().read_all("location")

    def update(self, location_id, x, y, z, location_barcode, place_id):
        self.location_id = location_id
        self.x = x
        self.y = y
        self.z = z
        self.location_barcode = location_barcode
        self.place_id = place_id
        super().update("location", self.location_id, f"x = {self.x}, y = {self.y}, z = {self.z}, location_barcode = '{self.location_barcode}', place_id = {self.place_id}")

    def delete(self, location_id):
        super().delete("location", location_id)
