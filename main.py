"""Точка входу."""
from exceptions import QuitGame
from game import Game


def main():
    try:
        Game().run()
    except QuitGame:
        print("\nВи вийшли з гри. До зустрічі!")
    except KeyboardInterrupt:
        print("\nГру перервано.")
    except Exception as e:
        print(f"\nКритична помилка: {e}")
    finally:
        print("Дякуємо за гру!")


if __name__ == "__main__":
    main()