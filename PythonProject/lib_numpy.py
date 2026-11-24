import numpy as np


def demo_numpy():
    try:
        arr = np.arange(1, 11)
        print("Масив:", arr)
        print("Сума:", arr.sum(), "| Середнє:", arr.mean())
        print("Квадрати:", arr ** 2)
    except Exception as e:
        print("Помилка numpy:", e)