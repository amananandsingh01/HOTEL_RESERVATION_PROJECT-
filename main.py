from manager import HotelManager

def main():
    manager = HotelManager()
    
    # Simple CLI
    print("--- Hotel Reservation System ---")
    action = input("Choose: [1] Search [2] Book [3] Cancel [4] Exit: ")
    
    if action == '1':
        cat = input("Enter Category (Standard/Deluxe/Suite): ")
        available = [r for r in manager.rooms if r.category == cat and r.is_available]
        for r in available: print(f"Room {r.room_id} - ${r.price}")
        
    elif action == '2':
        name = input("Guest Name: ")
        rid = input("Room ID: ")
        res_id = manager.book_room(name, rid)
        print(f"Booking successful! ID: {res_id}" if res_id else "Booking failed.")

    elif action == '3':
        rid = input("Reservation ID: ")
        if manager.cancel_reservation(rid): print("Cancelled.")
        else: print("Invalid ID.")

if __name__ == "__main__":
    main()
