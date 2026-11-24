from colorama import Fore, Style, init


def demo_colorama():
    try:
        init(autoreset=True)
        print(Fore.RED + "Червоний текст")
        print(Fore.GREEN + "Зелений текст")
        print(Fore.YELLOW + Style.BRIGHT + "Яскравий жовтий текст")
    except Exception as e:
        print("Помилка colorama:", e)