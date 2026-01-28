# множество - set

users = {"Anna", "Sasha", "Lena", "Anna"}
users_list = ["Anna", "Sasha", "Lena", "Anna"]
user_set = set(users_list)
print(users_list)
print(users)

sets_of_cars = set()
print(type(sets_of_cars))
sets_of_cars.add("audi")
sets_of_cars.add("bmw")
sets_of_cars.add("lada")
sets_of_cars.add("lada")
print(len(sets_of_cars))
sets_of_cars.remove("bmw") # удаление
sets_of_cars.discard("lada22") #удаление без ошибки
print(sets_of_cars) #

for car in sets_of_cars:
    print(car)

sets_of_cars_2 = {"mazda", "audi", "uaz"}

# объединение множеств - union |
print("union")
result_ser_of_cars = sets_of_cars.union(sets_of_cars_2)
print(result_ser_of_cars)
print(sets_of_cars | sets_of_cars_2)

# пересечение множеств intersection &
print("intersection")
result_ser_of_cars = sets_of_cars.intersection(sets_of_cars_2)
print(result_ser_of_cars)
print(sets_of_cars & sets_of_cars_2)

# разность множеств difference -
print("difference")
result_ser_of_cars = sets_of_cars.difference(sets_of_cars_2)
print(result_ser_of_cars)
print(sets_of_cars - sets_of_cars_2)
print(sets_of_cars_2 - sets_of_cars)

# симметричная разность множеств symmetric_difference ^ (вернуть все элементы уникальные, неповторяющиеся)
print("symmetric_difference")
result_ser_of_cars = sets_of_cars.symmetric_difference(sets_of_cars_2)
print(result_ser_of_cars)
print(sets_of_cars ^ sets_of_cars_2)

# issubset является ли одно множество подножеством другого
users = {"Masha", "Dasha", "Sasha", "Lena"}
superusers = {"Sasha", "Lena"}

print(users.issubset(superusers))
print(superusers.issubset(users))

#frozenset  множество, которое не изменнеятся
person = frozenset({"Masha", "Dasha", "Sasha"})
print(type(person))

numbers = ["24234234", "233", "37737"]
set_numbers = frozenset(numbers)
print(set_numbers)