import pyfiglet


def demo_pyfiglet():
    try:
        print(pyfiglet.figlet_format("LAB 4"))
    except Exception as e:
        print("Помилка pyfiglet:", e)