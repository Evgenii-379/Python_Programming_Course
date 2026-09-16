# Домашнее задание к лекции 5.«Функции — использование встроенных и создание собственных» ***Вуколов Евгений***

Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

```python
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
```    
Перечень полок, на которых находятся документы хранится в следующем виде:

```python
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
```

## Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

* `p` – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
* `s` – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;  
*Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ*.
* `l`– list – команда, которая выведет список всех документов в формате `passport "2207 876234" "Василий Гупкин"`;
* `a` – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. *Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку*.

**Внимание**: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

## Задача №2
* `d` – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. *Предусмотрите сценарий, когда пользователь вводит несуществующий документ*;
* `m` – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. *Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку*;
* `as` – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. *Предусмотрите случай, когда пользователь добавляет полку, которая уже существует*.;

## Задача №3
Почитать про lambda-функции. И что такое `*args` и `**kwargs`.

## Задача №4
Для подготовки к следующей лекции прочитайте про [классы](https://pythonworld.ru/osnovy/obektno-orientirovannoe-programmirovanie-obshhee-predstavlenie.html).

---
Инструкция по выполнению домашнего задания:
Выполняйте домашнее задание в Jdoodle. Инструкцию по работе с JDoodle вы найдёте в первом занятии “Python. Знакомство с консолью”

*Никаких файлов прикреплять не нужно.*

# **Решение :**

## **Задача №1 и Задача №2**


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_owner():

    number = input("Введите номер документа: ")
    found = False

    for doc in documents:
        if doc["number"] == number:
            print(doc["name"])
            found = True

    if found == False:
        print("Документ не найден")


def find_shelf():
    number = input("Введите номер документа: ")
    found = False

    for shelf, docs in directories.items():
        if number in docs:
            print(shelf)
            found = True
            break

    if found == False:
        print("Документ не найден")


def find_document():

    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')



def add_document():
    number = input("Введите номер документа: ")
    type_doc = input("Введите тип документа: ")
    name = input("Введите имя: ")
    shelf_number = input("Введите номер полки: ")

    if shelf_number in directories:
        documents.append({"number": number, "type": type_doc, "name": name, })
        directories[shelf_number].append(number)

    else:
        print("Полка не найдена")

def delete_document() :
    number = input("Ведите номер документа: ")
    found = False
    for doc in documents:
        if doc["number"] == number:
            found  = True
            documents.remove(doc)

    for shelf, docs in directories.items():
        if number in docs:
            docs.remove(number)
            found = True

    if found == False:
        print("Документ не найден ")

def move_document() :
    number = input("Введите номер документа:  ")
    shelf_target = input("Введите номер целевой полки: ")
    found = False

    if shelf_target in directories:

        for shelf, docs in directories.items():
            if number in docs:
                docs.remove(number)
                found = True
                directories[shelf_target].append(number)
                break

        if found == False:
            print("Документ не найден")

    else:
        print("Полка не найдена")

def add_shelf() :
    number_new_shelf = input("Назовите номер новой полки: ")
    if number_new_shelf in directories:
        print("Полка уже существует")
    else:
        directories[number_new_shelf]= []



command = input("Введите команду: ")
if command == "p":
    find_owner()

elif command == "s":
    find_shelf()

elif command == "l":
    find_document()

elif command == "a":
    add_document()

elif command == "d":
    delete_document()

elif command == "m" :
    move_document()

elif command == "as":
    add_shelf()

print(documents)
print(directories)

