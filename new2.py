# словари
person = {}
#    ключ(харак-тика):   значение
car = {
    "brand": "bmw",
    "model": "x5",
    "year": 1997,
}
# добавление элемента в словарь
person["name"] = "Alex"
person["age"] = 19
person["skills"] = ["work", "sleep"]

print(person)

# получение значения по ключу
print(person["age"])

age = person.get("age1", "err")
print(age)

# удаление и получение элемента по ключу
age = person.pop("age")
print(age)
print(person)


print(person.keys())
print(person.values())
print(person.items())

my_list1 = [1, 2, 3, 4, 5]
print(id(my_list1))

#my_list2 = my_list1
my_list2 = my_list1.copy()
print(id(my_list2))

my_list1.pop()
print(my_list1)
print(my_list2)

person = []
for i in range(3): # создание диапазона [0, 1, 2]
   name = input("Введите имя: ")
   age = input("Введите возраст: ")
   person_info = {"name": name, "age": age}
   person.append(person_info)
print(person)

person = []
N = 3
for i in range(N): # range( start, stop, step) range(N) = [0,1,2,3,4,5...,N-1]
   # i + 1, так как i начинается с 0
   print(f"ВВедите инфо о {i+1} человеке из {N}")
   name = input("Введите имя: ")
   age = input("Введите возраст: ")
   person_info = {"name": name, "age": age}
   person.append(person_info)
print(person)

