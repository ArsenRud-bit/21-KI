# Дані 4 користувачів (логін, пароль і список оцінок для кожного)
l1, p1, g1 = "arseniy", "123", [9, 2, 5, 7, 3, 4]
l2, p2, g2 = "olena", "321", [10, 12, 4, 3, 5]
l3, p3, g3 = "max", "111", [5, 6, 7, 2, 1, 9]
l4, p4, g4 = "katia", "222", [12, 11, 9, 4, 8]

# Запитуємо дані у користувача
user_login = input("Логін: ")
user_pass = input("Пароль: ")

# Змінні для результату
my_grades = []
success = False

# Перевіряємо кожного користувача окремо
if user_login == l1 and user_pass == p1:
  my_grades = g1
  success = True
elif user_login == l2 and user_pass == p2:
  my_grades = g2
  success = True
elif user_login == l3 and user_pass == p3:
  my_grades = g3
  success = True
elif user_login == l4 and user_pass == p4:
  my_grades = g4
  success = True

# Виводимо результат залежно від успішності входу
if success:
  print("\nУспішний вхід!")
  print("Усі оцінки:", *my_grades)

  bad = 0
  good = 0

  # Рахуємо оцінки за допомогою циклу for
  for mark in my_grades:
    if mark <= 4:
      bad += 1
    else:
      good += 1

  print("Незадовільні (1-4):", bad)
  print("Задовільні (5-12):", good)

else:
  print("\nНеправильний логін або пароль!")
























