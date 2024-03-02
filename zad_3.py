class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f"Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    
    def __str__(self):
        return f"House - {super().__str__()}, Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()}, Floor: {self.floor}"


house = House(area=150, rooms=4, price=300000, address="ul. Kwiatowa 5", plot=500)
flat = Flat(area=80, rooms=2, price=150000, address="ul. Słoneczna 10", floor=2)

print(house)
print(flat)
"""
print("House:")
print("Area:", house.area)
print("Rooms:", house.rooms)
print("Price:", house.price)
print("Address:", house.address)
print("Plot:", house.plot)

print("\nFlat:")
print("Area:", flat.area)
print("Rooms:", flat.rooms)
print("Price:", flat.price)
print("Address:", flat.address)
print("Floor:", flat.floor)
"""