"""
    Parent: Vehicle (color, brand, model, fuel_type)
    
    Child:  Car( no_of_wheels=4 )
    
    Child: Bike( no_ofwheels=2)
    """


class Vehicle:
    def __init__(self, color, brand, model, fuel_type):
        self.color = color
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        return f"<Brand: {self.brand}\nFuel Type:{self.fuel_type}>"

    def __repr__(self) -> str:
        return f"<Color: {self.color}\nModel:{self.model}>"

    def show_details(self) -> None:
        print(
            f"<Color:{self.color} \n Brand: {self.brand}\n Model: {self.model} \nFuel Type:{self.fuel_type}>"
        )


class Car(Vehicle):
    def __init__(self, color, brand, model, fuel_type, no_of_wheels):
        super().__init__(color, brand, model, fuel_type)
        self.no_of_wheels = no_of_wheels

    def show_details(self) -> None:
        super().show_details()
        print(f"No of Wheels: {self.no_of_wheels}")


class Bike(Vehicle):
    def __init__(self, color, brand, model, fuel_type, no_of_wheels):
        super().__init__(color, brand, model, fuel_type)
        self.no_of_wheels = no_of_wheels

    def show_details(self) -> None:
        super().show_details()
        print("No of Wheels: {self.no_of_wheels}")


car1 = Car(
    color="Blue",
    brand="Toyota",
    model="Hatchback",
    fuel_type="Hybrid",
    no_of_wheels="4",
)

bike1 = Bike(
    color="Yellow", brand="Bajaj", model="Avenger", fuel_type="petrol", no_of_wheels="2"
)
# print(bike1)
bike1.show_details()
# print(car1)
car1.show_details()
