class Dog:

    trait = 'loyal'

    def __init__(self, name, breed,id):
        self.name = name
        self.breed = breed
        self.__id = id

    def bark(self):
        return f"{self.name} is barking!"
    @property #can use this method without () now. id can be called like a normal attribute but still private
    def id(self):
        return self.__id

    @id.setter
    def id(self, num: int):
        if num < 0:
            raise ValueError("ID can't be negative")
        self.__id = num


shiro = Dog('shiro', 'golden', 1)
print(shiro.bark())
print(shiro.trait)
print(shiro.id)
shiro.id = 5
print(shiro.id)