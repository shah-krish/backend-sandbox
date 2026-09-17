class Pizza:
    base_crust = "Thin"

    def __init__(self, topping):
        self.topping = topping

    # Instance Method
    def describe_pizza(self):
        return f"A {self.base_crust} crust pizza with {self.topping}."

    # Class Method
    @classmethod
    def change_crust(cls, new_crust):
        cls.base_crust = new_crust

    # Static Method
    @staticmethod
    def is_healthy(topping):
        return topping in ["spinach", "mushrooms", "peppers"]

mushroom = Pizza("mushroom")
pineapple = Pizza("pineapple")
print(mushroom.describe_pizza())
mushroom.change_crust("thick")
print(pineapple.describe_pizza()) #pineapple's crust also changed because of class method