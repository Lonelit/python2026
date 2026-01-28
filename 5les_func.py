#  вызов в функции с помощью def
def print_hello(name): #   имя функции и ее параметр называют сигнатурой функции
    print(name.title())   # тело функции
def print_fio(name, last_name, age):
    name = name.title()
    last_name = last_name.upper()
    new_age = age * 2
    print(name, last_name, new_age)
def hello():
    print("hello")

hello()
print_hello("Alex")
print_fio("dima","ivanov",10)

# numbers = [2, 7, 10, 12, 55]
def get_min_value(numbers):
    min_value = numbers[0]
    for i in numbers:
        if i < min_value:
            min_value = i
    print(min_value)

numbers_1 = [2, 7, 10, 12, 55]
numbers_54 = [2, 7, 10, 12, 133 ,55, 1]
get_min_value(numbers_1)
get_min_value(numbers=numbers_54)
get_min_value([2000, 7, -10, 12, 55])

# text1 = "hello11 privet 25"
def get_count_numbers(text):
    count = 0
    symbols = "0123456789"
    for i in text:
        if i in symbols:
            count +=1
    print(count)
text1 = "hello11 privet 25"
get_count_numbers(text1)

def get_count_numbers(text):
    count = 0
    symbols = "0123456789"
    sum_numbers = 0
    for i in text:
        if i in symbols:
            count += 1
        if i.isdigit(): # isdigit проверяет цифра ли это
            sum_numbers += int(i) # int("1122") = 1122, int("1122a") = error
    print(f"количество цифр - {count}")
    print(f"сумма цифр - {sum_numbers}")
text1 = "hello11 privet 25"
get_count_numbers(text1)

for i in text1: #text1 = ["h", "e", "l" ....]
    # print(i)

array = [1, 5, 7, 80, 9]
# найти максимальное четное
def get_max_even_number(numbers):
    max_value = numbers[0]
    for i in numbers:
        if i > max_value
            max_value = i
    print(max_value)

