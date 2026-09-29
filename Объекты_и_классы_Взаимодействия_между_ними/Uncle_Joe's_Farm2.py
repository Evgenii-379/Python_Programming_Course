# I am implementing animal classes and defining methods for interacting with the animals

class Cow :
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлена")

    def milk(self):
        print(f"{self.name} подоена")

    def voice(self):
        print(f"{self.name} говорит Муу")

manka = Cow("Манька", 500)

manka.feed()
manka.milk()
manka.voice()

class Sheep:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлен")

    def shear(self):
        print(f"{self.name} подстрижен")

    def voice(self):
        print(f"{self.name} говорит Бее")

lamb = Sheep("Барашек", 200)

lamb.feed()
lamb.shear()
lamb.voice()

curly = Sheep("Кудрявый", 150)

curly.feed()
curly.shear()
curly.voice()

class Goat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлен")

    def milk(self):
        print(f"{self.name} подоен")

    def voice(self):
        print(f"{self.name} говорит Мее")

horns = Goat("Рога", 250)

horns.feed()
horns.milk()
horns.voice()

hooves = Goat("Копыта", 200)

hooves.feed()
hooves.milk()
hooves.voice()

class Goose:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлен")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорит Га Га")

grey = Goose("Серый", 15)

grey.feed()
grey.collect_eggs()
grey.voice()

white = Goose("Белый", 10)

white.feed()
white.collect_eggs()
white.voice()

class Chicken:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлен")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорит Ко Ко")

chick = Chicken("Ко-Ко", 5)

chick.feed()
chick.collect_eggs()
chick.voice()

kukareku = Chicken("Кукареку", 3)

kukareku.feed()
kukareku.collect_eggs()
kukareku.voice()


class Duck:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f"{self.name} накормлена")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорит Кря Кря")

quack = Duck("Кряква", 7)

quack.feed()
quack.collect_eggs()
quack.voice()

# Calculating the total weight of all animals and displaying the name of the heaviest animal

animals = [manka, lamb, curly, horns, hooves, grey, white, chick, kukareku, quack]
total = 0

for animal in animals:
    total += animal.weight

print(total)

max_weight = 0
max_name =""

for animal in animals:
    if animal.weight > max_weight:
        max_weight = animal.weight
        max_name = animal.name

print(max_name)



