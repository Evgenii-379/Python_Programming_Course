# Домашнее задание к лекции «Объекты и классы. Взаимодействие между ними» ***Вуколов Евгений***
​
Привет! Вы уже прошли курс по Git и узнали на занятии, что такое IDE. Пришло время применить полученные знания!

Начиная с этого занятия, пишите код в IDE (рекомендуем [Pycharm](https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows), версия Community, инструкцию по установке вы найдете на сайте).  
- Почему лучше работать в IDE? — Ускоряет работу, есть подсветка ошибок, отладка по шагам.  
- Для более подробной информации изучите [инструкцию по работе с Pycharm](https://github.com/netology-code/guides/blob/master/python/Pycharm.md).  
- Опирайтесь на принятые [правила оформления кода](https://github.com/netology-code/codestyle/tree/master/python), чтобы выработать привычку писать профессионально. При несоблюдении принятого стиля домашние задания **могут** быть отправлены на доработку.   

## Как сдавать задачи
1. Инициализируйте на своём компьютере пустой Git-репозиторий
2. Добавьте в этот же каталог необходимые файлы
3. Сделайте необходимые коммиты
4. Создайте публичный репозиторий на GitHub и свяжите свой локальный репозиторий с удалённым
5. Сделайте пуш (удостоверьтесь, что ваш код появился на GitHub)
6. Ссылку на ваш проект отправьте в личном кабинете на сайте [netology.ru](http://netology.ru/)
7. Задачи, отмеченные как необязательные, можно не сдавать, это не повлияет на получение зачета (в этом ДЗ все задачи являются обязательными)
8. Любые вопросы по решению задач задавайте в чате Slack, но мы не сможем проверить или помочь, если вы пришлете:
* архивы;
* скриншоты кода;
* теоретический рассказ о возникших проблемах.

## Задача №1 "Ферма Дядюшки Джо"
Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
* гусей "Серый" и "Белый"
* корову "Маньку"
* овец "Барашек" и "Кудрявый"
* кур "Ко-Ко" и "Кукареку"
* коз "Рога" и "Копыта"
* и утку "Кряква"
​
Со всеми животными вам необходимо как-то взаимодействовать:
* кормить
* корову и коз доить
* овец стричь
* собирать яйца у кур, утки и гусей
* различать по голосам(коровы мычат, утки крякают и т.д.)
​
## Задание 1:
Нужно реализовать классы животных и определить методы взаимодействия с животными.  
​Для каждого животного из списка должен существовать экземпляр класса.  
Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
​
## Задание 2:
У каждого животного должно быть определено имя(```self.name```) и вес(```self.weight```). 
- Необходимо посчитать общий вес всех животных(экземпляров класса);
- Вывести название самого тяжелого животного.

## Задача №2 "Аудиоколлекция"
Необходимо уметь хранить информацию по альбомам и трекам в них. Это можно сделать, используя классы ```Album``` и ```Track```.  
У класса ```Track``` есть поля:
* Название;
* Длительность в минутах(используется тип данных ```int```).
И метод ```show```, выводящий информацию по треку в виде ```<Название-Длительность>```.  

У класса ```Album``` есть поля:
* Название альбома
* Группа
* Список треков
И три метода:
* ```get_tracks``` - выводит информацию по всем трекам(используется метод ```show```).
* ```add_track``` - добавление нового трека в список треков.
* ```get_duration``` - выводит длительность всего альбома.

## Задание:
Создать 2 альбома с 3 треками. Для каждого вывести его длительность.



# Выполнение заданий :

## Задание № 1 :

```
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

```

