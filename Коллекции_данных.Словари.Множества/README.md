# **Домашнее задание к лекции «4.Коллекции данных.Словари.Множества»** ***Вуколов Евгений***

Перед выполнением задания прочитайте короткую статью [про типы данных](https://wombat.org.ua/AByteOfPython/data_structures.html) и отличную [статью на Хабре](https://habr.com/ru/post/319164/)

## **Задание 1**  
Дан список с визитами по городам и странам.  Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
```python
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
```

## **Задание 2**  
Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]
```python
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
 ``` 

## **Задание 3**  
Дан список поисковых запросов. Получить распределение количества слов в них.
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
```python
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
```

## **Задание 4**  
Дана статистика рекламных каналов по объемам продаж.
Напишите скрипт, который возвращает название канала с максимальным объемом.
Т.е. в данном примере скрипт должен возвращать 'yandex'.
```python
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
```

## **Задание 5**  
*Напишите код для преобразования произвольного списка вида ```['2018-01-01', 'yandex', 'cpc', 100]``` (он может быть любой длины) в словарь
```{'2018-01-01': {'yandex': {'cpc': 100}}}```



Для подготовки к следующей лекции прочитайте про [функции](https://foxford.ru/wiki/informatika/funktsii-v-python)

---
Инструкция по выполнению домашнего задания:
Выполняйте домашнее задание в Jdoodle. Инструкцию по работе с JDoodle вы найдёте в первом занятии “Python. Знакомство с консолью”


*Никаких файлов прикреплять не нужно.*


# **Ответы:**


## **Задание 1**

```
geo_logs = [
  {'visit1': ['Москва', 'Россия']},
  {'visit2': ['Дели', 'Индия']},
  {'visit3': ['Владимир', 'Россия']},
  {'visit4': ['Лиссабон', 'Португалия']},
  {'visit5': ['Париж', 'Франция']},
  {'visit6': ['Лиссабон', 'Португалия']},
  {'visit7': ['Тула', 'Россия']},
  {'visit8': ['Тула', 'Россия']},
  {'visit9': ['Курск', 'Россия']},
  {'visit10': ['Архангельск', 'Россия']},
]

geo_logs = [visit for visit in geo_logs if 'Россия' in list(visit.values())[0]]
print(geo_logs)
```

- ![visit](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-07-30%20201735.png)

## **Вывод:** 

[{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]

## **Задание 2**

```
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
my_list=[ n for sublist in ids.values() for n in sublist]
print(list(set(my_list)))

```
- ![geo_ID](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-07-30%20203220.png)

## **Вывод:**

[98, 35, 15, 213, 54, 119]

## **Задание 3**

```
queries = [
  'смотреть сериалы онлайн',
  'новости спорта',
  'афиша кино',
  'курс доллара',
  'сериалы этим летом',
  'курс по питону',
  'сериалы про спорт'
]
my_dict={}
for query in queries:
   words_count=(len(query.split()))
 
   if words_count in my_dict : 
      my_dict[words_count]=my_dict[words_count] +1
   else :
      my_dict[words_count]= 1
 
for key,value in my_dict.items():
   percent= value/len(queries)*100
   percent=round(percent,2)
   print(key,value,percent)

```
- ![queries](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-07-30%20203417.png)

## **Вывод:**


3 4 57.14
2 3 42.86

## **Задание 4**

```
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max_value = 0
max_channel = ''
for key,value in stats.items():
  if value > max_value:
     max_value = value
     max_channel = key
print(max_channel)

```
- ![stats](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-07-30%20203528.png)

## **Вывод:**

yandex

## **Задание 5**

```
data = ['2018-01-01', 'yandex', 'cpc', 100]
result = {}
current_dict = result
for index, elem in enumerate(data[:-1]):
    if index == len(data) - 2:
        current_dict[elem] = data[index+1]

    else:
        current_dict[elem] = {}
        current_dict = current_dict[elem]
print(result)

```
- ![converting_list](https://github.com/Evgenii-379/Python_Programming_Course/blob/main/%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B0/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-07-30%20203626.png)

## **Вывод:**

{'2018-01-01': {'yandex': {'cpc': 100}}}






















