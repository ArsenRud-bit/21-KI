import os
import io
import time
import requests
import numpy as np
import pandas as pd
from PIL import Image
import colorama
from colorama import Fore, Style
import pyfiglet
import qrcode
from faker import Faker
import wikipedia
from tqdm import tqdm

# Ініціалізація colorama для підтримки кольорів у консолі
colorama.init(autoreset=True)


def print_banner():
    """Виводить гарний заголовок за допомогою pyfiglet та colorama"""
    banner = pyfiglet.figlet_format("Data & QR Tool", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "=========================================================")
    print(Fore.GREEN + "  Демонстраційний скрипт, що об'єднує 10 Python-бібліотек")
    print(Fore.YELLOW + "=========================================================\n")


def main():
    print_banner()

    # 1. FAKER: Генерація фейкових даних користувачів
    print(Fore.BLUE + "[1/5] Генерація тестових даних користувачів (Faker)...")
    fake = Faker('uk_UA')  # Налаштування української локалізації
    users_data = []

    # tqdm для прогрес-бару генерації
    for _ in tqdm(range(50), desc="Створення профілів", unit="user"):
        users_data.append({
            "Name": fake.name(),
            "Email": fake.email(),
            "City": fake.city(),
            "Score": fake.random_int(min=50, max=100)
        })
        time.sleep(0.01)  # невелика затримка для демонстрації tqdm

    # 2. PANDAS & NUMPY: Аналіз та обробка даних
    print("\n" + Fore.BLUE + "[2/5] Обробка даних через Pandas та NumPy...")
    df = pd.DataFrame(users_data)

    # Використання NumPy для розрахунків
    scores = df['Score'].to_numpy()
    mean_score = np.mean(scores)
    std_dev = np.std(scores)

    print(Fore.MAGENTA + f" -> Всього створено записів: {len(df)}")
    print(Fore.MAGENTA + f" -> Середній бал (NumPy): {mean_score:.2f}")
    print(Fore.MAGENTA + f" -> Стандартне відхилення (NumPy): {std_dev:.2f}")

    # Збереження DataFrame у CSV
    csv_filename = "generated_users.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(Fore.GREEN + f" -> Дані успішно збережено у файл '{csv_filename}'")

    # 3. WIKIPEDIA: Отримання інформації
    print("\n" + Fore.BLUE + "[3/5] Запит інформації з Wikipedia...")
    wikipedia.set_lang("uk")
    search_query = "Python"
    try:
        wiki_page = wikipedia.page(search_query)
        wiki_summary = wikipedia.summary(search_query, sentences=2)
        print(Fore.MAGENTA + f" -> Стаття: {wiki_page.title}")
        print(Fore.WHITE + f" -> Короткий зміст: {wiki_summary}")
        wiki_url = wiki_page.url
    except Exception as e:
        print(Fore.RED + f" -> Помилка під час запиту до Вікіпедії: {e}")
        wiki_url = "https://www.python.org"

    # 4. REQUESTS & PILLOW (PIL): Завантаження та обробка зображення
    print("\n" + Fore.BLUE + "[4/5] Завантаження зображення через Requests та обробка у Pillow...")
    img_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

    try:
        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            # Відкриття зображення з байтів за допомогою Pillow
            img = Image.open(io.BytesIO(response.content))
            print(Fore.MAGENTA + f" -> Оригінальний розмір логотипу Python: {img.size} пікселів")

            # Зміна розміру зображення
            resized_img = img.resize((200, 60))
            resized_img.save("python_logo_small.png")
            print(Fore.GREEN + " -> Зображення зменшено та збережено як 'python_logo_small.png'")
    except Exception as e:
        print(Fore.RED + f" -> Не вдалося завантажити зображення: {e}")

    # 5. QRCODE: Створення QR-коду
    print("\n" + Fore.BLUE + "[5/5] Генерація QR-коду (qrcode)...")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wiki_url)
    qr.make(fit=True)

    # Перетворення QR-коду на Pillow-зображення та збереження
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_filename = "wikipedia_python_qr.png"
    qr_img.save(qr_filename)

    print(Fore.GREEN + f" -> Створено QR-код із посиланням на сторінку Вікіпедії: '{qr_filename}'")

    print("\n" + Fore.YELLOW + "=========================================================")
    print(Fore.GREEN + "Усі завдання успішно виконано!")
    print(Fore.YELLOW + "=========================================================")


import os
import json
import datetime
import random
import math


def print_separator():
    print("-" * 60)


def main():
    print("🤖 Вітаю! Запущено персонального помічника на стандартних бібліотеках Python.\n")
    print_separator()

    # 1. DATETIME: Робота з датою та часом
    print("📅 [1/5] Модуль datetime: аналіз часу")
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f" -> Поточна дата і час: {formatted_date}")

    # Вираховуємо, скільки днів залишилося до Нового року
    new_year = datetime.datetime(now.year + 1, 1, 1)
    days_left = (new_year - now).days
    print(f" -> До Нового року залишилось: {days_left} днів")
    print_separator()

    # 2. RANDOM: Генерація випадкових елементів
    print("🎲 [2/5] Модуль random: мотивація дня")
    quotes = [
        "Кожен день — це нова можливість покращити свій код.",
        "Маленькі кроки ведуть до великих досягнень.",
        "Помилки — це просто докази того, що ви намагаєтесь.",
        "Простий і чистий код завжди перемагає."
    ]
    daily_quote = random.choice(quotes)
    lucky_number = random.randint(1, 100)
    print(f" -> Цитата дня: \"{daily_quote}\"")
    print(f" -> Ваше щасливе число на сьогодні: {lucky_number}")
    print_separator()

    # 3. MATH: Математичні розрахунки
    print("📐 [3/5] Модуль math: розрахунок прогресу доби")
    # Вираховуємо відсоток часу, який вже минув від початку доби (у годинах та хвилинах)
    seconds_passed = now.hour * 3600 + now.minute * 60 + now.second
    total_seconds_in_day = 86400
    day_progress = (seconds_passed / total_seconds_in_day) * 100

    # Використовуємо math.floor для округлення вниз
    rounded_progress = math.floor(day_progress)
    print(f" -> Від доби вже минуло: {rounded_progress}%")
    print_separator()

    # 4. OS: Взаємодія з операційною системою та файловою системою
    print("📁 [4/5] Модуль os: перевірка та створення директорій")
    log_dir = "session_logs"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f" -> Створено нову папку для логів: '{log_dir}/'")
    else:
        print(f" -> Папка '{log_dir}/' вже існує.")

    current_os = os.name  # 'posix' або 'nt'
    print(f" -> Тип операційної системи (код): {current_os}")
    print_separator()

    # 5. JSON: Збереження даних у форматі JSON
    print("💾 [5/5] Модуль json: збереження звіту сесії")
    session_data = {
        "timestamp": formatted_date,
        "quote_of_the_day": daily_quote,
        "lucky_number": lucky_number,
        "day_progress_percent": rounded_progress,
        "days_to_new_year": days_left
    }

    file_path = os.path.join(log_dir, "last_session.json")

    # Записуємо дані у файл з підтримкою українських символів (ensure_ascii=False)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    print(f" -> Звіт успішно збережено у файл: '{file_path}'")
    print_separator()
    print("✨ Успішно виконано! Усі 5 вбудованих бібліотек спрацювали разом.")


if __name__ == "__main__":
    main()
