# списки
from pstats import count_calls

numbers = []
cars = ["bmw", "audi"]

# получение длины списка
print(len(cars))

# добавление элемента в конец списка
cars.append("lada")
print(cars)
cars.insert(0, "kia")
print(cars)
# расширение списка
cars.extend(["honda", "mazda"])
print(cars)
#удаление элемента списка (только первое вхождение)
cars.remove("honda")
print(cars)
# получение индекса элемента
ind_mazda = cars.index("mazda")
print(ind_mazda)
# подсчет кол-ва элементов
count_mazda = cars.count("mazda")
print(count_mazda)

# удаление  и получение элемента, по индексу
deleted_cars = cars.pop()
print(deleted_cars)
print(cars)

bmw = "bmw" in cars
print(bmw)

if "bmw" in cars:
    print("ok")

# получение среза
#   -4     -3     -2      -1
#    0      1      2       3
# ['kia', 'bmw', 'audi', 'lada']
print(cars)
print(cars[1:3])
print(cars[-3:])
# [start:end:step]
print(cars[::-1])

# как пройтись циклом по списку
for car in cars:
    print(car.upper())
    print(car.title())
    print(f"B слове {car} - {len(car)} символов")

for car in cars:
    if len(car) > 3:
        print(f"B слове {car} - {len(car)} символов")
for car in cars:
    if len(car) > 3:
        for i in car:
            print(i.upper())

# name = input("Введите своё имя: ")
# print("Вы ввели имя -", name)

N = 3 # количество итераций (проходов цикла)
i = 0 # нач значения счетчика цикла
my_list = []

print()

# while i < N:
#     item = input("Введите строку: ")
#     if len(item) > 3:
#         my_list.append(item) # добавляем в конец списка
#     else:
#         print(f"строка {item} менее трех символов!")
#     i+=1
# print(my_list)

"""
# пользователь вводит с клавиатуры строки
ввод закончить пи ввооде строки end (в любом регистре)
добавлять в список строки с ! на конце
"""
words = []
while True:
    text = input("ВВедите строку:\n")
    if text.lower() == "end":
        break
    else:
        if text: # если строка не пустая
            if text[-1] == "!": # если в строке есть ! то он добавляется к нам в список
                words.append(text)
                print(words)