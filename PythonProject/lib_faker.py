from faker import Faker


def demo_faker():
    try:
        fake = Faker("uk_UA")
        for _ in range(3):
            print(fake.name(), "|", fake.city(), "|", fake.email())
    except Exception as e:
        print("Помилка faker:", e)