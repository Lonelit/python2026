users ={
    "Dima": {
        "phone": "+1 555-555-555",
        "street": "lenina",
    },
    "Igor": {
            "phone": "+1 555-555-555",
            "street": "lenina",
    },
    "Elena": {
            "phone": "+1 555-555-555",
            "street": "lenina",
    },
}
# словарь это users
# item ключ
# users значение
# users[item]), users.get(item) - Значение элемента словоря по ключу
for item in users: #поиск по ключу (игорь дима елена)
    print(users[item])

for key, value in users.items():
    print(key, value)

print("----------")
print(users.items())

user_1 = { "name": "Dima", "age": 20 }
user_1_other = {"street": "lenina", "city": "spb"}

user_1.update(user_1_other)
print(user_1)
