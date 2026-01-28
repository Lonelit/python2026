user_count =3
user_info = {}

for i in range(1, user_count+1):
    print(f"Введите информацию о {i}-м пользователе")
    name = input("Username: ")
    user_info[name] = {}

    street = input("street: ")
    phone = input("phone: ")

    user_info[name]["street"] = street
    user_info[name]["phone"] = phone

for user in user_info:
    print(f"Имя пользователля: {user}")
    print(f"улица:{user_info[user]["street"]}")
    print(f"тел:{user_info[user]["phone"]}")
    print("####################")
