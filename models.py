class Room:
    def __init__(self, room_id, category, price, is_available=True):
        self.room_id = room_id
        self.category = category
        self.price = price
        self.is_available = is_available

    def to_dict(self):
        return self.__dict__

class Reservation:
    def __init__(self, res_id, guest_name, room_id):
        self.res_id = res_id
        self.guest_name = guest_name
        self.room_id = room_id
