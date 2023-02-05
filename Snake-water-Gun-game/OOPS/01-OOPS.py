# Inheritance
# Single Inheritance

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"The make of car is {self.make}, model is {self.model} and year is {self.year}"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def description(self):
        return super().description() + f", and the battery size is {self.battery_size}."


ec = ElectricCar("Tesla", "Model S", 2021, 75)
print(ec.description())

# Output:
# The make of car is Tesla, model is Model S and year is 2021, and the battery size is 75.

# Multiple Inheritance


class A:
    def __init__(self):
        self.a = "a"
        print("A")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B:
    def __init__(self):
        self.b = "b"
        print("B")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")

    def feature5(self):
        print("Feature 5 is working")

# Multi-level Inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("Name:", self.name)


class Mammal(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_info(self):
        Animal.show_info(self)
        print("Breed:", self.breed)


class Dog(Mammal):
    def __init__(self, name, breed, color):
        Mammal.__init__(self, name, breed)
        self.color = color

    def show_info(self):
        Mammal.show_info(self)
        print("Color:", self.color)
