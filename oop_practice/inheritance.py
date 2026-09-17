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

