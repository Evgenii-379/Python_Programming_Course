class Cow :
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} накормлена")

    def milk(self):
        print(f"{self.name} подоена")

    def voice(self):
        print(f"{self.name} говорит Муу")

manka = Cow("Манька")

manka.feed()
manka.milk()
manka.voice()

class Sheep:

    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} накормлен")

    def shear(self):
        print(f"{self.name} подстрижен")

    def voice(self):
        print(f"{self.name} говорит Бее")

lamb = Sheep("Барашек")

lamb.feed()
lamb.shear()
lamb.voice()

curly = Sheep("Кудрявый")

curly.feed()
curly.shear()
curly.voice()

class Goat:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} накормлен")

    def milk(self):
        print(f"{self.name} подоен")

    def voice(self):
        print(f"{self.name} говорит Мее")

horns = Goat("Рога")

horns.feed()
horns.milk()
horns.voice()

hooves = Goat("Копыта")

hooves.feed()
hooves.milk()
hooves.voice()

class Goose:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} накормлен")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорит Га Га")

grey = Goose("Серый")

grey.feed()
grey.collect_eggs()
grey.voice()

white = Goose("Белый")

white.feed()
white.collect_eggs()
white.voice()

class Chicken:

    def __init__(self, name):
        self.name = name
    def feed(self):
        print(f"{self.name} накормлен")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорят Ко Ко")

chick = Chicken("Ко-Ко")

chick.feed()
chick.collect_eggs()
chick.voice()

kukareku = Chicken("Кукареку")

kukareku.feed()
kukareku.collect_eggs()
kukareku.voice()


class Duck:

    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} накормлена")

    def collect_eggs(self):
        print(f"{self.name} яйца собраны")

    def voice(self):
        print(f"{self.name} говорит Кря Кря")

quack = Duck("Кряква")

quack.feed()
quack.collect_eggs()
quack.voice()


