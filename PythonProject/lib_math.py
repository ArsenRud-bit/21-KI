import math


def demo_math():
    try:
        print("sqrt(144) =", math.sqrt(144))
        print("pi =", round(math.pi, 4))
        print("sin(90°) =", math.sin(math.radians(90)))
    except Exception as e:
        print("Помилка math:", e)