
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Kitchen"), Room("Bed Room"), Room("Guest Room")] # list of Room objects
 #[Room("Living Room"), Room("Kitchen"), Room("Bed Room"), Room("Guest Room")] is a list comprehension. It creates a 
 # list 
 # containing four Room objects, each initialized with a different room name.
    def __str__(self):
        room_names = ", ".join(room.name for room in self.rooms)# list comprehension
        return f"House with rooms: {room_names}"

my_house = House()
print(my_house)


my_list=["ram","shayam","Sita"]
for name in my_list:
    print(name)