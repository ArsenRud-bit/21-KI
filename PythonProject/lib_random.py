import random


def demo_random():
    try:
        print("Випадкове число 1-100:", random.randint(1, 100))
        print("Вибір зі списку:", random.choice(["яблуко", "груша", "слива"]))
        nums = [1, 2, 3, 4, 5]
        random.shuffle(nums)
        print("Перемішаний список:", nums)
    except Exception as e:
        print("Помилка random:", e)