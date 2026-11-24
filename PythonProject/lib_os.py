import os


def demo_os():
    try:
        print("Поточна папка:", os.getcwd())
        print("Файли:", os.listdir("."))
    except OSError as e:
        print("Помилка os:", e)