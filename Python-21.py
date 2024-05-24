# 1. Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_year(self, year):
        self.car.year = year
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car


builder = CarBuilder()
car = builder.set_make("BMW").set_model("X5").set_year(2021).set_color("blue").build()
print(car)

# 2. Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_pasta_type(self, pasta_type):
        self.pasta.pasta_type = pasta_type

    def set_sauce(self, sauce):
        self.pasta.sauce = sauce

    def set_fillings(self, fillings):
        self.pasta.fillings = fillings

    def set_addons(self, addons):
        self.pasta.addons = addons

    def get_pasta(self):
        return self.pasta


class Pasta:
    def __init__(self):
        self.pasta_type = ''
        self.sauce = ''
        self.fillings = ''
        self.addons = ''


class SpaghettiBuilder(PastaBuilder):
    def __init__(self):
        super().__init__()
        self.set_pasta_type('Spaghetti')

class PenneBuilder(PastaBuilder):
    def __init__(self):
        super().__init__()
        self.set_pasta_type('Penne')

class FusilliBuilder(PastaBuilder):
    def __init__(self):
        super().__init__()
        self.set_pasta_type('Fusilli')


spaghetti_builder = SpaghettiBuilder()
spaghetti_builder.set_sauce('Tomato')
spaghetti_builder.set_fillings('Meatballs')
spaghetti_builder.set_addons('Parmesan cheese')

spaghetti = spaghetti_builder.get_pasta()
print(f'Type: {spaghetti.pasta_type}')
print(f'Sauce: {spaghetti.sauce}')
print(f'Fillings: {spaghetti.fillings}')
print(f'Addons: {spaghetti.addons}')

# 3. Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_objects(self, name, obj):
        self._objects[name] = obj

    def unregister_objects(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class Car:
    def __init__(self):
        self.make = "Ford"
        self.model = "Mondeo"
        self.year = "2018"

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


prototype = Prototype()

car = Car()
prototype.register_objects('car', car)

car_clone = prototype.clone('car', year='2020')

print(car)
print(car_clone)