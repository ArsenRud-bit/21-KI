# 1. Легендарна програма всіх програмістів
print("Hello, World!")
print("=" * 45)

# 2. Створення змінних всіх відомих базових типів даних
text_data = "Python"                 # str (рядок)
integer_data = 2026                  # int (ціле число)
float_data = 3.14                    # float (десяткове число)
boolean_data = True                  # bool (логічний тип)
list_data = [10, 20, 30]             # list (список)
tuple_data = (1, 2, 3)               # tuple (кортеж)
set_data = {5, 6, 7}                 # set (множина)
dict_data = {"name": "Арсеній"}      # dict (словник)

# Виведення значень та їхніх типів за допомогою f-рядків та функції type()
print("--- ЗМІННІ ТА ЇХНІ ТИПИ ---")
print(f"text_data: {text_data} | Тип: {type(text_data)}")
print(f"integer_data: {integer_data} | Тип: {type(integer_data)}")
print(f"float_data: {float_data} | Тип: {type(float_data)}")
print(f"boolean_data: {boolean_data} | Тип: {boolean_data.__class__.__name__}") # або через type()
print(f"list_data: {list_data} | Тип: {type(list_data)}")
print(f"tuple_data: {tuple_data} | Тип: {type(tuple_data)}")
print(f"set_data: {set_data} | Тип: {type(set_data)}")
print(f"dict_data: {dict_data} | Тип: {type(dict_data)}")

print("=" * 45)

# 3. Використання всіх вивчених операторів
print("--- ДЕМОНСТРАЦІЯ ОПЕРАТОРІВ ---")

a = 12
b = 5

# Арифметичні оператори (+, -, *, /, //, %, **)
print(f"Додавання ({a} + {b}): {a + b}")
print(f"Віднімання ({a} - {b}): {a - b}")
print(f"Множення ({a} * {b}): {a * b}")
print(f"Ділення ({a} / {b}): {a / b}")
print(f"Цілочисельне ділення ({a} // {b}): {a // b}")
print(f"Остача від ділення ({a} % {b}): {a % b}")
print(f"Піднесення до степеня ({a} ** 2): {a ** 2}")

print("-" * 20)

# Оператори порівняння (>, <, ==, !=, >=, <=)
print(f"Більше ({a} > {b}): {a > b}")
print(f"Менше або дорівнює ({b} <= 5): {b <= 5}")
print(f"Діє рівність ({a} == 12): {a == 12}")
print(f"Нерівно ({a} != {b}): {a != b}")

print("-" * 20)

# Логічні оператори (and, or, not)
is_active = True
has_permissions = False
print(f"Логічне AND (True and False): {is_active and has_permissions}")
print(f"Логічне OR (True or False): {is_active or has_permissions}")
print(f"Логічне NOT (not True): {not is_active}")

print("-" * 20)

# Оператори присвоєння зі зміною (+=, -= тощо)
score = 50
score += 25  # те саме що score = score + 25
print(f"Оператор присвоєння зі зміною (50 += 25): {score}")

# Оператор належності (in)
target_num = 20
print(f"Чи є число {target_num} у списку list_data? {target_num in list_data}")






























