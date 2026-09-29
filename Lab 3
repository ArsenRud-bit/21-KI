# Лабораторна робота №3: Консольний міні-магазин
# Дедлайн: 12 жовтня включно

# Початкові дані (каталог товарів та залишки на складі)
catalog = {
    "1": {"name": "Пряники «Козацькі»", "price": 45.50, "stock": 15},
    "2": {"name": "Енергетик Monster Ultra", "price": 68.00, "stock": 8},
    "3": {"name": "Шоколад Roshen", "price": 38.90, "stock": 20},
    "4": {"name": "Чіпси Lays", "price": 55.00, "stock": 12}
}

cart = {}

# Лямбда-функція для форматування ціни (формат: xxx.xxгрн)
format_price = lambda price: f"{price:.2f}грн"


def show_catalog():
    print("\n--- КАТАЛОГ ТОВАРІВ ---")
    # Використання лямбди для сортування товарів за ціною (від дешевших до дорожчих)
    sorted_items = sorted(catalog.items(), key=lambda item: item[1]["price"])

    for key, product in sorted_items:
        print(f"[{key}] {product['name']} — {format_price(product['price'])} (В наявності: {product['stock']} шт.)")


def add_to_cart():
    show_catalog()
    choice = input("\nВведіть номер товару, щоб додати в кошик: ")
    if choice in catalog:
        try:
            qty = int(input("Введіть кількість: "))
            if qty <= 0:
                print("Кількість має бути більшою за нуль!")
                return
            if catalog[choice]["stock"] >= qty:
                if choice in cart:
                    cart[choice] += qty
                else:
                    cart[choice] = qty
                print(f"Товар успішно додано до кошика!")
            else:
                print(f"Недостатньо товару на складі! Доступно: {catalog[choice]['stock']} шт.")
        except ValueError:
            print("Помилка: введіть ціле число для кількості.")
    else:
        print("Такого товару немає в каталозі.")


def remove_from_cart():
    if not cart:
        print("\nВаш кошик порожній.")
        return

    print("\n--- ВАШ КОШИК ---")
    for key, qty in cart.items():
        print(f"[{key}] {catalog[key]['name']} — {qty} шт.")

    choice = input("\nВведіть номер товару для видалення з кошика: ")
    if choice in cart:
        try:
            qty_to_remove = int(input("Скільки штук видалити?: "))
            if qty_to_remove >= cart[choice]:
                del cart[choice]
                print("Товар повністю видалено з кошика.")
            else:
                cart[choice] -= qty_to_remove
                print(f"Видалено {qty_to_remove} шт. товару.")
        except ValueError:
            print("Помилка: введіть коректне число.")
    else:
        print("Цього товару немає у вашому кошику.")


def checkout():
    if not cart:
        print("\nКошик порожній. Купівля неможлива.")
        return

    print("\n--- ОФОРМЛЕННЯ ЗАМОВЛЕННЯ ---")
    total = 0
    # Лямбда для підрахунку загальної вартості позиції
    calculate_subtotal = lambda price, qty: price * qty

    for key, qty in cart.items():
        product = catalog[key]
        subtotal = calculate_subtotal(product["price"], qty)
        total += subtotal
        # Зменшуємо залишки на складі
        catalog[key]["stock"] -= qty
        print(f"- {product['name']} x {qty} = {format_price(subtotal)}")

    print(f"Загальна сума до сплати: {format_price(total)}")
    print("Дякуємо за покупку!")
    cart.clear()


def admin_panel():
    password = input("Введіть пароль адміністратора (пароль: admin123): ")
    if password == "admin123":
        print("\n--- ПАНЕЛЬ АДМІНІСТРАТОРА: ЗАЛИШКИ ТОВАРІВ ---")
        for key, product in catalog.items():
            print(
                f"[{key}] {product['name']} — Залишок: {product['stock']} шт. | Ціна: {format_price(product['price'])}")
    else:
        print("Неправильний пароль!")


def main():
    while True:
        print("\n=== МІНІ-МАГАЗИН ===")
        print("1. Переглянути каталог товарів")
        print("2. Додати товар в кошик")
        print("3. Видалити товар з кошика")
        print("4. Купити товари з кошика")
        print("5. Увійти як адміністратор (залишки)")
        print("6. Вихід")

        choice = input("Оберіть опцію (1-6): ")

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            admin_panel()
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, оберіть від 1 до 6.")


if __name__ == "__main__":
    main()
