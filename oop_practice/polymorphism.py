class Animal:
    def speak(self) -> str:
        return "Animal noises"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

class Cow(Animal):
    def speak(self) -> str:
        return "Moo"

animals = [Animal(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())

# python doesn't support method overriding like java but we can use None and if statements
class Calculator:
    def add(self, a, b, c=None):
        if not c:
            return a+b
        return a+b+c

c = Calculator()
print(c.add(1,2))

# Duck typing: unrelated classes with can be passed in a function if they have same method
class Duck:
    def quack(self) -> None:
        print("Quack")

class Robot:
    def quack(self) -> None:
        print("BEEP")

def sound(creature):
    creature.quack()

duck = Duck()
robot = Robot()
sound(duck)
sound(robot)