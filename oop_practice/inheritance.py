class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand}")

class ElectricVehicle(Vehicle):
    def charge(self) -> None: #child doesn't always need constructor, will simply use parent's
        print(f"Charging {self.brand} to 100%...")

class GasVehicle(Vehicle):
    def __init__(self, brand: str, year: int, capacity: str):
        super().__init__(brand,year) #super to reference parent attributes
        self.capacity = capacity

tesla = ElectricVehicle("tesla", "2026")
print(tesla.brand)

honda = GasVehicle("honda", "2025", "50L")
print(honda.capacity)

#Composition (Has-A) example
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self) -> None:
        print(f"Engine ({self.horsepower} HP) starting.")

class Car:
    def __init__(self, make: str, engine: Engine):
        self.make = make
        self.engine = engine  # Car HAS an Engine

    def drive(self) -> None:
        print(f"Starting {self.make}:")
        self.engine.start()

v8 = Engine(450)
mustang = Car("Ford Mustang", v8)
mustang.drive()

