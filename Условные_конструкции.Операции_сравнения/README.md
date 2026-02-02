# Домашнее задание к лекции 2.«Условные конструкции. Операции сравнения»

## Задача №1
На лекции мы рассматривали пример для военкомата. Сейчас мы знаем про его рост. Расширить это приложение следующими условиями:
1. Проверка на возраст призывника.
2. Количество детей.
3. Учится ли он сейчас.

## Задание №2
Разработать приложение для определения знака зодиака по дате рождения.
Пример:
```
Введите месяц: март
Введите число: 6

Вывод:
Рыбы
```

## Задание №3
К следующей лекции прочитать про циклы [for](https://foxford.ru/wiki/informatika/tsikl-for-v-python) и
 [while](https://foxford.ru/wiki/informatika/tsikl-while-v-python).

---
Инструкция по выполнению домашнего задания:
Выполняйте домашнее задание в Jdoodle. Инструкцию по работе с JDoodle вы найдёте в первом занятии “Python. Знакомство с консолью”

*Никаких файлов прикреплять не нужно.*


# **Решение:**


## **Задание № 1**

```

height = int(input("введите рост:"))
age = int(input("Введите возраст:"))
children = int(input("Введите количество детей:"))
is_student = input("Вы студент? (да/нет):")
if height <= 170 and age >= 18 and children < 2 and is_student == "нет":
    print("В танкисты")

elif height <= 180 and age >= 18 and children < 2 and is_student == "нет":
    print("На флот")

elif height <= 200 and age >=18 and children < 2 and is_student == "нет":
    print("В десантники")

else:
    print("Не годен к службе")

```

- ![voencomat](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-02-02%20124543.png)


## **Задание № 2**

```

month = input("Введите месяц:")
day = int(input("Введите число:"))
if (month == "Декабрь" and day >= 22) or (month == "Январь" and day <= 19):
    print("Козерог")
elif (month == "Январь" and day >= 20) or (month == "Февраль" and day <= 18):
    print("Водолей")
elif (month == "Февраль" and day >= 19) or (month == "Март" and day <= 20):
    print("Рыба")
elif (month == "Март" and day >= 21) or (month == "Апрель" and day <= 19):
    print("Овен")
elif (month == "Апрель" and day >= 20) or (month == "Май" and day <= 20):
    print("Телец")
elif (month == "Май" and day >= 21) or (month == "Июнь" and day <= 20):
    print("Близнецы")
elif (month == "Июнь" and day >= 21) or (month == "Июль" and day <= 22):
    print("Рак")
elif (month == "Июль" and day >= 23) or (month == "Август" and day <= 22):
    print("Лев")
elif (month == "Август" and day >= 23) or (month == "Сентябрь" and day <= 22):
    print("Дева")
elif (month == "Сентябрь" and day >= 23) or (month == "Октябрь" and day <= 22):
    print("Весы")
elif (month == "Октябрь" and day >= 23) or (month == "Ноябрь" and day <= 21):
    print("Скорпион")
elif (month == "Ноябрь" and day >= 22) or (month == "Декабрь" and day <= 21):
    print("Стрелец")


else:
    print("Другой знак зодиака")

```

- ![zodiac_sign](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-02-02%20124704.png)


