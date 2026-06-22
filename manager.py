import json
import os
from models import Room, Reservation

class HotelManager:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.rooms = []
        self.reservations = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.rooms = [Room(**r) for r in data.get("rooms", [])]
                self.reservations = data.get("reservations", {})

    def save_data(self):
        data = {
            "rooms": [r.to_dict() for r in self.rooms],
            "reservations": self.reservations
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def process_payment(self, amount):
        print(f"Processing payment of ${amount}... Success!")
        return True

    def book_room(self, guest_name, room_id):
        for room in self.rooms:
            if room.room_id == room_id and room.is_available:
                if self.process_payment(room.price):
                    room.is_available = False
                    res_id = f"RES-{len(self.reservations)+101}"
                    self.reservations[res_id] = {"guest": guest_name, "room": room_id}
                    self.save_data()
                    return res_id
        return None

    def cancel_reservation(self, res_id):
        if res_id in self.reservations:
            room_id = self.reservations[res_id]["room"]
            for room in self.rooms:
                if room.room_id == room_id:
                    room.is_available = True
            del self.reservations[res_id]
            self.save_data()
            return True
        return False
