# строки string (не изменные)
message = "hello"
name = 'Misha'
char = "i"

print(type(message))
print(type(name))
print(type(char))

text = ("kjhsfshdnsd"
        "jdskdjsndnfn"
        "sldjfnsfsflslfm\n"
        ";alw,ldcmkfskfn")
print(text)
long_text = """
kffwsjfkwj
fw;lmflkwfwf
w;lfmwkmflwkmf
;wlmfwlmfwm"""
print(long_text)

alphabet = "abcdefghijklmn"
print(alphabet[0], alphabet[1:], alphabet[-7])
print(list(alphabet))

for char in alphabet:
    print(char)

print(len(alphabet))

#конкатинация объединение

name = "Misha junior"
last_name = "ivanov"
full_name = name + " " + last_name
print(full_name)
print(" ".join([name, last_name]))

# повторение
print("a"*3)
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize()) #сделал только первую букву большую
print(name.replace("i", "!!!"))
print(name.count("i"))
email = "admin@yandex.ru"
print(email.endswith("yandex.ru"))
print(email.startswith("admin"))
if "admin" in email:
    print("admin in email")
input_value = "  hello!   "
print(input_value.strip())
print(input_value.lstrip()) # удалили пробелы только слева
site = "auth.vk.spb.ru"
domens = site.split(".")
print(domens)
print(len(domens))
print(domens[0])
print(domens[-1])
